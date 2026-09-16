/**
 * Minimal FINA WEB API client (no dependencies; Node 18+ or any fetch runtime).
 *
 * A direct counterpart to fina_client.py, handling the three things every FINA
 * client has to get right and that are easy to get wrong:
 *
 *   - the token is valid for 36 hours, so it is cached rather than re-fetched
 *     per call (re-authenticating on every request is the usual cause of a slow
 *     integration);
 *   - `ex` in the response body signals failure even when the HTTP status is
 *     200, so it is checked on every call;
 *   - a 401 means the token expired, so it re-authenticates once and retries
 *     rather than relying on expiry arithmetic, which clock skew makes
 *     unreliable.
 *
 * Usage:
 *   const fina = new FinaClient({ baseUrl: "http://192.168.1.10:8080",
 *                                 login: "login", password: "password" });
 *   const { products } = await fina.get<{ products: Product[] }>("getProducts");
 *   const { id } = await fina.post<{ id: number }>("saveDocProductOut", payload);
 */

export class FinaError extends Error {}

export interface FinaClientOptions {
  baseUrl: string;
  login: string;
  password: string;
  /** Required only on MultiTenant installations. */
  tenantKey?: string;
  timeoutMs?: number;
}

/** Format a Date the way FINA expects: no offset, no trailing Z.
 *
 * The server interprets the value in its own local time, so sending an ISO
 * string (which is UTC) posts the document at the wrong time. */
export function finaDateTime(value: Date): string {
  const pad = (n: number) => String(n).padStart(2, "0");
  return (
    `${value.getFullYear()}-${pad(value.getMonth() + 1)}-${pad(value.getDate())}` +
    `T${pad(value.getHours())}:${pad(value.getMinutes())}:${pad(value.getSeconds())}`
  );
}

type Area = "operation" | "reporting";

export class FinaClient {
  private readonly baseUrl: string;
  private readonly login: string;
  private readonly password: string;
  private readonly tenantKey?: string;
  private readonly timeoutMs: number;
  private token: string | null = null;

  constructor(options: FinaClientOptions) {
    this.baseUrl = options.baseUrl.replace(/\/+$/, "");
    this.login = options.login;
    this.password = options.password;
    this.tenantKey = options.tenantKey;
    this.timeoutMs = options.timeoutMs ?? 60_000;
  }

  private headers(): Record<string, string> {
    const headers: Record<string, string> = {
      "Content-Type": "application/json",
      Accept: "application/json",
    };
    if (this.token) headers.Authorization = `Bearer ${this.token}`;
    if (this.tenantKey) headers.tenant_key = this.tenantKey;
    return headers;
  }

  private async send(method: string, url: string, body?: unknown): Promise<Response> {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), this.timeoutMs);
    try {
      return await fetch(url, {
        method,
        headers: this.headers(),
        body: body === undefined ? undefined : JSON.stringify(body),
        signal: controller.signal,
      });
    } finally {
      clearTimeout(timer);
    }
  }

  async authenticate(): Promise<string> {
    this.token = null; // never send a stale token on the auth call itself
    const response = await this.send(
      "POST",
      `${this.baseUrl}/api/authentication/authenticate`,
      { login: this.login, password: this.password },
    );
    const result = (await response.json()) as { token?: string; ex?: string };
    if (result.ex) throw new FinaError(`authentication failed: ${result.ex}`);
    if (!result.token) throw new FinaError("authentication returned no token");
    this.token = result.token;
    return result.token;
  }

  /**
   * Call any FINA method. Path arguments are appended in order, which is how
   * FINA passes parameters (there are no query strings).
   */
  async call<T>(
    area: Area,
    method: string,
    { pathArgs = [], body, httpMethod }: {
      pathArgs?: Array<string | number>;
      body?: unknown;
      httpMethod?: string;
    } = {},
  ): Promise<T> {
    if (this.token === null) await this.authenticate();

    const verb = httpMethod ?? (body === undefined ? "GET" : "POST");
    const segments = pathArgs.map((a) => encodeURIComponent(String(a))).join("/");
    const url = `${this.baseUrl}/api/${area}/${method}` + (segments ? `/${segments}` : "");

    let response = await this.send(verb, url, body);
    if (response.status === 401) {
      // The 36-hour token expired; get a new one and retry once.
      await this.authenticate();
      response = await this.send(verb, url, body);
    }
    if (!response.ok) {
      const detail = (await response.text()).slice(0, 500);
      throw new FinaError(`HTTP ${response.status} calling ${method}: ${detail}`);
    }

    const text = await response.text();
    const result = (text ? JSON.parse(text) : {}) as T & { ex?: string };
    // A 200 with a non-null `ex` is a failure. This is the check that a client
    // written against the HTTP status alone will miss.
    if (result && result.ex) throw new FinaError(`${method}: ${result.ex}`);
    return result;
  }

  get<T>(method: string, ...pathArgs: Array<string | number>): Promise<T> {
    return this.call<T>("operation", method, { pathArgs });
  }

  post<T>(method: string, body: unknown, ...pathArgs: Array<string | number>): Promise<T> {
    return this.call<T>("operation", method, { pathArgs, body });
  }

  report<T>(method: string, ...pathArgs: Array<string | number>): Promise<T> {
    return this.call<T>("reporting", method, { pathArgs });
  }
}
