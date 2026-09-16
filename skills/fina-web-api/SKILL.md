---
name: fina-web-api
description: >-
  Complete developer reference for the FINA WEB API 10.0 — the HTTP API of FINA,
  a Georgian ERP / accounting / warehouse / POS system. Covers all 150 endpoints
  across api/operation, api/reporting and api/authentication, with full request
  and response schemas, every field typed and translated from the Georgian
  source documentation, and every coded value tabulated. Use this skill whenever
  the user mentions FINA, ფინა, fina-api, or works with endpoints such as
  getProducts, getProductsRest, saveDocProductOut, saveCustomer, getRealizesJournal,
  or any api/operation or api/reporting path. Use it for syncing products, stock,
  prices, customers or vendors out of FINA; for posting sales, purchases,
  transfers, returns, money receipts, advances or RS waybills into FINA; for gift
  cards, bonus cards and loyalty programs; and for journals and reports. Use it
  even when the user never names the API but is clearly integrating with a
  Georgian ERP, accounting, warehouse or point-of-sale backend, or is debugging
  an integration that returns Georgian error text.
---

# FINA WEB API

FINA is a Georgian ERP system (accounting, warehouse, retail POS). Each customer
runs their own FINA server, so the base URL always comes from them — there is no
vendor-hosted endpoint to point at.

This skill is a complete port of the *FINA WEB API 10.0* documentation, which is
written in Georgian. Every endpoint, field, type and coded value is here in
English with the Georgian original alongside, so a Georgian-speaking colleague
can check any translation against the source.

## Start here

**Read [`references/index.md`](references/index.md) first** when you do not
already know which method you need. It lists all 150 methods with their verb,
endpoint and purpose, grouped by domain, and tells you which reference file to
open next.

This is worth the tokens. The API has clusters of near-identical methods whose
differences are exactly the sort of thing that produces code that looks correct
and syncs the wrong data — `getProductsRest` versus `getProductsRestByStore`
versus `getProductsRestAfter` versus `getProductsRestSummary`, for example. The
index makes the distinction visible before you commit to one.

Then open the one reference file you need. They are large because the schemas
are complete; you are not meant to read more than one.

| You are working on | Open |
|---|---|
| Anything — shared behaviour, auth, error handling | [`references/conventions.md`](references/conventions.md) |
| Customers, vendors, their groups, addresses, agreements, sub-accounts | [`references/contragents.md`](references/contragents.md) |
| Products, services, fixed assets, characteristics, sub-codes, images | [`references/catalog.md`](references/catalog.md) |
| Prices, price types, discounts, units | [`references/pricing.md`](references/pricing.md) |
| Stock balances, reserves, cost price | [`references/stock.md`](references/stock.md) |
| Stores, users, permissions, staff, banks, projects, terminals | [`references/directories.md`](references/directories.md) |
| Gift cards, bonus cards, loyalty (Cloud) programs | [`references/loyalty-and-cards.md`](references/loyalty-and-cards.md) |
| Bookkeeping account values and entries | [`references/accounting.md`](references/accounting.md) |
| Reading sales, orders, returns | [`references/documents-read-trade.md`](references/documents-read-trade.md) |
| Reading transfers, services, production | [`references/documents-read-ops.md`](references/documents-read-ops.md) |
| Posting sales, purchases, transfers, orders | [`references/documents-write-trade.md`](references/documents-write-trade.md) |
| Posting money, advances, card payments | [`references/documents-write-money.md`](references/documents-write-money.md) |
| Issuing discount, bonus and gift cards | [`references/documents-write-cards.md`](references/documents-write-cards.md) |
| Posting production and disassembly | [`references/documents-write-production.md`](references/documents-write-production.md) |
| Journals and reports | [`references/reporting.md`](references/reporting.md) |
| Any coded value (`pay_type`, `vat_type`, `w_type`, …) | [`references/enums.md`](references/enums.md) |
| Whether a method exists on the customer's server version | [`references/changelog.md`](references/changelog.md) |

The reference files are large. To pull a single method without reading a whole
file:

```bash
sed -n '/^### saveDocProductOut$/,/^---$/p' references/documents-write-trade.md
```

## The four things that break FINA integrations

Everything else is in `conventions.md`. These four cause most of the damage, so
they are worth knowing before you write a line of code.

### 1. A 200 OK can still be a failure

Every response carries an `ex` field. **If `ex` is non-null, the call failed**,
regardless of the HTTP status. A client that only checks `response.ok` will
silently treat errors as successes and, on write methods, report documents as
posted that were not.

```python
data = response.json()
if data.get("ex"):
    raise FinaError(data["ex"])
```

### 2. `id: 0` creates, any other id overwrites

Save methods are upserts. There is no separate create endpoint, no dry run, and
no delete API. `saveCustomer` with an id that already exists overwrites that
customer, and `saveDocProductOut` with an existing document id rewrites a posted
document. When creating, pass `0` explicitly rather than omitting the field.

### 3. Dates have no timezone

Dates are `yyyy-MM-ddTHH:mm:ss`, with no offset and no trailing `Z`. The server
reads them as its own local time. A client that serialises UTC by default will
post documents at the wrong time, and the error will look like a data-entry
mistake rather than a bug. Format dates explicitly.

### 4. The source documentation contradicts itself in 34 methods

This reference was generated by parsing the PDF and cross-checking its prose
against its own JSON examples. They disagree in 34 places — fields that appear
in an example but are never described, and fields described but absent from
every example.

**Where they disagree, the example wins**; it reflects what the server actually
returns. Each affected method carries a warning callout naming the fields. Two
you will hit early:

- `getCustomers`, `getCustomersByCode`, `getVendors`, `getVendorsByCode` return
  `phone` and `email`, though the field list calls them `tel` and `mail`.
- Every reporting journal returns `journals`, though the prose documents
  `journal`.

If a field you expect is missing at runtime, check the method's warning callout
before assuming your code is wrong.

## Writing code against FINA

Two ready-made clients are bundled — [`scripts/fina_client.py`](scripts/fina_client.py)
and [`scripts/fina_client.ts`](scripts/fina_client.ts). Both authenticate, cache
the 36-hour token, raise on a non-null `ex`, and re-authenticate once on a 401.
Use one as-is, or as the shape to follow when writing a client in another stack.

A FINA integration almost always has the same skeleton, because nearly every
reference in the API is a numeric FINA id rather than a code you already know:

1. **Resolve directories once.** Pull stores, price types, users, staff and
   projects, and cache the id mappings. Do this before anything else; without
   these ids you cannot construct a document.
2. **Map custom fields by meaning, not by name.** Installation-specific columns
   arrive as `usr_column_NNN` and the numbers differ per customer. Call the
   matching `get*AdditionalFields` method and map on the user-assigned `header`.
3. **Sync incrementally.** For recurring jobs prefer the `*After/{after_date}`
   variants (`getProductsAfter`, `getProductPricesAfter`,
   `getProductsRestAfter`, `getProductsRestByStoreAfter`) over full catalogue
   pulls.
4. **Check `ex` on every call, and record the returned document `id`** on
   writes. That id is the only handle you will have on what you created.

### Before posting a document

The `saveDoc*` methods write into a live accounting system. They move stock,
post ledger entries and, for waybills, feed filings to the Georgian Revenue
Service (RS.ge). Treat them the way you would treat a production database
write — because that is what they are.

- Confirm with the user before running a `saveDoc*` call against a real server.
- Check `make_entry`: it decides whether the accounting entry is posted at all,
  and getting it wrong yields stock movements with no ledger effect or the
  reverse.
- Look up `w_type`, `t_type` and `t_payer` in
  [`references/enums.md`](references/enums.md) rather than guessing. The same
  small integers mean different things in different fields, so a plausible-looking
  number produces a valid document with wrong semantics.

## Regenerating this skill

The reference files are generated, not hand-written. When FINA publishes a new
revision, point the scripts at the new PDF rather than editing the markdown:

```bash
python3 scripts/extract_methods.py "FINA WEB API 11.0.pdf" -o assets/methods.json
python3 scripts/verify_extraction.py "FINA WEB API 11.0.pdf" assets/methods.json
python3 scripts/build_glossary.py        # only new Georgian strings need translating
python3 scripts/render_references.py
python3 scripts/render_overview.py
python3 scripts/extract_changelog.py "FINA WEB API 11.0.pdf"
```

`build_glossary.py` preserves existing translations, so a new revision only
surfaces the strings that are genuinely new. `verify_extraction.py` fails loudly
if anything in the new PDF does not parse — run it before trusting the output.
