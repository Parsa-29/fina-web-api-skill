#!/usr/bin/env python3
"""Collect every unique Georgian string from methods.json into a glossary.

Translating in a separate, reviewable glossary rather than inline keeps the
work honest: the same phrase always renders the same way, a human can audit all
translations in one place, and re-running the extractor for a future API
revision only surfaces the strings that are genuinely new.

Existing translations are preserved, so this is safe to re-run.

Usage: python3 scripts/build_glossary.py [-g assets/glossary.ka-en.json]
"""

import argparse
import json
import os
from collections import Counter


def collect(methods):
    counts = Counter()
    for m in methods:
        counts[m["title_ka"]] += 1
        counts[m["description_ka"]] += 1
        for note in m.get("notes_ka", []):
            counts[note] += 1
        for bucket in ("request_fields", "response_fields", "path_params"):
            for f in m[bucket]:
                counts[f["description_ka"]] += 1
                for e in f["enum_values"]:
                    counts[e["meaning_ka"]] += 1
    counts.pop("", None)
    return counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--methods", default="assets/methods.json")
    ap.add_argument("-g", "--glossary", default="assets/glossary.ka-en.json")
    args = ap.parse_args()

    methods = json.load(open(args.methods, encoding="utf-8"))["methods"]
    counts = collect(methods)

    existing = {}
    if os.path.exists(args.glossary):
        existing = json.load(open(args.glossary, encoding="utf-8"))["terms"]

    # Frequency order puts the highest-leverage strings first: the top 12 cover
    # a fifth of all occurrences.
    terms = {ka: existing.get(ka, "") for ka, _ in counts.most_common()}
    done = sum(1 for v in terms.values() if v)

    with open(args.glossary, "w", encoding="utf-8") as fh:
        json.dump({
            "_comment": "Georgian -> English. Empty value = not yet translated.",
            "occurrences": sum(counts.values()),
            "unique": len(terms),
            "translated": done,
            "terms": terms,
        }, fh, ensure_ascii=False, indent=1)
    print(f"{len(terms)} unique strings, {done} translated, {len(terms) - done} remaining")


if __name__ == "__main__":
    main()
