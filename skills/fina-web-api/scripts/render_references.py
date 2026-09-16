#!/usr/bin/env python3
"""Render the bilingual reference files from methods.json + the glossary.

Everything here is generated, never hand-edited: methods.json holds what the
PDF says, the glossary holds how each Georgian phrase is translated, and this
script is the only place that decides presentation. Regenerating after a new
API revision is therefore a mechanical step rather than a rewrite.

Usage: python3 scripts/render_references.py [-o references]
"""

import argparse
import json
import os
import re

TYPE_HINT = {
    "byte": "byte", "sbyte": "sbyte", "int": "int", "long": "long",
    "decimal": "decimal", "double": "double", "string": "string",
    "bool": "bool", "datetime": "datetime", "date": "date", "object": "object",
}


def anchor(name):
    return name.lower()


class Renderer:
    def __init__(self, methods, glossary):
        self.by_name = {m["name"]: m for m in methods}
        self.glossary = glossary

    def en(self, ka):
        """Translate, falling back to the original so nothing silently vanishes."""
        if not ka:
            return ""
        return self.glossary.get(ka) or ka

    def bilingual(self, ka):
        """English first (the model reads this), Georgian kept for verification."""
        english = self.en(ka)
        if not ka or english == ka:
            return english
        return f"{english} · *{ka}*"

    def field_rows(self, fields):
        """Render fields as dotted paths so nesting is unambiguous in a table."""
        rows = []
        containers = {f["name"]: f for f in fields if f["type"] in ("collection", "object")}
        for f in fields:
            path = f["name"]
            parent = f["parent"]
            seen = set()
            while parent and parent not in seen:
                seen.add(parent)
                marker = "[]" if containers.get(parent, {}).get("type") == "collection" else ""
                path = f"{parent}{marker}.{path}"
                parent = containers.get(parent, {}).get("parent")
            if f["type"] == "collection":
                path += "[]"

            if f["type"] in ("collection", "object"):
                type_cell = f["type"]
            else:
                type_cell = TYPE_HINT.get(f["type"], f["type"])
                if f.get("is_array"):
                    type_cell += "[]"
                if f.get("max_length"):
                    type_cell += f"[{f['max_length']}]"
                if f.get("nullable"):
                    type_cell += "?"

            desc = self.bilingual(f["description_ka"]).replace("|", "\\|")
            rows.append(f"| `{path}` | {type_cell} | {desc} |")
        return rows

    def table(self, title, fields):
        if not fields:
            return []
        out = ([title, ""] if title else []) + [
            "| Field | Type | Description |", "|---|---|---|"]
        out += self.field_rows(fields)
        out.append("")
        return out

    def malformed(self, valid, what):
        """Note examples that are not parseable JSON as printed in the source.

        These are typos in the PDF (a stray comma, a missing one). Copying the
        example verbatim will fail to parse, and the cause is not obvious, so
        it is worth saying out loud rather than silently repairing.
        """
        if valid is False:
            return [f"> [!NOTE]", f"> The {what} example above is not valid JSON as "
                    f"printed in the source documentation (it contains a typo such as "
                    f"a stray or missing comma). The field list below is authoritative.",
                    ""]
        return []

    def warnings(self, m):
        """Surface places where the source contradicts itself.

        The JSON example is what the API actually returns, so it wins; the
        prose is what a reader would otherwise trust. Saying so explicitly is
        the whole point, because this is invisible when reading the PDF.
        """
        undoc = [x["field"] for x in m["doc_inconsistencies"]
                 if x["kind"] == "undocumented"]
        absent = [x["field"] for x in m["doc_inconsistencies"]
                  if x["kind"] == "absent_from_example"]
        if not undoc and not absent:
            return []
        out = ["> [!WARNING]", "> **The source documentation is inconsistent here.**"]
        if undoc:
            names = ", ".join(f"`{n}`" for n in undoc)
            out.append(f"> {names} appear in the JSON example but are never described "
                       f"in the field list. They are real — the example is what the "
                       f"API returns.")
        if absent:
            names = ", ".join(f"`{n}`" for n in absent)
            out.append(f"> {names} are described in the field list but do not appear in "
                       f"the JSON example. Verify against a live response before relying "
                       f"on them.")
        out.append("")
        return out

    def method(self, m):
        out = [f"### {m['name']}", ""]
        out.append(self.bilingual(m["title_ka"]))
        out.append("")
        desc = self.bilingual(m["description_ka"])
        if desc:
            out += [desc, ""]
        out += [f"**{m['http_method']}** `{m['path']}`", ""]

        out += self.table("**Path parameters**", m["path_params"])

        if m["request_body"]:
            out += ["**Request body**", "", "```json", m["request_body"].strip(), "```", ""]
            out += self.malformed(m["request_body_valid_json"], "request body")
            out += self.table("", m["request_fields"])

        if m["response"]:
            out += ["**Response**", "", "```json", m["response"].strip(), "```", ""]
            out += self.malformed(m["response_valid_json"], "response")
            out += self.table("", m["response_fields"])
        elif m["response_same_as"]:
            target = m["response_same_as"]
            out += [f"**Response** — identical to [`{target}`](#{anchor(target)}).", ""]

        for note in m["notes_ka"]:
            english = self.en(note)
            if english and english not in " ".join(out):
                out += [f"> {english}", ""]

        out += self.warnings(m)

        if m["see_also"]:
            links = ", ".join(f"`{s}`" for s in m["see_also"])
            out += [f"See also: {links}", ""]
        return out

    def file(self, title, names, preamble=None):
        # conventions.md carries hand-written prose that no per-method page can
        # express; everything after it is still generated.
        if preamble:
            lines = []
            for n in names:
                lines += self.method(self.by_name[n])
            return preamble + "\n".join(lines).rstrip() + "\n"
        out = [f"# {title}", "",
               f"{len(names)} methods. Generated from *FINA WEB API 10.0* — do not "
               f"edit by hand; see `scripts/render_references.py`.", "",
               "| Method | Verb | Endpoint | Purpose |", "|---|---|---|---|"]
        for n in names:
            m = self.by_name[n]
            out.append(f"| [`{n}`](#{anchor(n)}) | {m['http_method']} | "
                       f"`{m['path']}` | {self.en(m['title_ka'])} |")
        out.append("")
        out.append("---")
        out.append("")
        for n in names:
            out += self.method(self.by_name[n])
            out.append("---")
            out.append("")
        return "\n".join(out).rstrip() + "\n"


def assign(groups, methods):
    """Map each method to its reference file, following the grouping config."""
    out = {}
    for g in groups:
        if "methods" in g:
            # An explicit list, used where document order does not match the
            # grouping a reader would expect.
            names = list(g["methods"])
        else:
            lo, hi = g["range"]
            names = [methods[i]["name"] for i in range(lo, hi + 1)] + g.get("extra", [])
        out[g["file"]] = [n for n in names if n not in g.get("exclude", [])]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--methods", default="assets/methods.json")
    ap.add_argument("-g", "--glossary", default="assets/glossary.ka-en.json")
    ap.add_argument("-c", "--groups", default="assets/groups.json")
    ap.add_argument("-o", "--out", default="references")
    ap.add_argument("--only", help="render just this file, for review")
    args = ap.parse_args()

    methods = json.load(open(args.methods, encoding="utf-8"))["methods"]
    glossary = json.load(open(args.glossary, encoding="utf-8"))["terms"]
    groups = json.load(open(args.groups, encoding="utf-8"))["groups"]

    r = Renderer(methods, glossary)
    mapping = assign(groups, methods)
    os.makedirs(args.out, exist_ok=True)

    for g in groups:
        if args.only and g["file"] != args.only:
            continue
        names = mapping[g["file"]]
        path = os.path.join(args.out, g["file"])
        pre = g.get("preamble")
        pre = open(pre, encoding="utf-8").read() if pre else None
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(r.file(g["title"], names, pre))
        size = os.path.getsize(path) // 1024
        print(f"{path}: {len(names)} methods, {size}KB")


if __name__ == "__main__":
    main()
