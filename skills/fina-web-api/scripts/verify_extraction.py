#!/usr/bin/env python3
"""Verify methods.json against the source PDF.

Extraction is only trustworthy if it is checked, so this asserts the invariants
that would catch silent corruption: every method named in the table of contents
is present, paths and verbs match the PDF text, JSON examples are balanced, and
no description has bled into the next method's heading.

Usage: python3 scripts/verify_extraction.py <pdf> assets/methods.json
"""

import json
import re
import sys

from pypdf import PdfReader

TOC_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_]*)\s*[-–—]\s*\S")


def main(pdf_path, json_path):
    data = json.load(open(json_path, encoding="utf-8"))
    methods = data["methods"]
    by_name = {m["name"]: m for m in methods}

    reader = PdfReader(pdf_path)
    pages = [p.extract_text() or "" for p in reader.pages]
    full = "\n".join(pages)
    # Paths are compared against a whitespace-stripped copy: a couple of
    # endpoints are typeset with a stray space inside the path, so the repaired
    # value is correct but not literally present in the extracted text.
    full_nospace = re.sub(r"\s+", "", full)

    # The table of contents (pages 2-6) is an independent list of every method,
    # so comparing against it catches anything the body parser skipped.
    toc = set()
    for page in pages[1:6]:
        for line in page.split("\n"):
            m = TOC_RE.match(line.strip())
            if m:
                toc.add(m.group(1))

    failures = []

    missing = toc - set(by_name)
    if missing:
        failures.append(f"in TOC but not extracted: {sorted(missing)}")
    extra = set(by_name) - toc
    if extra:
        failures.append(f"extracted but not in TOC: {sorted(extra)}")

    for m in methods:
        name = m["name"]
        if m["http_method"] not in ("GET", "POST"):
            failures.append(f"{name}: bad verb {m['http_method']!r}")
        if not m["path"].startswith("api/"):
            failures.append(f"{name}: bad path {m['path']!r}")
        # The path must actually name the method. A typographic space in the
        # source once truncated a path to its base, which "starts with api/"
        # happily accepts.
        segments = [s for s in m["path"].split("/") if s]
        if name not in segments:
            failures.append(f"{name}: path {m['path']!r} does not contain the method name")
        # The endpoint must appear in the PDF, ignoring typographic spaces.
        if m["path"] not in full_nospace:
            failures.append(f"{name}: path not found verbatim in PDF")
        if not m["title_ka"]:
            failures.append(f"{name}: missing Georgian title")
        if not m["response"] and not m["response_same_as"]:
            failures.append(f"{name}: no response example and no cross-reference")
        if m["response_same_as"] and m["response_same_as"] not in by_name:
            failures.append(f"{name}: cross-references unknown {m['response_same_as']}")
        if m["http_method"] == "POST" and not m["request_body"]:
            failures.append(f"{name}: POST with no request body")
        # Every {placeholder} in the path must be documented.
        for ph in re.findall(r"\{(\w+)\}", m["path"]):
            if ph not in {p["name"] for p in m["path_params"]}:
                failures.append(f"{name}: undocumented path param {{{ph}}}")
        # Bleed detection. A description that ran into the next method picks up
        # its heading, which always reads "<name> - <Georgian title>". An inline
        # cross-reference ("see method getDiscountTypes") has no trailing dash,
        # so the dash is what separates corruption from a genuine reference.
        for bucket in ("request_fields", "response_fields", "path_params"):
            for f in m[bucket]:
                for other in by_name:
                    if other == name:
                        continue
                    if re.search(r"\b" + other + r"\s*[-\u2013\u2014]\s+\S",
                                 f["description_ka"]):
                        failures.append(
                            f"{name}.{f['name']}: description bled into {other}")
        for blob in (m["request_body"], m["response"]):
            if blob and blob.count("{") != blob.count("}"):
                failures.append(f"{name}: unbalanced JSON example")

    print(f"methods: {len(methods)} | TOC entries: {len(toc)}")
    print(f"fields: {sum(len(m['request_fields']) + len(m['response_fields']) + len(m['path_params']) for m in methods)}")
    inconsistent = [m['name'] for m in methods if m['doc_inconsistencies']]
    print(f"methods with source doc inconsistencies: {len(inconsistent)}")

    if failures:
        print(f"\nFAILED ({len(failures)}):")
        for f in failures[:40]:
            print("  -", f)
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
