# Authentication and shared conventions

Behaviour that applies to every call. Read this before writing any FINA client;
most of it is stated once in the source documentation and then assumed
everywhere, which makes it easy to miss.

## Base URLs

A FINA server is reached at its own host and port — there is no central,
vendor-hosted endpoint, so the base URL always comes from the customer.

| Area | Base URL |
|---|---|
| Authentication | `http://[IP:PORT]/api/authentication` |
| Operations (master data and documents) | `http://[IP:PORT]/api/operation` |
| Reporting (journals and reports) | `http://[IP:PORT]/api/reporting` |
| Swagger UI | `http://[IP:PORT]/swagger` (added in 10.0.20260625) |

## Request headers

```
Content-Type:   application/json
Accept:         application/json
Authorization:  Bearer <access token>
tenant_key:     <your_tenant_key>
```

`tenant_key` is required only when working against a MultiTenant installation.
Sending it to a single-tenant server is harmless; omitting it on a MultiTenant
one is not.

## Authentication

`POST api/authentication/authenticate` with a login and password returns a JWT
that is **valid for 36 hours** (it was longer before release 3.1.20200921).

Cache the token and reuse it. Authenticating on every call is the most common
way to make a FINA integration slow, and it is avoidable. Re-authenticate when
a call returns 401, not on a timer — clock skew between your process and the
server makes expiry arithmetic unreliable.

## Errors: the `ex` field is the one that matters

Every response carries an `ex` field. **A 200 OK with a non-null `ex` is a
failure.** This is the single most important thing to get right in a FINA
client, because the HTTP status alone will tell you the call succeeded.

```python
data = response.json()
if data.get("ex"):
    raise FinaError(data["ex"])
```

HTTP statuses used: `200 OK`, `400 Bad Request`, `401 Unauthorized`,
`500 Internal Server Error`.

## Dates

Dates are passed and returned as `yyyy-MM-ddTHH:mm:ss` — no timezone offset and
no trailing `Z`. The server interprets them in its own local time, so a client
that serialises UTC will silently post documents at the wrong time. Format
dates explicitly rather than relying on a library's ISO default.

## Identifiers

Almost every reference is a numeric FINA `id`, not a human-readable code. A
product's `code`, a customer's identification number and a card's `code` are
data, not keys. The usual shape of an integration is therefore: pull the
directories once (stores, price types, users, staff, projects), cache the id
mappings, then refer to ids from then on.

Where a save method takes an `id`, **passing `0` creates a new record and
passing an existing id updates it.** There is no separate create and update
endpoint, and no confirmation step — `saveCustomer` with an id that exists will
overwrite that customer.

## Custom fields (`add_fields`)

FINA lets each installation add its own columns, which surface as
`usr_column_NNN`. The numbers differ per installation, so never hard-code them.
Call the matching `get*AdditionalFields` method to learn which column carries
which business meaning, and map by the user-assigned `header`, not the column
name.

## Incremental sync: the `*After` methods

Several catalogues have an `*After/{after_date}` variant — `getProductsAfter`,
`getProductPricesAfter`, `getProductsRestAfter`, `getProductsRestByStoreAfter`.
These return only what changed after the given timestamp and are the right tool
for a recurring sync; the plain method re-downloads the entire catalogue every
run.

Their responses are documented by reference ("identical to `getProducts`"),
which is why those pages have no example of their own.

## Batch fetches: the `*Array` methods

The `*Array` methods are POSTs that take a bare JSON array of ids, e.g.
`[1, 2, 3]`, rather than an object. The source documentation gives two limits
worth respecting: **at most ~2000 ids** for `getProductsArray` (beyond that it
recommends pulling the whole catalogue instead), and **at most 20** for
`getProductsImageArray`, since images are returned base64-encoded and responses
get large fast.

## Writing documents

The `saveDoc*` methods post real documents into a live accounting system. They
affect stock, ledgers and, for waybills, filings with the Georgian Revenue
Service. There is no dry-run mode and no API for deleting a document.

Two fields deserve particular care:

- `make_entry` controls whether the accounting entry is posted. Getting it
  wrong produces stock movements with no ledger effect, or vice versa.
- `w_type`, `t_type` and `t_payer` drive waybill and transportation data that
  goes to RS.ge. See [`enums.md`](enums.md) — the codes are not interchangeable
  between fields.

Always check `ex` after a write, and record the returned document `id`; it is
the only handle you will have on what you created.

## Known defects in the source documentation

The PDF this reference was generated from contradicts itself in 34 methods.
Where the JSON example and the field list disagree, **the example wins** — it
reflects what the server actually returns. Each affected method carries a
warning callout naming the specific fields. The most consequential:

- `getCustomers`, `getCustomersByCode`, `getVendors`, `getVendorsByCode` —
  examples return `phone` and `email`; the field list calls them `tel` and
  `mail`.
- Every reporting journal — the prose documents `journal`, every example
  returns `journals`.

---

### authenticate

Authorization · *ავტორიზაცია*

Authorization (token generation) · *ავტორიზაცია (თოქენის გენერაცია)*

**POST** `api/authentication/authenticate`

**Request body**

```json
{ 
    "login": "your login", 
    "password": "your password" 
}
```

| Field | Type | Description |
|---|---|---|
| `login` | string | Login for API access · *API -სთან დაშვების ლოგინი* |
| `password` | string | Password for API access · *API -სთან დაშვების პაროლი* |

**Response**

```json
{ 
    "token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9……..0kJov3akIA", 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `token` | string | The generated token (valid for 36 hours) · *წარმოადგენს დაგენერირებულ თოქენს (მოქმედია 36 საათის განმავლობაში)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |
