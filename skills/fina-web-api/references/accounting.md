# Bookkeeping accounts and entries

3 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getAccountValue`](#getaccountvalue) | POST | `api/operation/getAccountValue` | Accounting account value |
| [`getAccountValueDetails`](#getaccountvaluedetails) | POST | `api/operation/getAccountValueDetails` | Itemised accounting account values |
| [`getEntriesJournal`](#getentriesjournal) | GET | `api/reporting/getEntriesJournal/{date_from}/{date_to}` | Journal of accounting entries |

---

### getAccountValue

Accounting account value · *ბუღალტრული ანგარიშის მნიშვნელობა*

Fetch the total turnover value (debit, credit) of an accounting account · *ბუღალტრული ანგარიშის ბრუნვის ჯამური მნიშვნელობის (დებეტ, კრედიტი) წამოღება*

**POST** `api/operation/getAccountValue`

**Request body**

```json
{ 
    "primary_acc": "1410", 
    "secondary_acc": "", 
    "date": "2019-09-12T13:00:00", 
    "obj": 6, 
    "is_gel": true 
}
```

| Field | Type | Description |
|---|---|---|
| `primary_acc` | string | Account code · *ანგარიშის კოდი* |
| `secondary_acc` | string | Account code (advance) · *ანგარიშის კოდი (საავანსო)* |
| `date` | datetime | Date · *თარიღი* |
| `obj` | int | Id of the specific object whose account is passed in primary_acc or secondary_acc (e.g. for 1410, obj will be the Id of the specific customer) · *იმ კონკრეტული ობიექტის Id, ვისი ანგარიშიცაა გადაცემული primary_acc ან secondary_acc - ში (მაგ: 1410 ის შემთხვევაში obj - იქნება კონრკეტული მყიდველის Id)* |
| `is_gel` | bool | Show the result in GEL equivalent · *შედეგი აჩვენოს ლარის ექვივალენტით* |

**Response**

```json
{ 
    "values": { 
        "debit_val": 1320.00, 
        "credit_val": 0.00 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `values.debit_val` | decimal | Debit value · *დებეტ მნიშვნელობა* |
| `values.credit_val` | decimal | Credit value · *კრედიტ მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `values` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---

### getAccountValueDetails

Itemised accounting account values · *ბუღალტრული ანგარიშის ჩაშლილი მნიშვნელობები*

Fetch the itemised total turnover value (debit, credit) of an accounting account · *ჩაშლილი ბუღალტრული ანგარიშის ბრუნვის ჯამური მნიშვნელობის (დებეტ, კრედიტი) წამოღება*

**POST** `api/operation/getAccountValueDetails`

**Request body**

```json
{ 
    "account": "1410", 
    "date": "2023-11-28T13:00:00", 
    "currency": "USD" 
}
```

| Field | Type | Description |
|---|---|---|
| `account` | string | Account code · *ანგარიშის კოდი* |
| `date` | datetime | Date · *თარიღი* |
| `currency` | string | Currency (if not passed, the result is returned in GEL equivalent) · *ვალუტა (არ გადაცემის შემთხვევაში შედეგი დაბრუნდება ლარის ექვივალენტით)* |

**Response**

```json
{ 
    "values": [{ 
        "id": 2, 
        "debit_val": 1320.00, 
        "credit_val": 0.00 
    },{ 
        "id": 9, 
        "debit_val": 0.00, 
        "credit_val": 150.00 
    }] 
    "ex": null 
}
```

> [!NOTE]
> The response example above is not valid JSON as printed in the source documentation (it contains a typo such as a stray or missing comma). The field list below is authoritative.

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the specific object whose account is passed (e.g. for 1410 this will be the customers' id) · *იმ კონკრეტული ობიექტის id, ვისი ანგარიშიცაა გადაცემული (მაგ: 1410 შემთხვევაში ეს იქნება მყიდველების id)* |
| `debit_val` | decimal | Debit value · *დებეტ მნიშვნელობა* |
| `credit_val` | decimal | Credit value · *კრედიტ მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getEntriesJournal

Journal of accounting entries · *ბუღალტრული გატარებების ჟურნალი*

Journal of accounting entries · *ბუღალტრული გატარებების ჟურნალი*

**GET** `api/reporting/getEntriesJournal/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "journals": [{ 
        "id": 3121, 
        "version": "AAAAAAABf5A=", 
        "date": "2018-10-19 16:03:21", 
        "doc_num": "5", 
        "waybill_num": null, 
        "doc_type": 49, 
        "purpose": "ავანსის მიღება მყიდველისგან - რონალდ რეიგანი", 
        "amount": 12.00, 
        "amount_currency": 24,  
        "currency": "USD", 
        "staff_id": 1, 
        "debit_acc": "1110.1", 
        "debit_comment": "მთავარი სალარო", 
        "debit_quantity": 0, 
        "credit_acc": "3120.8", 
        "credit_comment": "რონალდ რეიგანი", 
        "credit_quantity": 0, 
        "project_id": 2 
    }, { 
        "id": 3121, 
        "version": "AAAAAAABf5A=", 
        "date": "2018-10-19 16:03:21", 
        "doc_num": "5", 
        "waybill_num": null, 
        "doc_type": 38, 
        "purpose": "ავანსის მიღება მყიდველისგან - რონალდ რეიგანი", 
        "amount": 1.83, 
        "amount_currency": 1.83,  
        "currency": "GEL", 
        "staff_id": 1, 
        "debit_acc": "3339", 
        "debit_comment": "გადასახდელი დღგ-ს ტრანზიტული ანგარიში", 
        "debit_quantity": 0, 
        "credit_acc": "3330", 
        "credit_comment": "გადასახდელი დღგ", 
        "credit_quantity": 0, 
        "project_id": 1 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `journal[]` | collection | Collection of the accounting entries journal consisting of: · *ბუღალტრული გატარებების ჟურნალის კოლექციაა რომელიც შედგება:* |
| `journal[].id` | int | Operation id · *ოპერაციის id* |
| `journal[].version` | string | Record version in the database (base64 of byte[]) · *ჩანაწერის ვერსია ბაზაში (base64 of byte[])* |
| `journal[].date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `journal[].doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `journal[].waybill_num` | string | Waybill number (RS - Revenue Service) · *ზედნადების ნომერი (RS)* |
| `journal[].doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `journal[].purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `journal[].amount` | decimal | Operation amount (equivalent in national currency) · *ოპერაციის თანხა (ექვივალენტი ეროვნულ ვალუტაში)* |
| `journal[].amount_currency` | decimal | Operation amount in the currency · *ოპერაციის თანხა ვალუტაში* |
| `journal[].currency` | string | Currency · *ვალუტა* |
| `journal[].staff_id` | int | Staff member id · *თანამშრომლის id* |
| `journal[].debit_acc` | string | Debit account · *დებეტ ანგარიში* |
| `journal[].debit_comment` | string | Description corresponding to the debit account · *დებეტ ანგარიშის შესაბამისი აღწერა* |
| `journal[].debit_quantity` | double | Quantity corresponding to the debit account · *დებეტ ანგარიშის შესაბამისი რაოდენობა* |
| `journal[].credit_acc` | string | Credit account · *კრედიტ ანგარიში* |
| `journal[].credit_comment` | string | Description corresponding to the credit account · *კრედიტ ანგარიშის შესაბამისი აღწერა* |
| `journal[].credit_quantity` | double | Quantity corresponding to the credit account · *კრედიტ ანგარიშის შესაბამისი რაოდენობა* |
| `journal[].project_id` | int | Project id · *პროექტის id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `journals` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `journal` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---
