#!/usr/bin/env python3
"""Generate references/index.md and references/enums.md.

index.md is the routing table: it is the one file that is always worth reading
in full, because picking the wrong method is the most expensive mistake an
integration can make. enums.md collects every coded value in one place, since
they are otherwise buried inside individual field descriptions and a wrong
magic number posts a wrong document.

Usage: python3 scripts/render_overview.py [-o references]
"""

import argparse
import json
import os
from collections import defaultdict


def build_index(methods, mapping, glossary, groups):
    where = {n: f for f, names in mapping.items() for n in names}
    titles = {g["file"]: g["title"] for g in groups}

    out = ["# Method index", "",
           f"All {len(methods)} methods in FINA WEB API 10.0. Find the method here, "
           "then open the reference file named in the last column for its full "
           "request/response schema.", "",
           "Reading this table first is worth the tokens: the API has several "
           "near-identical methods whose differences matter (a full pull versus an "
           "incremental one, all stores versus a single store), and choosing wrong "
           "produces code that looks right and syncs the wrong data.", ""]

    by_file = defaultdict(list)
    for m in methods:
        by_file[where[m["name"]]].append(m)

    out += ["## Quick routing", "",
            "| If you need to… | Look in |", "|---|---|"]
    for g in groups:
        f = g["file"]
        if f in by_file:
            out.append(f"| {titles[f]} | [`{f}`]({f}) |")
    out += ["", "---", ""]

    for g in groups:
        f = g["file"]
        if f not in by_file:
            continue
        out += [f"## {titles[f]}", "", f"→ [`{f}`]({f})", "",
                "| Method | Verb | Endpoint | Purpose |", "|---|---|---|---|"]
        for m in by_file[f]:
            purpose = glossary.get(m["title_ka"]) or m["title_ka"]
            out.append(f"| [`{m['name']}`]({f}#{m['name'].lower()}) | {m['http_method']} "
                       f"| `{m['path']}` | {purpose} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def build_enums(methods, mapping, glossary):
    """Group identical enum sets so the same coded list is stated once."""
    where = {n: f for f, names in mapping.items() for n in names}
    seen = {}
    for m in methods:
        for bucket in ("request_fields", "response_fields", "path_params"):
            for field in m[bucket]:
                if not field["enum_values"]:
                    continue
                key = (field["name"], tuple(
                    (e["value"], e["meaning_ka"]) for e in field["enum_values"]))
                entry = seen.setdefault(key, {
                    "field": field["name"],
                    "values": field["enum_values"],
                    "used_by": [],
                })
                entry["used_by"].append((m["name"], where[m["name"]]))

    out = ["# Coded values (enums)", "",
           "Every coded value in the API, collected from the field descriptions "
           "where the source documentation buries them.", "",
           "These matter more than they look. The codes are bare integers with no "
           "symbolic names, several fields reuse the same numbers for different "
           "meanings (`pay_type` 1 is cashless, but `w_type` 1 does not exist and "
           "`t_payer` 1 is the buyer), and a wrong number posts a valid-looking "
           "document with the wrong semantics. Check the field name, not just the "
           "number.", ""]

    for entry in sorted(seen.values(), key=lambda e: (e["field"], -len(e["used_by"]))):
        out += [f"## `{entry['field']}`", "", "| Value | Meaning |", "|---|---|"]
        for e in entry["values"]:
            meaning = glossary.get(e["meaning_ka"]) or e["meaning_ka"]
            out.append(f"| `{e['value']}` | {meaning} · *{e['meaning_ka']}* |")
        users = ", ".join(f"[`{n}`]({f}#{n.lower()})" for n, f in entry["used_by"][:8])
        extra = "" if len(entry["used_by"]) <= 8 else f" and {len(entry['used_by']) - 8} more"
        out += ["", f"Used by: {users}{extra}", ""]
    return "\n".join(out).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--methods", default="assets/methods.json")
    ap.add_argument("-g", "--glossary", default="assets/glossary.ka-en.json")
    ap.add_argument("-c", "--groups", default="assets/groups.json")
    ap.add_argument("-o", "--out", default="references")
    args = ap.parse_args()

    methods = json.load(open(args.methods, encoding="utf-8"))["methods"]
    glossary = json.load(open(args.glossary, encoding="utf-8"))["terms"]
    groups = json.load(open(args.groups, encoding="utf-8"))["groups"]

    import render_references
    mapping = render_references.assign(groups, methods)

    for name, text in (("index.md", build_index(methods, mapping, glossary, groups)),
                       ("enums.md", build_enums(methods, mapping, glossary))):
        path = os.path.join(args.out, name)
        open(path, "w", encoding="utf-8").write(text)
        print(f"{path}: {os.path.getsize(path) // 1024}KB")


if __name__ == "__main__":
    main()
