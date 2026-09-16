# Writing documents — sales, purchases, transfers and orders

10 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`saveDocCustomerOrder`](#savedoccustomerorder) | POST | `api/operation/saveDocCustomerOrder` | Order received from a customer |
| [`saveDocProductOut`](#savedocproductout) | POST | `api/operation/saveDocProductOut` | Goods sale |
| [`saveDocProductIn`](#savedocproductin) | POST | `api/operation/saveDocProductIn` | Goods purchase |
| [`saveDocProductMove`](#savedocproductmove) | POST | `api/operation/saveDocProductMove` | Internal transfer |
| [`saveDocProvidedService`](#savedocprovidedservice) | POST | `api/operation/saveDocProvidedService` | Provision of a service |
| [`saveDocReceivedService`](#savedocreceivedservice) | POST | `api/operation/saveDocReceivedService` | Receipt of a service |
| [`saveDocCustomerReturn`](#savedoccustomerreturn) | POST | `api/operation/saveDocCustomerReturn` | Return of goods from a customer |
| [`saveDocProductCancel`](#savedocproductcancel) | POST | `api/operation/saveDocProductCancel` | Write-off of goods |
| [`saveDocCafeOrder`](#savedoccafeorder) | POST | `api/operation/saveDocCafeOrder` | Restaurant order |
| [`updateRsStatus`](#updatersstatus) | POST | `api/operation/updateRsStatus` | Update the RS status of an existing waybill |

---

### saveDocCustomerOrder

Order received from a customer · *მყიდველისგან მიღებული შეკვეთა*

Save an order received from a customer (insert, update) · *მყიდველისგან მიღებული შეკვეთის შენახვა (insert, update)*

**POST** `api/operation/saveDocCustomerOrder`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2018-12-04T18:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "შეკვეთა მყიდველისგან - Test", 
    "amount": 65.7, 
    "currency": "GEL", 
    "rate": 1.0, 
    "store": 1, 
    "user": 2, 
    "staff": 3, 
    "project": 2, 
    "customer": 8, 
    "is_vat": true, 
    "pay_type": 1, 
    "tr_start": "ტრანსპორტირების დაწყების ადგილი", 
    "tr_end": "ტრანსპორტირების დასრულების ადგილი", 
    "invoice_num": 0, 
    "invoice_bank": 0, 
    "pay_date": "2021-02-12T12:02:00", 
    "delivery_date": "2021-02-12T12:02:00", 
    "reserved_until": "2021-02-14T12:02:00", 
    "reserved": true, 
    "actived": true, 
    "add_fields": [{ 
        "field": "usr_column_511", 
        "value": "ირმის ნახტომი" 
    }], 
    "products": [{ 
        "id": 2, 
        "sub_id": 1, 
        "quantity": 1.0, 
        "price": 35.70 
    }, { 
        "id": 3, 
        "sub_id": 2, 
        "quantity": 3.0, 
        "price": 10.0 
    }], 
    "services": [] 
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
| `is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `tr_start` | string[200] | Place where transportation starts · *ტრანსპორტირების დაწყების ადგილი* |
| `tr_end` | string[200] | Place where transportation ends · *ტრანსპორტირების დასრულების ადგილი* |
| `invoice_num` | int | Invoice number · *ინვოისის ნომერი* |
| `invoice_bank` | int | Bank account Id (getBankAccounts) · *საბანკო ანგარიშის Id (getBankAccounts)* |
| `pay_date` | datetime | Payment date (>= the operation date) · *გადახდის თარიღი (> = ოპერაციის თარიღზე)* |
| `delivery_date` | datetime | Delivery date (>= the operation date) · *მიწოდების თარიღი (>= ოპერაციის თარიღზე)* |
| `reserved_until` | datetime | Date the reservation is automatically cancelled (>= the operation date (if automatic reservation cancellation is enabled in the program)) · *რეზერვაციის ავტომატურად გაუქმების თარიღი (>= ოპერაციის თარიღზე (თუ პროგრამაში ჩართულია რეზერვაციის ავტომატური გაუქმების რეჟიმი))* |
| `reserved` | bool | Reservation status · *რეზერვაციის სტატუსი* |
| `actived` | bool | Order status (whether it is active) · *შეკვეთის სტატუსი (აქტიურია თუ არა)* |
| `add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `products[].id` | int | Product Id · *საქონლის Id* |
| `products[].sub_id` | int | Product sub-code Id (default=0) · *საქონლის ქვე-კოდის Id, (default=0)* |
| `products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `products[].price` | decimal | Unit price of the product · *საქონლის ერთეულის ფასი* |
| `services[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `services[].id` | int | Provided service Id · *გაწეული მომსახურების Id* |
| `services[].quantity` | decimal | Quantity of the provided service · *გაწეული მომსახურების რაოდენობა* |
| `services[].price` | decimal | Unit price of the provided service · *გაწეული მომსახურების ერთეულის ფასი* |

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

See also: `getBankAccounts`

---

### saveDocProductOut

Goods sale · *საქონლის რეალიზაცია*

Save a goods sale (insert, update) · *საქონლის რეალიზაციის შენახვა (insert, update)*

**POST** `api/operation/saveDocProductOut`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2018-12-08T18:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "რელიზაცია", 
    "amount": 65.7, 
    "currency": "GEL", 
    "rate": 1.0, 
    "store": 1, 
    "user": 2, 
    "staff": 3, 
    "project": 2, 
    "customer": 8, 
    "is_vat": true, 
    "make_entry": true, 
    "pay_type": 1, 
    "price_type": 3, 
    "w_type": 2, 
    "t_type": 1, 
    "t_payer": 2, 
    "w_cost": 0.5, 
    "foreign": false, 
    "drv_name": "მძღოლის სახელი, გვარი", 
    "tr_start": "ტრანსპორტირების დაწყების ადგილი", 
    "tr_end": "ტრანსპორტირების დასრულების ადგილი", 
    "driver_id": "12345678910", 
    "car_num": "SAK005", 
    "tr_text": "მისაბმელი/გადამზიდავი", 
    "sender": "გამგზავნი/ჩამბარებელი", 
    "reciever": "მიმღები", 
    "comment": "კომენტარის ტექსტი", 
    "overlap_type": 0, 
    "overlap_amount": 0, 
    "add_fields": [{ 
        "field": "usr_column_510", 
        "value": "test string" 
    }], 
    "products": [{ 
        "id": 2, 
        "sub_id": 0, 
        "quantity": 1.0, 
        "price": 35.70 
    }, { 
        "id": 3, 
        "sub_id": 0, 
        "quantity": 3.0, 
        "price": 10.0 
    }], 
    "services": [{ 
        "id": 20, 
        "quantity": 1.0, 
        "price": 2.0 
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
| `is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |
| `pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `price_type` | int | Price type Id (default 3 (retail price)) · *ფასის ტიპის Id (Default -3 (საცალო ფასი))* |
| `w_type` | byte | Waybill type (2 - with transportation, 3 - without transportation) · *ზედნადების ტიპი (2 - ტრანსპორტირებით, 3 - ტრანსპორტირების გარეშე)* |
| `t_type` | byte | Transportation type (1 - road, 2 - rail, 3 - air, 4 - other, 6 - foreign road, 7 - carrier road) · *ტრანსპორტირების ტიპი (1 - საავტომობილო, 2 - სარკინიგზო, 3 - საავიაციო, 4 - სხვა, 6 - საავტომობილო უცხო ქვეყნის, 7 - გადამზიდავი საავტომობილო)* |
| `t_payer` | byte | Payer of the transportation cost (1 - buyer, 2 - seller) · *ტრანსპორტირების ღირებულების გადამხდელი (1 - მყიდველი, 2 - გამყიდველი)* |
| `w_cost` | decimal | Transportation cost · *ტრანსპორტირების ხარჯი* |
| `foreign` | bool | Foreign citizen · *უცხო ქვეყნის მოქალაქე* |
| `drv_name` | string[50] | Driver's first and last name · *მძღოლის სახელი, გვარი* |
| `tr_start` | string[200] | Place where transportation starts · *ტრანსპორტირების დაწყების ადგილი* |
| `tr_end` | string[200] | Place where transportation ends · *ტრანსპორტირების დასრულების ადგილი* |
| `driver_id` | string[50] | Driver's personal number · *მძღოლის პირადი ნომერი* |
| `car_num` | string[50] | Vehicle registration number · *ავტომობილის ნომერი* |
| `tr_text` | string[200] | Trailer/carrier (if the transportation type is 7, the carrier's identification code must be specified; if the transportation type is 4, the transportation form is specified; for road transport, the trailer number if there is one) · *მისაბმელი/გადამზიდავი (თუ ტრანსპორტირების ტიპი არის 7, უნდა მიეთითოს გადამზიდავის საიდენტიფიკაციო კოდი, თუ ტრანსპორტირების ტიპი არის 4 - ეთიება ტრანსპორტირების ფორმა, ხოლო საავტომობილოს შემთხვევაში - მისაბმელის ნომერი ასეთის არსებობის შემთხვევაში)* |
| `sender` | string | Sender/deliverer · *გამგზავნი/ჩამბარებელი* |
| `reciever` | string | Recipient · *მიმღები* |
| `comment` | string | Comment · *კომენტარი* |
| `overlap_type` | byte | Advance/VAT offset (0 - offset neither, 1 - offset the advance, VAT partially, 2 - offset the advance, VAT fully, 3 - offset the advance, not VAT) · *ავანსი/დღგ-ს გადახურვა (0 - არ გადაიხუროს არც ერთი, 1 - ავანსი გადაიხუროს, დღგ - ნაწილობრივ, 2 - ავანსი გადაიხუროს, დღგ - სრულად, 3 - ავანსი გადაიხუროს, დღგ - არა) * |
| `overlap_amount` | decimal | Offset VAT amount (if overlap_type is 2 the amount is calculated automatically; if overlap_type is 1, the offset VAT amount must not exceed the VAT amount of the customer's advance) · *გადახურული დღგ- ს თანხა, (თუ overlap_type არის 2, მოხდება თანხის ავტომატური დაანგარიშება, თუ overlap_type არის 1 - გადახურული დღგ -ს თანხა არ უნდა აღემატებოდეს მყიდველის ავანსის დღგ-ს თანხას)* |
| `add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `products[].id` | int | Product Id · *საქონლის Id* |
| `products[].sub_id` | int | Product sub-code Id (default=0) · *საქონლის ქვე-კოდის Id, (default=0)* |
| `products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `products[].price` | decimal | Unit price of the product · *საქონლის ერთეულის ფასი* |
| `services[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `services[].id` | int | Provided service Id · *გაწეული მომსახურების Id* |
| `services[].quantity` | decimal | Quantity of the provided service · *გაწეული მომსახურების რაოდენობა* |
| `services[].price` | decimal | Unit price of the provided service · *გაწეული მომსახურების ერთეულის ფასი* |

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

### saveDocProductIn

Goods purchase · *საქონლის შესყიდვა*

Save a goods purchase (insert, update) · *საქონლის შესყიდვის შენახვა (insert, update)*

**POST** `api/operation/saveDocProductIn`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2019-02-18T13:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "shesyidva", 
    "amount": 65.7, 
    "currency": "GEL", 
    "rate": 1, 
    "store": 1, 
    "user": 2, 
    "staff": 3, 
    "project": 2, 
    "vendor": 2, 
    "is_vat": true, 
    "make_entry": true, 
    "w_num": "", 
    "i_num": "", 
    "add_fields": [{ 
        "field": "usr_column_525", 
        "value": "test string123" 
    }], 
    "products": [{ 
        "id": 2, 
        "sub_id": 0, 
        "quantity": 1, 
        "price": 35.7 
    }, { 
        "id": 3, 
        "sub_id": 0, 
        "quantity": 3, 
        "price": 10 
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
| `vendor` | int | Vendor Id · *მომწოდებლის Id* |
| `is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |
| `w_num` | string[50] | Waybill number · *ზედნადების ნომერი* |
| `i_num` | string[50] | Invoice / customs declaration number · *ა/ფ, საბაჟო დეკლარაციის ნომერი* |
| `add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `products[].id` | int | Product Id · *საქონლის Id* |
| `products[].sub_id` | int | Product sub-code Id (default=0) · *საქონლის ქვე-კოდის Id, (default=0)* |
| `products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `products[].price` | decimal | Unit price of the product · *საქონლის ერთეულის ფასი* |

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

### saveDocProductMove

Internal transfer · *შიდა გადაზიდვა*

Save an internal goods transfer (insert, update) · *საქონლის შიდა გადაზიდვის შენახვა (insert, update)*

**POST** `api/operation/saveDocProductMove`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2019-02-14T11:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "შიდა გადაზიდვა - Test", 
    "store_from": 1, 
    "store_to": 2, 
    "user": 2, 
    "staff": 3, 
    "make_entry": true, 
    "t_type": 1, 
    "t_payer": 2, 
    "w_cost": 0.5, 
    "foreign": false, 
    "drv_name": "მძღოლის სახელი, გვარი", 
    "tr_start": "ტრანსპორტირების დაწყების ადგილი", 
    "tr_end": "ტრანსპორტირების დასრულების ადგილი", 
    "driver_id": "12345678910", 
    "car_num": "SAK005", 
    "tr_text": "მისაბმელი/გადამზიდავი", 
    "add_fields": [{ 
        "field": "usr_column_518", 
        "value": "test string123" 
    }], 
    "products": [{ 
        "id": 2, 
        "sub_id": 0, 
        "quantity": 1 
    }, { 
        "id": 3, 
        "sub_id": 0, 
        "quantity": 3 
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
| `store_from` | int | Id of the sending store · *გამგზავნი საწყობის Id* |
| `store_to` | int | Id of the receiving store · *მიმღები საწყობის Id* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `staff` | int | Staff member Id (0 = take the staff member linked to the user) · *თანამშრომლის Id (0 = მომხმარებელზე მიბმული თანამშრომლის აღება)* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |
| `t_type` | byte | Transportation type (1 - road, 2 - rail, 3 - air, 4 - other, 6 - foreign road, 7 - carrier road) · *ტრანსპორტირების ტიპი (1 - საავტომობილო, 2 - სარკინიგზო, 3 - საავიაციო, 4 - სხვა, 6 - საავტომობილო უცხო ქვეყნის, 7 - გადამზიდავი საავტომობილო)* |
| `t_payer` | byte | Payer of the transportation cost (1 - buyer, 2 - seller) · *ტრანსპორტირების ღირებულების გადამხდელი (1 - მყიდველი, 2 - გამყიდველი)* |
| `w_cost` | decimal | Transportation cost · *ტრანსპორტირების ხარჯი* |
| `foreign` | bool | Foreign citizen · *უცხო ქვეყნის მოქალაქე* |
| `drv_name` | string[50] | Driver's first and last name · *მძღოლის სახელი, გვარი* |
| `tr_start` | string[200] | Place where transportation starts · *ტრანსპორტირების დაწყების ადგილი* |
| `tr_end` | string[200] | Place where transportation ends · *ტრანსპორტირების დასრულების ადგილი* |
| `driver_id` | string[50] | Driver's personal number · *მძღოლის პირადი ნომერი* |
| `car_num` | string[50] | Vehicle registration number · *ავტომობილის ნომერი* |
| `tr_text` | string[200] | Trailer/carrier (if the transportation type is 7, the carrier's identification code must be specified; if the transportation type is 4, the transportation form is specified; for road transport, the trailer number if there is one) · *მისაბმელი/გადამზიდავი (თუ ტრანსპორტირების ტიპი არის 7, უნდა მიეთითოს გადამზიდავის საიდენტიფიკაციო კოდი, თუ ტრანსპორტირების ტიპი არის 4 - ეთიება ტრანსპორტირების ფორმა, ხოლო საავტომობილოს შემთხვევაში - მისაბმელის ნომერი ასეთის არსებობის შემთხვევაში)* |
| `add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `products[].id` | int | Product Id · *საქონლის Id* |
| `products[].sub_id` | int | Product sub-code Id (default=0) · *საქონლის ქვე-კოდის Id, (default=0)* |
| `products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |

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

### saveDocProvidedService

Provision of a service · *მომსახურების გაწევა*

Save a provided service (insert, update) · *გაწეული მომსახურების შენახვა (insert, update)*

**POST** `api/operation/saveDocProvidedService`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2018-12-08T18:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "მომსახურების გაწევა", 
    "amount": 2.0, 
    "currency": "GEL", 
    "rate": 1.0, 
    "store": 1, 
    "user": 2, 
    "staff": 3, 
    "project": 2, 
    "customer": 8, 
    "is_vat": true, 
    "make_entry": true, 
    "pay_type": 1, 
    "overlap_type": 0, 
    "overlap_amount": 0, 
    "add_fields": [{ 
        "field": "usr_column_510", 
        "value": "test string" 
    }], 
    "services": [{ 
        "id": 20, 
        "quantity": 1.0, 
        "price": 2.0 
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
| `is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |
| `pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `overlap_type` | byte | Advance/VAT offset (0 - offset neither, 1 - offset the advance, VAT partially, 2 - offset the advance, VAT fully, 3 - offset the advance, not VAT) · *ავანსი/დღგ-ს გადახურვა (0 - არ გადაიხუროს არც ერთი, 1 - ავანსი გადაიხუროს, დღგ - ნაწილობრივ, 2 - ავანსი გადაიხუროს, დღგ - სრულად, 3 - ავანსი გადაიხუროს, დღგ - არა) * |
| `overlap_amount` | decimal | Offset VAT amount (if overlap_type is 2 the amount is calculated automatically; if overlap_type is 1, the offset VAT amount must not exceed the VAT amount of the customer's advance) · *გადახურული დღგ- ს თანხა, (თუ overlap_type არის 2, მოხდება თანხის ავტომატური დაანგარიშება, თუ overlap_type არის 1 - გადახურული დღგ -ს თანხა არ უნდა აღემატებოდეს მყიდველის ავანსის დღგ-ს თანხას)* |
| `add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `services[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `services[].id` | int | Provided service Id · *გაწეული მომსახურების Id* |
| `services[].quantity` | decimal | Quantity of the provided service · *გაწეული მომსახურების რაოდენობა* |
| `services[].price` | decimal | Unit price of the provided service · *გაწეული მომსახურების ერთეულის ფასი* |

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

### saveDocReceivedService

Receipt of a service · *მომსახურების მიღება*

Save a received service (insert, update) · *მიღებული მომსახურების შენახვა (insert, update)*

**POST** `api/operation/saveDocReceivedService`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2018-12-08T18:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "მომსახურების მიღება", 
    "amount": 2.0, 
    "currency": "GEL", 
    "rate": 1.0, 
    "user": 2, 
    "project": 2, 
    "vendor": 3, 
    "is_vat": true, 
    "make_entry": true, 
    "pay_type": 1, 
    "overlap_type": 0, 
    "overlap_amount": 0, 
    "add_fields": [{ 
        "field": "usr_column_510", 
        "value": "test string" 
    }], 
    "services": [{ 
        "id": 2, 
        "quantity": 1.0, 
        "price": 2.0 
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
| `project` | int | Project Id · *პროექტის Id* |
| `vendor` | int | Vendor Id · *მომწოდებლის Id* |
| `is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |
| `pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `overlap_type` | byte | Advance/VAT offset (0 - offset neither, 1 - offset the advance, VAT partially, 2 - offset the advance, VAT fully, 3 - offset the advance, not VAT) · *ავანსი/დღგ-ს გადახურვა (0 - არ გადაიხუროს არც ერთი, 1 - ავანსი გადაიხუროს, დღგ - ნაწილობრივ, 2 - ავანსი გადაიხუროს, დღგ - სრულად, 3 - ავანსი გადაიხუროს, დღგ - არა) * |
| `overlap_amount` | decimal | Offset VAT amount (if overlap_type is 2 the amount is calculated automatically; if overlap_type is 1, the offset VAT amount must not exceed the VAT amount of the customer's advance) · *გადახურული დღგ- ს თანხა, (თუ overlap_type არის 2, მოხდება თანხის ავტომატური დაანგარიშება, თუ overlap_type არის 1 - გადახურული დღგ -ს თანხა არ უნდა აღემატებოდეს მყიდველის ავანსის დღგ-ს თანხას)* |
| `add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `services[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `services[].id` | int | Received service Id · *მიღებული მომსახურების Id* |
| `services[].quantity` | decimal | Quantity of the provided service · *გაწეული მომსახურების რაოდენობა* |
| `services[].price` | decimal | Unit price of the provided service · *გაწეული მომსახურების ერთეულის ფასი* |

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

### saveDocCustomerReturn

Return of goods from a customer · *საქონლის დაბრუნება მყიდველისგან*

Save goods returned from a customer (insert, update) · *მყიდველისგან დაბრუნებული საქონლის შენახვა (insert, update)*

**POST** `api/operation/saveDocCustomerReturn`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2019-05-01T14:25:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "dabruneba", 
    "amount": 65.7, 
    "currency": "GEL", 
    "rate": 1, 
    "store": 1, 
    "user": 2, 
    "staff": 3, 
    "project": 2, 
    "customer": 8, 
    "is_vat": true, 
    "make_entry": true, 
    "pay_type": 1, 
    "t_type": 1, 
    "t_payer": 2, 
    "w_cost": 0.5, 
    "foreign": false, 
    "drv_name": "მძღოლის სახელი, გვარი", 
    "tr_start": "ტრანსპორტირების დაწყების ადგილი", 
    "tr_end": "ტრანსპორტირების დასრულების ადგილი", 
    "driver_id": "12345678910", 
    "car_num": "SAK001", 
    "tr_text": "მისაბმელი/გადამზიდავი", 
    "products": [{ 
        "id": 29, 
        "sub_id": 0, 
        "quantity": 1, 
        "price": 35.7, 
        "out_id": 6547 
    }, { 
        "id": 3, 
        "sub_id": 0, 
        "quantity": 3, 
        "price": 10, 
        "out_id": 0 
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
| `is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |
| `pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `t_type` | byte | Transportation type (1 - road, 2 - rail, 3 - air, 4 - other, 6 - foreign road, 7 - carrier road) · *ტრანსპორტირების ტიპი (1 - საავტომობილო, 2 - სარკინიგზო, 3 - საავიაციო, 4 - სხვა, 6 - საავტომობილო უცხო ქვეყნის, 7 - გადამზიდავი საავტომობილო)* |
| `t_payer` | byte | Payer of the transportation cost (1 - buyer, 2 - seller) · *ტრანსპორტირების ღირებულების გადამხდელი (1 - მყიდველი, 2 - გამყიდველი)* |
| `w_cost` | decimal | Transportation cost · *ტრანსპორტირების ხარჯი* |
| `foreign` | bool | Foreign citizen · *უცხო ქვეყნის მოქალაქე* |
| `drv_name` | string[50] | Driver's first and last name · *მძღოლის სახელი, გვარი* |
| `tr_start` | string[200] | Place where transportation starts · *ტრანსპორტირების დაწყების ადგილი* |
| `tr_end` | string[200] | Place where transportation ends · *ტრანსპორტირების დასრულების ადგილი* |
| `driver_id` | string[50] | Driver's personal number · *მძღოლის პირადი ნომერი* |
| `car_num` | string[50] | Vehicle registration number · *ავტომობილის ნომერი* |
| `tr_text` | string[200] | Trailer/carrier (if the transportation type is 7, the carrier's identification code must be specified; if the transportation type is 4, the transportation form is specified; for road transport, the trailer number if there is one) · *მისაბმელი/გადამზიდავი (თუ ტრანსპორტირების ტიპი არის 7, უნდა მიეთითოს გადამზიდავის საიდენტიფიკაციო კოდი, თუ ტრანსპორტირების ტიპი არის 4 - ეთიება ტრანსპორტირების ფორმა, ხოლო საავტომობილოს შემთხვევაში - მისაბმელის ნომერი ასეთის არსებობის შემთხვევაში)* |
| `products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `products[].id` | int | Product Id · *საქონლის Id* |
| `products[].sub_id` | int | Product sub-code Id (default=0) · *საქონლის ქვე-კოდის Id, (default=0)* |
| `products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `products[].price` | decimal | Unit price of the product · *საქონლის ერთეულის ფასი* |
| `products[].out_id` | int | Id of the sale operation being returned (which specific sale is being returned, default=0) · *გაყიდვის ოპერაციის Id (თუ რომელი გაყიდვის დაბრუნება ხდება კონკრეტულად, default=0)* |

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

### saveDocProductCancel

Write-off of goods · *საქონლის ჩამოწერა*

Save a write-off of goods (insert, update) · *საქონლის ჩამოწერის შენახვა (insert, update)*

**POST** `api/operation/saveDocProductCancel`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2019-02-23T13:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "ჩამოწერა", 
    "store": 1, 
    "user": 2, 
    "staff": 3, 
    "project": 2, 
    "make_entry": true, 
    "add_fields": [{ 
        "field": "usr_column_526", 
        "value": "test string123" 
    }], 
    "products": [{ 
        "id": 2, 
        "sub_id": 1, 
        "quantity": 1 
    }, { 
        "id": 3, 
        "sub_id": 0, 
        "quantity": 3 
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
| `store` | int | Store (warehouse) Id · *საწყობის Id* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `staff` | int | Staff member Id (0 = take the staff member linked to the user) · *თანამშრომლის Id (0 = მომხმარებელზე მიბმული თანამშრომლის აღება)* |
| `project` | int | Project Id · *პროექტის Id* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |
| `add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `products[].id` | int | Product Id · *საქონლის Id* |
| `products[].sub_id` | int | Product sub-code Id (default=0) · *საქონლის ქვე-კოდის Id, (default=0)* |
| `products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |

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

### saveDocCafeOrder

Restaurant order · *რესტორნის შეკვეთა*

Save a restaurant order (insert, update) · *რესტორნის შეკვეთის შენახვა (insert, update)*

**POST** `api/operation/saveDocCafeOrder`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2019-02-28T10:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "შეკვეთა cafe", 
    "amount": 9, 
    "store": 2, 
    "user": 2, 
    "project": 2, 
    "customer_name": "", 
    "customer_tel": "", 
    "customer_address": "", 
    "products": [{ 
        "id": 2, 
        "quantity": 1, 
        "price": 3.5 
    }, { 
        "id": 3, 
        "quantity": 3, 
        "price": 1 
    }], 
    "services": [] 
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
| `store` | int | Store (warehouse) Id · *საწყობის Id* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `project` | int | Project Id · *პროექტის Id* |
| `customer_name` | string[100] | Customer's first and last name · *მყიდველის სახელი, გვარი* |
| `customer_tel` | string[20] | Customer's phone · *მყიდველის ტელ* |
| `customer_address` | string[250] | Customer's address · *მყიდველის მისამართი* |
| `products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `products[].id` | int | Product Id · *საქონლის Id* |
| `products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `products[].price` | decimal | Unit price of the product · *საქონლის ერთეულის ფასი* |
| `services[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `services[].id` | int | Provided service Id · *გაწეული მომსახურების Id* |
| `services[].quantity` | decimal | Quantity of the provided service · *გაწეული მომსახურების რაოდენობა* |
| `services[].price` | decimal | Unit price of the provided service · *გაწეული მომსახურების ერთეულის ფასი* |

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

### updateRsStatus

Update the RS status of an existing waybill · *არსებული ზედნადების RS სტატუსის განახლება*

Update the RS status of an existing waybill · *არსებული ზედნადების RS სტატუსის განახლება*

**POST** `api/operation/updateRsStatus`

**Request body**

```json
{ 
    "id": 4164, 
    "w_id": 352264608, 
    "w_status": 1, 
    "w_num": "0123654878" 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of an operation in the FINA database · *FINA ს ბაზაში არსებული ოპერაციის Id* |
| `w_id` | long | Id of the waybill assigned when uploading to RS.ge · *ზედნადების Id, რომელიც მიენიჭა RS.ge ზე ატვირთვისას* |
| `w_status` | int | Status of the waybill assigned on RS.ge · *ზედნადების სტატუსი, რომელიც მიენიჭა RS.ge ზე* |
| `w_num` | string[50] | Number of the waybill assigned when uploading to RS.ge · *ზედნადების ნომერი, რომელიც მიენიჭა RS.ge ზე ატვირთვისას* |

**Response**

```json
{ 
    "status": true, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `status` | bool | Returns a value depending on whether the operation succeeded · *აბრუნებს მნიშვნელობას ოპერაციის წარმატებით შესრულების მიხედვით* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---
