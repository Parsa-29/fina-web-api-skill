#!/usr/bin/env python3
"""Extract the version history table into references/changelog.md.

Version history answers a question the per-method pages cannot: whether the
server a developer is actually integrating with has the method or field they
just found. FINA servers in the wild run older builds, so "getLoyaltyCustomers
exists" is only half an answer.

The table is a Word table with merged cells, so the flattened text interleaves
versions, method names and change descriptions. Rather than guess at the cell
structure, this splits on version numbers and reports what each block mentions,
keeping the Georgian so nothing is lost when the shape is ambiguous.

Usage: python3 scripts/extract_changelog.py <pdf> [-o references/changelog.md]
"""

import argparse
import json
import re

from pypdf import PdfReader

VERSION_RE = re.compile(r"\b(\d+\.\d+\.\d{8})\b")

# The handful of change phrases the table actually uses.
PHRASES = [
    (re.compile(r"დაემატა ახალი მეთოდები"), "new methods added"),
    (re.compile(r"დაემატა ახალი მეთოდი"), "new method added"),
    (re.compile(r"დაემატა ველები:\s*([A-Za-z0-9_,\s]+)"), "fields added: {}"),
    (re.compile(r"დაემატა ველი:\s*([A-Za-z0-9_,\s]+)"), "field added: {}"),
    (re.compile(r"გაუქმდა\s*/\s*ჩანაცვლდა მეთოდით\s*[-–—]?\s*(\w+)"),
     "removed / replaced by {}"),
    (re.compile(r"დაემატა swagger"), "Swagger added"),
    (re.compile(r"დაემატა PostgreSQL"), "PostgreSQL support added"),
    (re.compile(r"თოქენის მოქმედების ვადა შემცირდა 36"),
     "token lifetime reduced to 36 hours"),
    (re.compile(r"ერთმანეთისგან გაიმიჯნა ველები:\s*([A-Za-z0-9_,\s]+)"),
     "fields separated from one another: {}"),
    (re.compile(r"დაემატა ყველა ტიპის ფასის წამოღება"),
     "fetching all price types added"),
]


def clean_field_list(raw):
    """Trim a captured field list to just the field names.

    A list may legitimately wrap across lines ("invoice_num, invoice_bank,\n
    pay_date"), so newlines cannot end the capture. But the line after an
    unwrapped list starts with the next method name, which then rides along on
    the final item. Each comma-separated item is a single identifier, so keeping
    only the first token of each drops the intruder without losing wrapped
    entries.
    """
    items = []
    for chunk in raw.split(","):
        token = chunk.split()
        if token:
            items.append(token[0])
    return ", ".join(items)


def summarise(text):
    out = []
    for pattern, template in PHRASES:
        for m in pattern.finditer(text):
            out.append(template.format(clean_field_list(m.group(1)))
                       if "{}" in template else template)
    # Preserve order of first appearance without duplicates.
    seen, ordered = set(), []
    for item in out:
        if item not in seen:
            seen.add(item)
            ordered.append(item)
    return ordered


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("-m", "--methods", default="assets/methods.json")
    ap.add_argument("-o", "--out", default="references/changelog.md")
    args = ap.parse_args()

    known = {m["name"] for m in
             json.load(open(args.methods, encoding="utf-8"))["methods"]}

    reader = PdfReader(args.pdf)
    # Skip the table of contents, which lists both section headings with dot
    # leaders and would otherwise yield an empty slice between them.
    pages = [p.extract_text() or "" for p in reader.pages]
    body_start = next(i for i, t in enumerate(pages) if "FINA Web API" in t and i > 2)
    text = "\n".join(pages[body_start:])
    start = text.find("ცვლილებები:")
    end = text.find("ავტორიზაცია:", start)
    table = text[start:end if end != -1 else None]

    parts = VERSION_RE.split(table)
    entries = []
    for i in range(1, len(parts), 2):
        version, body = parts[i], parts[i + 1]
        methods = [n for n in sorted(set(re.findall(r"\b([a-z][A-Za-z0-9_]{3,})\b", body)))
                   if n in known]
        entries.append((version, methods, summarise(body), body))

    out = ["# Version history", "",
           "Which FINA release introduced each method and field. Check this before "
           "relying on anything recent: servers in the field run older builds, and a "
           "method that exists in this documentation may simply not be present on the "
           "server being integrated with.", "",
           "The source table uses merged cells, so a version's changes are listed "
           "together rather than strictly paired with individual methods. The Georgian "
           "original is kept for anything ambiguous.", "",
           "| Version | Methods affected | Change |", "|---|---|---|"]
    for version, methods, changes, _ in entries:
        names = ", ".join(f"`{n}`" for n in methods) or "—"
        change = "; ".join(changes) or "—"
        out.append(f"| `{version}` | {names} | {change} |")

    # Reverse index: the question is usually "when did X appear?", not
    # "what changed in version Y?".
    out += ["", "---", "", "## By method", "",
            "The earliest version in which each method is mentioned. A method with no "
            "entry predates this changelog.", "",
            "| Method | First mentioned in |", "|---|---|"]
    first = {}
    for version, methods, _, _ in entries:
        for n in methods:
            first[n] = version  # entries run newest-first, so the last wins
    for n in sorted(first):
        out.append(f"| `{n}` | `{first[n]}` |")

    open(args.out, "w", encoding="utf-8").write("\n".join(out).rstrip() + "\n")
    print(f"{args.out}: {len(entries)} versions, {len(first)} methods referenced")


if __name__ == "__main__":
    main()
