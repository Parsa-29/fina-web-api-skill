#!/usr/bin/env python3
"""Minimal FINA WEB API client (standard library only).

Deliberately dependency-free so it can be dropped into any project. It handles
the three things every FINA client has to get right and that are easy to get
wrong:

  * the token is valid for 36 hours, so it is cached rather than re-fetched per
    call (re-authenticating on every request is the usual cause of a slow
    integration);
  * `ex` in the response body signals failure even when the HTTP status is 200,
    so it is checked on every call;
  * a 401 means the token expired, so it re-authenticates once and retries
    rather than relying on expiry arithmetic, which clock skew makes unreliable.

Usage:
    fina = FinaClient("http://192.168.1.10:8080", "login", "password")
    products = fina.get("getProducts")["products"]
    doc_id = fina.post("saveDocProductOut", payload)["id"]
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from datetime import datetime
from typing import Any

FINA_DATETIME = "%Y-%m-%dT%H:%M:%S"


def fina_datetime(value: datetime) -> str:
    """Format a datetime the way FINA expects: no offset, no trailing Z.

    The server interprets the value in its own local time, so passing a UTC
    timestamp posts the document at the wrong time.
    """
    return value.strftime(FINA_DATETIME)


class FinaError(RuntimeError):
    """Raised when FINA reports a failure, via `ex` or via an HTTP status."""


class FinaClient:
    def __init__(self, base_url: str, login: str, password: str,
                 tenant_key: str | None = None, timeout: int = 60):
        self.base_url = base_url.rstrip("/")
        self.login = login
        self.password = password
        self.tenant_key = tenant_key  # required only on MultiTenant installations
        self.timeout = timeout
        self._token: str | None = None

    # -- transport ---------------------------------------------------------

    def _headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        if self.tenant_key:
            headers["tenant_key"] = self.tenant_key
        return headers

    def _send(self, method: str, url: str, body: Any) -> dict:
        data = json.dumps(body).encode("utf-8") if body is not None else None
        request = urllib.request.Request(url, data=data, method=method,
                                         headers=self._headers())
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            payload = response.read().decode("utf-8")
        return json.loads(payload) if payload else {}

    def authenticate(self) -> str:
        url = f"{self.base_url}/api/authentication/authenticate"
        self._token = None  # never send a stale token on the auth call itself
        result = self._send("POST", url, {"login": self.login,
                                          "password": self.password})
        if result.get("ex"):
            raise FinaError(f"authentication failed: {result['ex']}")
        token = result.get("token")
        if not token:
            raise FinaError("authentication returned no token")
        self._token = token
        return token

    def call(self, area: str, method: str, *path_args: Any,
             body: Any = None, http_method: str | None = None) -> dict:
        """Call any FINA method.

        `area` is "operation" or "reporting". Path arguments are appended in
        order, which is how FINA passes parameters (there are no query strings).
        """
        if self._token is None:
            self.authenticate()

        verb = http_method or ("POST" if body is not None else "GET")
        segments = "/".join(str(a) for a in path_args)
        url = f"{self.base_url}/api/{area}/{method}"
        if segments:
            url = f"{url}/{segments}"

        try:
            result = self._send(verb, url, body)
        except urllib.error.HTTPError as exc:
            if exc.code == 401:
                # The 36-hour token expired; get a new one and retry once.
                self.authenticate()
                result = self._send(verb, url, body)
            else:
                detail = exc.read().decode("utf-8", "replace")[:500]
                raise FinaError(f"HTTP {exc.code} calling {method}: {detail}") from exc

        # A 200 with a non-null `ex` is a failure. This is the check that a
        # client written against the HTTP status alone will miss.
        if isinstance(result, dict) and result.get("ex"):
            raise FinaError(f"{method}: {result['ex']}")
        return result

    # -- conveniences ------------------------------------------------------

    def get(self, method: str, *path_args: Any) -> dict:
        return self.call("operation", method, *path_args)

    def post(self, method: str, body: Any, *path_args: Any) -> dict:
        return self.call("operation", method, *path_args, body=body)

    def report(self, method: str, *path_args: Any) -> dict:
        return self.call("reporting", method, *path_args)
