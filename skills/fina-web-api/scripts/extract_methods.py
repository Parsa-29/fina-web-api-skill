#!/usr/bin/env python3
"""Extract structured method records from the FINA WEB API PDF.

The PDF is highly regular: every method is introduced by a heading line
("getProducts - saqonlis katalogi") followed by labelled lines:

    fuNqcia:    <name>          (Georgian: ფუნქცია)
    aRwera:     <description>   (Georgian: აღწერა)
    meTodi:     GET | POST      (Georgian: მეთოდი)
    gamoZaxeba: api/...         (Georgian: გამოძახება)

then optional "Request Body:" / "Response:" JSON blocks, each followed by a
"sadac:" (სადაც - "where:") block listing every field as

    field_name (type[maxlen]) - description

This script turns all of that into methods.json. It deliberately does no
translation and no summarising: everything here is verbatim from the PDF, so
the output can be diffed against the source. Translation happens in phase 2.

Usage: python3 scripts/extract_methods.py <pdf> -o assets/methods.json
"""

import argparse
import json
import re
import sys

from pypdf import PdfReader

# Georgian labels used as structural markers in the document.
L_FUNC = "ფუნქცია:"
L_DESC = "აღწერა:"
L_HTTP = "მეთოდი:"
L_PATH = "გამოძახება:"
L_WHERE = "სადაც:"

# Top-level section headings (they appear on their own line before a method).
SECTIONS = {
    "ავტორიზაცია:": "authentication",
    "ოპერაციული მხარე:": "operation",
    "რეპორტინგი:": "reporting",
}

# A field definition line: name (type) - description, where the type may carry
# a max length (string[50]), a nullable marker (datetime?) or an array marker
# (int[]). Missing any of these spellings silently swallows the field into the
# previous one's description, so all three are matched explicitly.
FIELD_RE = re.compile(
    r"^(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*"
    r"\((?P<type>[A-Za-z][A-Za-z0-9 ]*?)\s*"
    r"(?:\[(?P<len>\d*)\])?(?P<nullable>\?)?\)\s*"
    r"[-–—]?\s*(?P<desc>.*)$"
)

# A container header introduces a nested object or array and always ends with a
# colon, e.g. "product_out - the goods sale, which consists of:" or "add_fields
# - collection of additional fields where:". Matching the trailing colon rather
# than the word "collection" catches single-object wrappers too, which most
# getDoc* methods use.
COLLECTION_RE = re.compile(
    r"^(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*[-–—]\s*(?P<desc>.+:)\s*$"
)

# Enum values embedded in descriptions: "(0 - not a payer, 1 - payer, ...)"
# or "(true - legal entity, false - natural person)".
ENUM_ITEM_RE = re.compile(r"(?:^|[,(])\s*(\d+|true|false)\s*[-–—]\s*([^,()]+)")


# Wingdings bullets and other private-use glyphs survive text extraction as
# meaningless codepoints; they add noise to every description.
JUNK_RE = re.compile(r"[\uf000-\uf8ff\u200b-\u200f]")


def clean(text):
    return re.sub(r"\s+", " ", JUNK_RE.sub(" ", text)).strip()


# Word turned some of the examples' straight quotes into typographic ones, so
# those blocks are not valid JSON as printed. Anyone copying the example hits a
# parse error for a reason invisible on the page.
SMART_QUOTES = {"\u201c": '"', "\u201d": '"', "\u2018": "'", "\u2019": "'"}


def normalise_json(text):
    if not text:
        return text, None
    for bad, good in SMART_QUOTES.items():
        text = text.replace(bad, good)
    try:
        json.loads(text)
        return text, True
    except Exception:
        return text, False


def page_text(page):
    """Extract a page's text with the running page-number header removed.

    The header matters because JSON blocks and field lists routinely span page
    breaks; leaving a stray "185" inside a JSON block would break brace
    matching and corrupt the example.
    """
    txt = page.extract_text() or ""
    lines = txt.split("\n")
    # Drop leading blank/number-only lines (the page number header).
    while lines and re.fullmatch(r"\s*\d*\s*", lines[0]):
        if lines[0].strip().isdigit() or not lines[0].strip():
            lines.pop(0)
        else:
            break
    return "\n".join(lines)


def load_body(pdf_path):
    """Return the document body (everything after the table of contents)."""
    reader = PdfReader(pdf_path)
    pages = [page_text(p) for p in reader.pages]
    # The TOC is dense with dot leaders; the body starts at the first page that
    # has none. Locating it this way survives the TOC growing in a future rev.
    start = next(
        (i for i, t in enumerate(pages) if "...." not in t and L_HTTP in t or
         (i > 2 and "...." not in t and "FINA Web API" in t)),
        7,
    )
    return "\n".join(pages[start:]), len(reader.pages)


def extract_json_block(text, start_idx, limit=None):
    """Return the balanced JSON block starting at or after start_idx.

    Handles both object and array bodies (a few methods POST a bare id array,
    e.g. getProductsArray takes [1, 2]). Bracket counting is safe because the
    examples contain no brackets inside string literals; a plain json.loads
    would fail on the PDF's trailing ellipses, so raw text is preserved as-is.

    `limit` caps how far ahead to look, so a method whose Response is prose
    ("same as getProducts") does not swallow the next method's JSON.
    """
    window = text[:limit] if limit is not None else text
    candidates = [i for i in (window.find("{", start_idx), window.find("[", start_idx))
                  if i != -1]
    if not candidates:
        return None, start_idx
    open_idx = min(candidates)
    pairs = {"{": "}", "[": "]"}
    opener = window[open_idx]
    closer = pairs[opener]
    depth = 0
    for i in range(open_idx, len(window)):
        if window[i] == opener:
            depth += 1
        elif window[i] == closer:
            depth -= 1
            if depth == 0:
                return window[open_idx:i + 1], i + 1
    return None, start_idx


def parse_enums(desc):
    """Pull `value - meaning` pairs out of a field description."""
    values = []
    for segment in re.findall(r"\(([^()]*)\)", desc):
        items = ENUM_ITEM_RE.findall("(" + segment)
        if len(items) >= 2:
            for value, meaning in items:
                values.append({"value": value, "meaning_ka": meaning.strip()})
    return values


# The PDF contains two identifiers typeset with a stray space after the
# underscore ("default_ cash"). Without repair the field-definition pattern
# fails and the field is silently absorbed into the previous description.
STRAY_SPACE_RE = re.compile(
    r"\b([A-Za-z][A-Za-z0-9_]*)_\s+([a-z][A-Za-z0-9_]*)(?=\s*\([A-Za-z])")


# A container is occasionally declared at the tail of another field's
# description instead of on its own line, e.g. "... quantity, consumeds -
# collection of goods consumed for this production, consisting of:". Left
# unsplit, every following field is attributed to the wrong parent.
INLINE_CONTAINER_RE = re.compile(
    r",\s*(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*[-–—]\s*(?P<desc>[^,:]*:)\s*$")


def parse_where(block):
    """Parse a 'sadac:' block into ordered field records.

    Descriptions wrap across several lines, so a line that does not start a new
    field is appended to the previous one. Collection headers (e.g. "products -
    collection consisting of:") become parent markers so phase 2 can nest them.
    """
    fields = []
    current_parent = None
    block = STRAY_SPACE_RE.sub(r"\1_\2", block)
    for raw in block.split("\n"):
        line = raw.strip()
        if not line:
            continue
        m = FIELD_RE.match(line)
        if m and m.group("type").strip().lower() in TYPES:
            fields.append({
                "name": m.group("name"),
                "type": m.group("type").strip().lower(),
                "max_length": int(m.group("len")) if m.group("len") else None,
                "is_array": m.group("len") == "",
                "nullable": bool(m.group("nullable")),
                "parent": current_parent,
                "description_ka": m.group("desc").strip(),
                "enum_values": [],
            })
            continue
        c = COLLECTION_RE.match(line)
        if c:
            current_parent = c.group("name")
            fields.append({
                "name": c.group("name"),
                "type": "collection",
                "max_length": None,
                "is_array": False,
                "nullable": False,
                "parent": None,
                "description_ka": c.group("desc").strip(),
                "enum_values": [],
            })
            continue
        if fields:
            fields[-1]["description_ka"] += " " + line
    for f in fields:
        f["description_ka"] = clean(f["description_ka"]).rstrip(",.")
    fields = split_inline_containers(fields)
    for f in fields:
        f["enum_values"] = parse_enums(f["description_ka"])
    return fields


def split_inline_containers(fields):
    """Promote containers declared at the tail of another field's description.

    Descriptions are only complete once wrapped lines have been joined, so this
    runs afterwards. Everything that followed the swallowed declaration was
    attributed to the previous container, and is re-parented here.
    """
    out = []
    override = None
    for f in fields:
        if f["type"] == "collection" or f["type"] == "object":
            override = None
            out.append(f)
            continue
        if override:
            f["parent"] = override
        m = INLINE_CONTAINER_RE.search(f["description_ka"])
        out.append(f)
        if m:
            f["description_ka"] = f["description_ka"][:m.start()].strip().rstrip(",.")
            override = m.group("name")
            out.append({
                "name": m.group("name"),
                "type": "collection",
                "max_length": None,
                "is_array": False,
                "nullable": False,
                "parent": None,
                "description_ka": m.group("desc").strip(),
                "enum_values": [],
            })
    return out


TYPES = {
    "int", "string", "bool", "byte", "decimal", "datetime", "date", "long",
    "double", "float", "short", "guid", "object", "array", "time", "sbyte",
}


def label_value(block, label):
    """Read the value following a label, joining wrapped continuation lines."""
    idx = block.find(label)
    if idx == -1:
        return None
    rest = block[idx + len(label):]
    out = []
    for line in rest.split("\n"):
        stripped = line.strip()
        if out and (not stripped or any(
                stripped.startswith(l) for l in (L_DESC, L_HTTP, L_PATH, L_WHERE))):
            break
        if any(stripped.startswith(l) for l in (L_DESC, L_HTTP, L_PATH)) and out:
            break
        out.append(stripped)
        if label in (L_HTTP, L_PATH):
            break
    return re.sub(r"\s+", " ", " ".join(out)).strip()


def section_ranges(body):
    """Map body offsets to section names using the three top-level headings."""
    marks = []
    for label, key in SECTIONS.items():
        for m in re.finditer(re.escape(label), body):
            marks.append((m.start(), key))
    marks.sort()
    return marks


def section_at(marks, offset):
    current = "operation"
    for pos, key in marks:
        if pos <= offset:
            current = key
        else:
            break
    return current


def split_methods(body):
    """Split the body into one text block per method, keeping section context."""
    marker = re.compile(re.escape(L_FUNC))
    hits = [m.start() for m in marker.finditer(body)]
    blocks = []
    for i, start in enumerate(hits):
        end = hits[i + 1] if i + 1 < len(hits) else len(body)
        # Reach back far enough to pick up the heading line ("name - Georgian
        # title"), which sometimes wraps onto a second line.
        head_start = max(0, start - 400)
        blocks.append((body[head_start:start], body[start:end], start))
    return blocks


# "the returned collection is the same as that returned by the getX method"
SAME_AS_RE = re.compile(r"([A-Za-z][A-Za-z0-9_]*)\s*[-–—]?\s*მეთოდით")


def trim_bleed(text, next_name):
    """Cut a description that ran into the following method's heading."""
    cuts = [len(text)]
    if next_name:
        m = re.search(r"\b" + re.escape(next_name) + r"\b", text)
        if m:
            cuts.append(m.start())
    for label in SECTIONS:
        i = text.find(label)
        if i != -1:
            cuts.append(i)
    return text[:min(cuts)].strip().rstrip(",.").strip()


def apply_json_structure(fields, example):
    """Correct field nesting using the JSON example, and flag name mismatches.

    The sequential 'which collection are we inside' heuristic cannot tell when a
    collection ends, so top-level fields listed after a collection (notably the
    ubiquitous `ex` error field) get attached to it. The example shows the real
    shape, so prefer it where it parses.
    """
    if not example:
        return fields, []
    try:
        doc = json.loads(example)
    except Exception:
        return fields, []

    depth = {}
    seen = {}

    def walk(node, parent):
        if isinstance(node, dict):
            for k, v in node.items():
                seen[k] = seen.get(k, 0) + 1
                depth.setdefault(k, parent)
                walk(v, k if isinstance(v, (dict, list)) else parent)
        elif isinstance(node, list):
            for item in node:
                walk(item, parent)

    walk(doc, None)
    def kind_of(name):
        found = []

        def scan(node):
            if isinstance(node, dict):
                for k, v in node.items():
                    if k == name:
                        found.append("collection" if isinstance(v, list) else
                                     "object" if isinstance(v, dict) else "field")
                    scan(v)
            elif isinstance(node, list):
                for item in node:
                    scan(item)

        scan(doc)
        return found[0] if found else None

    for f in fields:
        if f["type"] == "collection":
            actual = kind_of(f["name"])
            if actual in ("collection", "object"):
                f["type"] = actual
        # Only trust the example where the name is unambiguous. Sibling
        # collections reuse names (`products` and `services` both carry id,
        # quantity, price), and there the sequential reading order is right and
        # a name lookup would be wrong. Containers are corrected too: the prose
        # often lists a nested collection such as `add_fields` at the top level
        # even though the example nests it inside its parent.
        if seen.get(f["name"]) == 1:
            f["parent"] = depth[f["name"]]
    # Names documented in prose but absent from the example (or vice versa) are
    # real inconsistencies in the source doc worth surfacing, not parse errors.
    documented = {f["name"] for f in fields}
    in_example = set(depth)
    mismatches = (
        [{"field": n, "kind": "undocumented"} for n in sorted(in_example - documented)]
        + [{"field": n, "kind": "absent_from_example"}
           for n in sorted(documented - in_example)])
    return fields, mismatches


def parse_method(heading, block, section, next_name=None):
    name = label_value(block, L_FUNC)
    if not name:
        return None
    name = name.split()[0]

    # The heading reads "<name> - <Georgian title>" and may wrap onto the next
    # line, so collapse whitespace first and stop at the next label.
    flat = re.sub(r"\s+", " ", heading)
    title_ka = ""
    for m in re.finditer(re.escape(name) + r"\s*[-–—]\s*(.+?)(?=$)", flat):
        title_ka = m.group(1).strip()
    title_ka = re.split(re.escape(L_FUNC), title_ka)[0].strip()

    http = (label_value(block, L_HTTP) or "").split()[0].upper()
    # One endpoint is typeset with a stray space after the base path
    # ("api/operation/ getLoyaltyBonusHistory/{qr_code}"). Splitting on
    # whitespace would silently truncate it to "api/operation/", so strip all
    # whitespace instead: a URL path never legitimately contains any.
    path = re.sub(r"\s+", "", label_value(block, L_PATH) or "")

    record = {
        "name": name,
        "title_ka": title_ka,
        "description_ka": label_value(block, L_DESC) or "",
        "http_method": http,
        "path": path,
        "section": section,
        "path_params": [],
        "request_body": None,
        "request_fields": [],
        "response": None,
        "response_fields": [],
        # Ten methods document their response by reference rather than by
        # example ("identical to getProducts"). Recording the target keeps the
        # generated docs honest instead of inventing a schema.
        "request_body_valid_json": None,
        "response_valid_json": None,
        "response_same_as": None,
        "notes_ka": [],
        "doc_inconsistencies": [],
    }

    req_idx = block.find("Request Body:")
    resp_idx = block.find("Response:")

    # A 'sadac:' block sitting before any JSON describes the URL path params.
    first_json = min(i for i in (req_idx, resp_idx, len(block)) if i != -1)
    pre = block[:first_json]
    where_idx = pre.find(L_WHERE)
    if where_idx != -1:
        record["path_params"] = parse_where(pre[where_idx + len(L_WHERE):])

    if req_idx != -1:
        body_json, after = extract_json_block(
            block, req_idx, limit=resp_idx if resp_idx > req_idx else None)
        body_json, valid = normalise_json(body_json)
        record["request_body"] = body_json
        record["request_body_valid_json"] = valid
        tail_end = resp_idx if resp_idx > after else len(block)
        w = block.find(L_WHERE, after, tail_end)
        if w != -1:
            record["request_fields"] = parse_where(block[w + len(L_WHERE):tail_end])

    if resp_idx != -1:
        resp_json, after = extract_json_block(block, resp_idx)
        resp_json, valid = normalise_json(resp_json)
        if resp_json:
            record["response"] = resp_json
            record["response_valid_json"] = valid
            w = block.find(L_WHERE, after)
            if w != -1:
                record["response_fields"] = parse_where(block[w + len(L_WHERE):])
        else:
            # Prose response: capture it verbatim and resolve the reference.
            prose = re.sub(r"\s+", " ", block[resp_idx + len("Response:"):]).strip()
            record["notes_ka"].append(prose)
            m = SAME_AS_RE.search(prose)
            if m:
                record["response_same_as"] = m.group(1)

    # A 'sadac:' block that yielded no typed fields still carries meaning (e.g.
    # "int[] - collection of product Ids"); keep it as a note.
    if req_idx != -1 and not record["request_fields"]:
        tail_end = resp_idx if resp_idx > req_idx else len(block)
        w = block.find(L_WHERE, req_idx, tail_end)
        if w != -1:
            note = re.sub(r"\s+", " ", block[w + len(L_WHERE):tail_end]).strip()
            if note:
                record["notes_ka"].append(note)

    for bucket, example in (("request_fields", record["request_body"]),
                            ("response_fields", record["response"])):
        if record[bucket]:
            record[bucket][-1]["description_ka"] = trim_bleed(
                record[bucket][-1]["description_ka"], next_name)
            record[bucket][-1]["enum_values"] = parse_enums(
                record[bucket][-1]["description_ka"])
            record[bucket], bad = apply_json_structure(record[bucket], example)
            record["doc_inconsistencies"] += [dict(b, bucket=bucket) for b in bad]
    if record["notes_ka"]:
        record["notes_ka"] = [trim_bleed(clean(n), next_name)
                              for n in record["notes_ka"]]
    # Descriptions often point at the lookup method that supplies an Id
    # ("discount (int) - discount Id (see method getDiscountTypes)"). Surfacing
    # these turns the generated docs into a navigable graph.
    blob = " ".join(
        f["description_ka"]
        for bucket in ("request_fields", "response_fields", "path_params")
        for f in record[bucket])
    record["see_also"] = sorted({
        m.group(1) for m in re.finditer(r"\b(get[A-Z][A-Za-z0-9_]*)\b", blob)
        if m.group(1) != name})
    record["title_ka"] = clean(record["title_ka"])
    record["description_ka"] = clean(record["description_ka"])
    return record


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("-o", "--out", default="assets/methods.json")
    args = ap.parse_args()

    body, page_count = load_body(args.pdf)

    marks = section_ranges(body)
    blocks = split_methods(body)
    names = [label_value(b, L_FUNC).split()[0] if label_value(b, L_FUNC) else None
             for _, b, _ in blocks]
    methods = []
    for i, (heading, block, offset) in enumerate(blocks):
        nxt = names[i + 1] if i + 1 < len(names) else None
        rec = parse_method(heading, block, section_at(marks, offset), nxt)
        if rec:
            methods.append(rec)

    out = {
        "source": args.pdf,
        "page_count": page_count,
        "method_count": len(methods),
        "methods": methods,
    }
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
    print(f"extracted {len(methods)} methods -> {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
