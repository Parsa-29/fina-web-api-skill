# Writing documents — money, advances and card payments

5 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`saveDocCustomerMoneyIn`](#savedoccustomermoneyin) | POST | `api/operation/saveDocCustomerMoneyIn` | Receipt of money |
| [`saveDocCustomerAdvanceIn`](#savedoccustomeradvancein) | POST | `api/operation/saveDocCustomerAdvanceIn` | Receipt of an advance |
| [`saveDocCustomerMoneyReturn`](#savedoccustomermoneyreturn) | POST | `api/operation/saveDocCustomerMoneyReturn` | Return of money |
| [`saveDocBonusPayment`](#savedocbonuspayment) | POST | `api/operation/saveDocBonusPayment` | Payment with points |
| [`saveDocGiftPayment`](#savedocgiftpayment) | POST | `api/operation/saveDocGiftPayment` | Redeem a gift card |

---

### saveDocCustomerMoneyIn

Receipt of money · *თანხის მიღება*

Save money received from a customer (insert, update) · *მყიდველისგან მიღებული თანხის შენახვა (insert, update)*

**POST** `api/operation/saveDocCustomerMoneyIn`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2019-03-09T13:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "თანხის მიღება - მყიდველი", 
    "amount": 65.7, 
    "currency": "GEL", 
    "rate": 1, 
    "store": 1, 
    "user": 1, 
    "staff": 3, 
    "project": 2, 
    "customer": 8, 
    "pay_type": 3, 
    "pay_type_id": 1, 
    "ref_id": 0, 
    "make_entry": true, 
    "add_fields": [{ 
        "field": "usr_column_529", 
        "value": "10 ქაღალდი2" 
    }] 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Operation Id. (pass 0 to create a new one) · *ოპერაციის Id. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `num` | long | Document number · *დოკუმენტის ნომერი* |
| `purpose` | string[750] | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `currency` | string | Currency code · *ვალუტის კოდი* |
| `rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `store` | int | Store (warehouse) Id · *საწყობის Id* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `staff` | int | Staff member Id (0 = take the staff member linked to the user) · *თანამშრომლის Id (0 = მომხმარებელზე მიბმული თანამშრომლის აღება)* |
| `project` | int | Project Id · *პროექტის Id* |
| `customer` | int | Customer Id · *მყიდველის Id* |
| `pay_type` | byte | Payment method (1 - cash, 2 - POS terminal, 3 - bank transfer, 4 - installment bank) · *გადახდის სახეობა (1 - ნაღდი, 2 - ტერმინალი, 3 - საბანკო გადარიცხვა, 4 - განვადების ბანკი) * |
| `pay_type_id` | int | Id of the cash register, POS terminal, bank account or installment bank in the FINA database (depending on which pay_type is selected) · *სალაროს, ტერმინალის, საბანკო ანგარიშის ან განვადების ბანკის Id არსებული FINA -ს ბაზაში (იმისდა მიხედვით რა არის არჩეული pay_type)* |
| `ref_id` | int | Id of an operation in FINA that this money receipt is based on · *FINA ში არსებული ოპერაციის Id, რომლის საფუძველიცაა მოცემული თანხის მიღება* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |
| `add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |

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

### saveDocCustomerAdvanceIn

Receipt of an advance · *ავანსის მიღება*

Save an advance received from a customer (insert, update) · *მყიდველისგან მიღებული ავანსის შენახვა (insert, update)*

**POST** `api/operation/saveDocCustomerAdvanceIn`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2019-03-30T11:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "ავანსის მიღება - მყიდველი", 
    "amount": 65.7, 
    "currency": "GEL", 
    "rate": 1, 
    "user": 1, 
    "staff": 3, 
    "project": 2, 
    "customer": 8, 
    "pay_type": 3, 
    "pay_type_id": 1, 
    "overlap_type": 0, 
    "overlap_amount": 0, 
    "ref_id": 0, 
    "make_entry": true, 
    "add_fields": [{ 
        "field": "usr_column_531", 
        "value": "10 საათი" 
    }] 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Operation Id. (pass 0 to create a new one) · *ოპერაციის Id. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `num` | long | Document number · *დოკუმენტის ნომერი* |
| `purpose` | string[750] | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `currency` | string | Currency code · *ვალუტის კოდი* |
| `rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `staff` | int | Staff member Id (0 = take the staff member linked to the user) · *თანამშრომლის Id (0 = მომხმარებელზე მიბმული თანამშრომლის აღება)* |
| `project` | int | Project Id · *პროექტის Id* |
| `customer` | int | Customer Id · *მყიდველის Id* |
| `pay_type` | byte | Payment method (1 - cash, 2 - POS terminal, 3 - bank transfer, 4 - installment bank) · *გადახდის სახეობა (1 - ნაღდი, 2 - ტერმინალი, 3 - საბანკო გადარიცხვა, 4 - განვადების ბანკი) * |
| `pay_type_id` | int | Id of the cash register, POS terminal, bank account or installment bank in the FINA database (depending on which pay_type is selected) · *სალაროს, ტერმინალის, საბანკო ანგარიშის ან განვადების ბანკის Id არსებული FINA -ს ბაზაში (იმისდა მიხედვით რა არის არჩეული pay_type)* |
| `overlap_type` | byte | Separating VAT on the advance (0 - do not separate, 1 - partially, 2 - fully) · *ავანსის დღგ-ს გამოყოფა (0 - არ გამოეყოს, 1 - ნაწილობრივ, 2 - სრულად) * |
| `overlap_amount` | decimal | Separated VAT amount (if overlap_type is 2 the amount is calculated automatically; if overlap_type is 1, the separated VAT amount must not exceed the VAT amount calculated from the amount passed in the total operation value (amount)) · *გამოყოფოლი დღგ- ს თანხა (თუ overlap_type არის 2, მოხდება თანხის ავტომატური დაანგარიშება, თუ overlap_type არის 1 - გამოყოფოლი დღგ -ს თანხა არ უნდა აღემატებოდეს ოპერაციის ჯამურ ღირებულებაში (amount) გადმოცემული თანხიდან გამოთვლილ დღგ-ს თანხას )* |
| `ref_id` | int | Id of an operation in FINA that this money receipt is based on · *FINA ში არსებული ოპერაციის Id, რომლის საფუძველიცაა მოცემული თანხის მიღება* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |
| `add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |

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

### saveDocCustomerMoneyReturn

Return of money · *თანხის დაბრუნება*

Save money returned to a customer (insert, update) · *მყიდველთან დაბრუნებული თანხის შენახვა (insert, update)*

**POST** `api/operation/saveDocCustomerMoneyReturn`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2019-03-09T13:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "თანხის დაბრუნება - მყიდველი", 
    "amount": 65.7, 
    "currency": "GEL", 
    "rate": 1, 
    "store": 1, 
    "user": 1, 
    "staff": 3, 
    "project": 2, 
    "customer": 8, 
    "pay_type": 1, 
    "pay_type_id": 1, 
    "ref_id": 0, 
    "make_entry": true, 
    "add_fields": [{ 
        "field": "usr_column_530", 
        "value": "10 ქაღალდი2" 
    }] 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Operation Id. (pass 0 to create a new one) · *ოპერაციის Id. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `num` | long | Document number · *დოკუმენტის ნომერი* |
| `purpose` | string[750] | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `currency` | string | Currency code · *ვალუტის კოდი* |
| `rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `store` | int | Store (warehouse) Id · *საწყობის Id* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `staff` | int | Staff member Id (0 = take the staff member linked to the user) · *თანამშრომლის Id (0 = მომხმარებელზე მიბმული თანამშრომლის აღება)* |
| `project` | int | Project Id · *პროექტის Id* |
| `customer` | int | Customer Id · *მყიდველის Id* |
| `pay_type` | byte | Return method (1 - cash, 2 - POS terminal, 3 - bank transfer, 4 - installment bank) · *დაბრუნების სახეობა (1 - ნაღდი, 2 - ტერმინალი, 3 - საბანკო გადარიცხვა, 4 - განვადების ბანკი) * |
| `pay_type_id` | int | Id of the cash register, POS terminal, bank account or installment bank in the FINA database (depending on which pay_type is selected) · *სალაროს, ტერმინალის, საბანკო ანგარიშის ან განვადების ბანკის Id არსებული FINA -ს ბაზაში (იმისდა მიხედვით რა არის არჩეული pay_type)* |
| `ref_id` | int | Id of an operation in FINA that this money return is based on · *FINA ში არსებული ოპერაციის Id, რომლის საფუძველიცაა მოცემული თანხის დაბრუნება* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |
| `add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |

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

### saveDocBonusPayment

Payment with points · *ქულით გადახდა*

Save a payment with points (insert, update) · *ქულით გადახდის შენახვა (insert, update)*

**POST** `api/operation/saveDocBonusPayment`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2019-03-09T13:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "ქულით გადახდა - მყიდველი", 
    "amount": 20.4, 
    "currency": "GEL", 
    "rate": 1, 
    "store": 1, 
    "user": 1, 
    "staff": 3, 
    "project": 2, 
    "customer": 8, 
    "ref_id": 0, 
    "make_entry": true 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Operation Id. (pass 0 to create a new one) · *ოპერაციის Id. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `num` | long | Document number · *დოკუმენტის ნომერი* |
| `purpose` | string[750] | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `currency` | string | Currency code · *ვალუტის კოდი* |
| `rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `store` | int | Store (warehouse) Id · *საწყობის Id* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `staff` | int | Staff member Id (0 = take the staff member linked to the user) · *თანამშრომლის Id (0 = მომხმარებელზე მიბმული თანამშრომლის აღება)* |
| `project` | int | Project Id · *პროექტის Id* |
| `customer` | int | Customer Id · *მყიდველის Id* |
| `ref_id` | int | Id of an operation in FINA that this payment with points is based on · *FINA ში არსებული ოპერაციის Id, რომლის საფუძველიცაა მოცემული ქულით გადახდა* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |

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

### saveDocGiftPayment

Redeem a gift card · *სასაჩუქრე ბარათის განაღდება*

Redeem a gift card (insert) · *სასაჩუქრე ბარათის განაღდება (insert)*

**POST** `api/operation/saveDocGiftPayment`

**Request body**

```json
{ 
    "date": "2024-05-22T13:00:00", 
    "card_id": 100009, 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "სასაჩუქრე ბარათით გადახდა - CARD123456", 
    "amount": 20.4, 
    "store": 1, 
    "user": 1, 
    "staff": 3, 
    "project": 2, 
    "customer": 8, 
    "ref_id": 133, 
    "make_entry": true 
}
```

| Field | Type | Description |
|---|---|---|
| `date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `card_id` | int | Gift card Id · *სასაჩუქრე ბარათის Id* |
| `num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `num` | long | Document number · *დოკუმენტის ნომერი* |
| `purpose` | string[750] | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `store` | int | Store (warehouse) Id · *საწყობის Id* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `staff` | int | Staff member Id (0 = take the staff member linked to the user) · *თანამშრომლის Id (0 = მომხმარებელზე მიბმული თანამშრომლის აღება)* |
| `project` | int | Project Id · *პროექტის Id* |
| `customer` | int | Customer Id · *მყიდველის Id* |
| `ref_id` | int | Id of an operation in FINA that this card redemption is based on · *FINA ში არსებული ოპერაციის Id, რომლის საფუძველიცაა მოცემული ბარათის განაღდება* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |

**Response**

```json
{ 
    "id": 3, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the created operation · *შექმნილი ოპერაციის Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---
