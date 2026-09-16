# FINA WEB API skill

An agent skill giving Claude Code (and other agents) a complete, verified reference
for the **FINA WEB API 10.0** — the HTTP API of [FINA](https://fina.ge), a Georgian
ERP / accounting / warehouse / POS system.

The official documentation is a 249-page PDF written in Georgian. This skill turns it
into something an agent can actually use: all **150 endpoints**, **1,903 typed fields**,
every JSON example, and every coded value — in English, with the Georgian original kept
alongside so any translation can be checked against the source.

```bash
npx skills add https://github.com/Parsa-29/fina-web-api-skill --skill fina-web-api
```

Add `--global` to install it for every project.

## Why this exists

Writing a FINA integration without the reference in front of you means guessing endpoint
names, and a guess that looks plausible fails at runtime. Worse, several of FINA's
conventions are easy to get wrong in ways that produce code which *appears* to work:

- **A `200 OK` can still be a failure.** Every response carries an `ex` field; if it is
  non-null the call failed, whatever the HTTP status says.
- **`id: 0` creates, any other id overwrites.** Save methods are upserts. There is no
  separate create endpoint, no dry run and no delete API.
- **Dates carry no timezone.** They are `yyyy-MM-ddTHH:mm:ss`, read as the server's local
  time. A client serialising UTC posts documents at the wrong time.
- **Coded values are bare integers that mean different things per field.** `pay_type 1`
  is cashless; `t_payer 1` is the buyer. A wrong number files a valid-looking document
  with the wrong meaning — including waybills sent to the Georgian Revenue Service.

## What's inside

```
skills/fina-web-api/
├── SKILL.md              routing + the conventions that break integrations
├── references/           18 files, ~9,600 lines
│   ├── index.md          all 150 methods, grouped, with links
│   ├── conventions.md    auth, `ex`, dates, ids, custom fields, incremental sync
│   ├── enums.md          every coded value, with which methods use it
│   ├── changelog.md      36 releases + "which version introduced this method?"
│   └── …                 14 domain files with full request/response schemas
├── scripts/
│   ├── fina_client.py    dependency-free client: token cache, `ex` check, 401 retry
│   ├── fina_client.ts    the same for Node 18+ / any fetch runtime
│   └── *.py              the generators, so the skill can be rebuilt for a new revision
└── assets/               methods.json, the Georgian→English glossary, grouping config
```

Reference files load one at a time, so a task about stock never pays for the loyalty docs.

## The part you can't get from the PDF

The reference was built by parsing the documentation and cross-checking its prose against
its own JSON examples. **They disagree in 34 methods.** Where they do, the example wins —
it reflects what the server actually returns — and the affected method carries a warning
naming the fields. Some that will cost you an afternoon otherwise:

| Method | The problem |
|---|---|
| `getCustomers`, `getVendors` (+2) | Examples return `phone` / `email`; the prose calls them `tel` / `mail` |
| All 12 reporting journals | Prose documents `journal`; every example returns `journals` |
| `getUserPermissions` | Returns `stores`, `cashes`, `users`, `price_types`, `default_cash`, `default_price` — none of them documented |
| `getInventories` | Returns `in_date`, undocumented |
| `getTransportationMeans` | Returns `driver_num`, undocumented |

Two endpoints are also typeset with a stray space in the PDF (`api/operation/ getLoyalty…`),
which silently truncates the path if you parse it naively. Both are corrected here.

## Verification

Extraction is checked by [`verify_extraction.py`](skills/fina-web-api/scripts/verify_extraction.py),
which asserts that every method in the table of contents is present, every endpoint appears
in the source, every `{placeholder}` is documented, every POST has a request body, no JSON
example is unbalanced, and no field description has bled into the next method.

The skill was also benchmarked against three realistic integration tasks, run with and
without it. With the skill: **22/22** objective checks. Without: **2/22** — the baseline
produced confident, well-structured code calling endpoints that do not exist.

> The reference is verified against the *documentation*, not against a live server. Where
> the documentation is wrong in ways its own examples don't reveal, only a real FINA
> instance will tell you.

## Rebuilding for a newer API revision

The reference files are generated. Point the scripts at the new PDF rather than editing
markdown by hand:

```bash
cd skills/fina-web-api
python3 scripts/extract_methods.py "FINA WEB API 11.0.pdf" -o assets/methods.json
python3 scripts/verify_extraction.py "FINA WEB API 11.0.pdf" assets/methods.json
python3 scripts/build_glossary.py        # only new Georgian strings need translating
python3 scripts/render_references.py
python3 scripts/render_overview.py
python3 scripts/extract_changelog.py "FINA WEB API 11.0.pdf"
```

`build_glossary.py` keeps existing translations, so a new revision only surfaces genuinely
new strings. Requires `pypdf`.

## Attribution and scope

This is an **unofficial, community-maintained** skill. It is not affiliated with,
endorsed by, or supported by შპს FINA.

The API descriptions, field names, JSON examples and coded values are derived from *FINA
WEB API 10.0 — დოკუმენტაცია*, © შპს FINA. That material remains theirs; it is reproduced
here in translated and restructured form to make the API usable from a coding agent. The
source PDF itself is **not** redistributed — obtain it from FINA. If FINA would like
anything changed or removed, please open an issue.

The tooling (the extraction, rendering and client scripts) is MIT licensed — see
[LICENSE](LICENSE).

Translations are mechanical and human-reviewable: every Georgian string is kept next to
its English rendering, and the full mapping lives in
[`glossary.ka-en.json`](skills/fina-web-api/assets/glossary.ka-en.json). Corrections are
welcome.
