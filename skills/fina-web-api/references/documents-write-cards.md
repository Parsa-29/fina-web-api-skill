# Writing documents — issuing cards and points

4 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`saveDocDiscountCard`](#savedocdiscountcard) | POST | `api/operation/saveDocDiscountCard` | Issue a discount card |
| [`saveDocBonusCard`](#savedocbonuscard) | POST | `api/operation/saveDocBonusCard` | Issue an accrual (bonus) card |
| [`saveDocGiftCard`](#savedocgiftcard) | POST | `api/operation/saveDocGiftCard` | Issue a gift card |
| [`saveDocBonusOperation`](#savedocbonusoperation) | POST | `api/operation/saveDocBonusOperation` | Accrue/spend points |

---

### saveDocDiscountCard

Issue a discount card · *ფასდაკლების ბარათის გაცემა*

Save a discount card issued to a customer (insert, update) · *მყიდველზე გაცემული ფასდაკლების ბარათის შენახვა (insert, update)*

**POST** `api/operation/saveDocDiscountCard`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2019-11-08T18:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "ფასდაკლების ბარათის გაცემა", 
    "customer": 31, 
    "store": 1, 
    "user": 1, 
    "card_code": "231", 
    "discount_id": 1, 
    "status": true 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Operation Id. (pass 0 to create a new one) · *ოპერაციის Id. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `num` | long | Document number · *დოკუმენტის ნომერი* |
| `purpose` | string[750] | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `customer` | int | Customer Id · *მყიდველის Id* |
| `store` | int | Store (warehouse) Id · *საწყობის Id* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `code` | string | Discount card code · *ფასდაკლების ბარათის კოდი* |
| `discount` | int | Discount Id (see method getDiscountTypes) · *ფასდაკლების Id (იხ მეთოდი getDiscountTypes)* |
| `status` | bool | Card status (whether it is active) · *ბარათის სტატუსი (აქტიურია თუ არა)* |

**Response**

```json
{ 
    "id": 2, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the inserted (or updated) operation · *დამატებული (ან დარედაქტირებული) ოპერაციის Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `card_code`, `discount_id` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `code`, `discount` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

See also: `getDiscountTypes`

---

### saveDocBonusCard

Issue an accrual (bonus) card · *დაგროვების (ბონუს) ბარათის გაცემა*

Save an accrual (bonus) card issued to a customer (insert, update) · *მყიდველზე გაცემული დაგროვების (ბონუს) ბარათის შენახვა (insert, update)*

**POST** `api/operation/saveDocBonusCard`

**Request body**

```json
{ 
  "id": 0, 
  "date": "2019-11-08T18:00:00", 
  "num_pfx": "", 
  "num": 0, 
  "purpose": "დაგროვების ბარათის გაცემა", 
  "customer": 31, 
  "store": 1, 
  "user": 1, 
  "card_code": "231", 
  "person_code": "0100010101", 
  "person_name": "სახელი, გვარი", 
  "person_address": "მისამართი", 
  "person_tel": "+995597222222", 
  "status": true 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Operation Id. (pass 0 to create a new one) · *ოპერაციის Id. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `num` | long | Document number · *დოკუმენტის ნომერი* |
| `purpose` | string[750] | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `customer` | int | Customer Id · *მყიდველის Id* |
| `store` | int | Store (warehouse) Id · *საწყობის Id* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `card_code` | string | Accrual card code · *დაგროვების ბარათის კოდი* |
| `person_code` | string | Holder's personal number · *მფლობელის პირადი ნომერი* |
| `person_name` | string | Holder's first and last name · *მფლობელის სახელი, გვარი* |
| `person_address` | string | Holder's address · *მფლობელის მისამართი* |
| `person_tel` | string | Holder's phone number · *მფლობელის ტელეფონის ნომერი* |
| `status` | bool | Card status (whether it is active) · *ბარათის სტატუსი (აქტიურია თუ არა)* |

**Response**

```json
{ 
    "id": 3, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the inserted (or updated) operation · *დამატებული (ან დარედაქტირებული) ოპერაციის Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### saveDocGiftCard

Issue a gift card · *სასაჩუქრე ბარათის გაცემა*

Save an issued gift card (insert) · *გაცემული სასაჩუქრე ბარათის შენახვა (insert)*

**POST** `api/operation/saveDocGiftCard`

**Request body**

```json
{ 
    "date": "2019-11-11T18:00:00", 
    "amount": 100, 
    "pay_amount": 100, 
    "code": "TT3359", 
    "store": 1, 
    "user": 1 
}
```

| Field | Type | Description |
|---|---|---|
| `date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `amount` | decimal | Gift card value · *სასაჩუქრე ბარათის ღირებულება* |
| `pay_amount` | decimal | Amount actually paid · *რეალურად გადახდილი თანხის ოდენობა* |
| `code` | string | Card code · *ბარათის კოდი* |
| `store` | int | Store (shop) Id · *საწყობის (მაღაზიის) Id* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |

**Response**

```json
{ 
    "id": 2, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the added gift card · *დამატებული სასაჩუქრე ბარათის Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### saveDocBonusOperation

Accrue/spend points · *ქულის დაგროვება/გახარჯვა*

Save an accrual or spending of points (insert, update) · *ქულის დაგროვების ან გახარჯვის შენახვა (insert, update)*

**POST** `api/operation/saveDocBonusOperation`

**Request body**

```json
{ 
    "card_id": 2013, 
    "ref_id": 16975, 
    "coeff": 1, 
    "amount": 10.0 
}
```

| Field | Type | Description |
|---|---|---|
| `card_id` | int | Accrual card Id · *დაგროვების ბარათის Id* |
| `ref_id` | int | Id of the operation on which the corresponding accrual or spending of points is based · *ოპერაციის Id, რომლის საფუძველზეც ხდება შესაბამისი ქულის დაგროვება ან გახარჯვა* |
| `coeff` | sbyte | Coefficient 1 or -1 (depending on whether it is an accrual or a spending) · *კოეფიციენტი 1 ან -1 (იმისდა მიხედვით დაგროვება ხდება თუ გახარჯვა)* |
| `amount` | decimal | Amount of points accrued (spent) (calculated in money) · *დაგროვილი (გახარჯული) ქულის ოდენობა (გამოთვლილი თანხაში)* |

**Response**

```json
{ 
    "res": true, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `res` | bool | Result of the operation · *ოპერაციის შესრულების შედეგი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---
