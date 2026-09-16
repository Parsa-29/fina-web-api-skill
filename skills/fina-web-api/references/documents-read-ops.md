# Reading documents — transfers, services and production

7 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getDocProductMove`](#getdocproductmove) | GET | `api/operation/getDocProductMove/{id}` | Goods transfer |
| [`getDocInventoryMove`](#getdocinventorymove) | GET | `api/operation/getDocInventoryMove/{id}` | Fixed asset transfer |
| [`getDocProvidedService`](#getdocprovidedservice) | GET | `api/operation/getDocProvidedService/{id}` | Provision of a service |
| [`getDocReceivedService`](#getdocreceivedservice) | GET | `api/operation/getDocReceivedService/{id}` | Receipt of a service |
| [`getDocProduction`](#getdocproduction) | GET | `api/operation/getDocProduction/{id}` | Production, adding goods - repair |
| [`getDocAutoService`](#getdocautoservice) | GET | `api/operation/getDocAutoService/{id}` | Auto service request |
| [`getDocAdvProduction`](#getdocadvproduction) | GET | `api/operation/getDocAdvProduction/{id}` | Complex production/disassembly |

---

### getDocProductMove

Goods transfer · *საქონლის გადატანა*

Fetch a goods transfer · *საქონლის გადატანის წამოღება*

**GET** `api/operation/getDocProductMove/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
    "product_move": { 
        "id": 14830, 
        "date": "2020-03-18T10:24:13", 
        "num_pfx": "", 
        "num": 11, 
        "waybill_num": null, 
        "purpose": "საქონლის გადატანა № 11", 
        "amount": 18.69858, 
        "store_from": 1, 
        "store_to": 2, 
        "user": 1, 
        "staff": 2, 
        "make_entry": true, 
        "t_type": 1, 
        "t_payer": 1, 
        "w_cost": 0.0, 
        "foreign": false, 
        "drv_name": "", 
        "tr_start": "", 
        "tr_end": "", 
        "driver_id": "", 
        "car_num": "", 
        "tr_text": "", 
        "add_fields": [{ 
            "field": "usr_column_518", 
            "value": "12:30" 
        }], 
        "products": [{ 
            "id": 12, 
            "sub_id": 0, 
            "self_cost": 1.01090475053712, 
            "quantity": 5.0 
        }, { 
            "id": 13, 
            "sub_id": 0, 
            "self_cost": 1.94915122076992, 
            "quantity": 7.0 
        }] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `product_move` | object | The internal goods transfer, consisting of: · *საქონლის შიდა გადატანაა რომელიც შედგება:* |
| `product_move.id` | int | Document id · *დოკუმენტის id* |
| `product_move.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `product_move.num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `product_move.num` | long | Document number · *დოკუმენტის ნომერი* |
| `product_move.waybill_num` | string | Waybill number (RS - Revenue Service) · *ზედნადების ნომერი (RS)* |
| `product_move.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `product_move.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `product_move.store_from` | int | Store Id (sender) · *საწყობის Id (გამგზავნი)* |
| `product_move.store_to` | int | Store Id (recipient) · *საწყობის Id (მიმღები)* |
| `product_move.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `product_move.staff` | int | Staff member Id · *თანამშრომლის Id* |
| `product_move.make_entry` | bool | Accounting entry status · *ბუღალტრული გატარების სტატუსი* |
| `product_move.t_type` | byte | Transportation type (1 - road, 2 - rail, 3 - air, 4 - other, 6 - foreign road, 7 - carrier road) · *ტრანსპორტირების ტიპი (1 - საავტომობილო, 2 - სარკინიგზო, 3 - საავიაციო, 4 - სხვა, 6 - საავტომობილო უცხო ქვეყნის, 7 - გადამზიდავი საავტომობილო)* |
| `product_move.t_payer` | byte | Payer of the transportation cost (1 - buyer, 2 - seller) · *ტრანსპორტირების ღირებულების გადამხდელი (1 - მყიდველი, 2 - გამყიდველი)* |
| `product_move.w_cost` | decimal | Transportation cost · *ტრანსპორტირების ხარჯი* |
| `product_move.foreign` | bool | Foreign citizen · *უცხო ქვეყნის მოქალაქე* |
| `product_move.drv_name` | string | Driver's first and last name · *მძღოლის სახელი, გვარი* |
| `product_move.tr_start` | string | Place where transportation starts · *ტრანსპორტირების დაწყების ადგილი* |
| `product_move.tr_end` | string | Place where transportation ends · *ტრანსპორტირების დასრულების ადგილი* |
| `product_move.driver_id` | string | Driver's personal number · *მძღოლის პირადი ნომერი* |
| `product_move.car_num` | string | Vehicle registration number · *ავტომობილის ნომერი* |
| `product_move.tr_text` | string | Trailer/carrier (if the transportation type is 7, the carrier's identification code; if the transportation type is 4, the transportation form; for road transport, the trailer number if there is one) · *მისაბმელი/გადამზიდავი (თუ ტრანსპორტირების ტიპი არის 7, გადამზიდავის საიდენტიფიკაციო კოდი, თუ ტრანსპორტირების ტიპი არის 4 - ტრანსპორტირების ფორმა, ხოლო საავტომობილოს შემთხვევაში - მისაბმელის ნომერი ასეთის არსებობის შემთხვევაში)* |
| `product_move.add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `product_move.add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `product_move.add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `product_move.products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `product_move.products[].id` | int | Product Id · *საქონლის Id* |
| `product_move.products[].sub_id` | int | Product sub-code Id · *საქონლის ქვე-კოდის Id* |
| `product_move.products[].self_cost` | decimal | Product cost price · *საქონლის თვითღირებულება* |
| `product_move.products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getDocInventoryMove

Fixed asset transfer · *ძირითადი საშუალების გადატანა*

Fetch a fixed asset transfer · *ძირითადი საშუალების გადატანის წამოღება*

**GET** `api/operation/getDocInventoryMove/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
    "inventory_move": { 
        "id": 14831, 
        "date": "2020-03-18T10:25:25", 
        "num_pfx": "", 
        "num": 12, 
        "waybill_num": null, 
        "purpose": "ძირითადი საშუალების გადაადგილება № 12", 
        "amount": 5.7, 
        "store_from": 1, 
        "store_to": 6, 
        "user": 1, 
        "staff": 2, 
        "make_entry": true, 
        "t_type": 1, 
        "t_payer": 1, 
        "w_cost": 0.0, 
        "foreign": false, 
        "drv_name": "", 
        "tr_start": "", 
        "tr_end": "", 
        "driver_id": "", 
        "car_num": "", 
        "tr_text": "", 
        "add_fields": [{ 
            "field": "usr_column_518", 
            "value": "01" 
        }], 
        "inventories": [{ 
            "id": 34, 
            "self_cost": 1.9, 
            "quantity": 3.0 
        }] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `inventory_move` | object | The internal fixed asset transfer, consisting of: · *ძირ. საშუალების შიდა გადატანაა რომელიც შედგება:* |
| `inventory_move.id` | int | Document id · *დოკუმენტის id* |
| `inventory_move.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `inventory_move.num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `inventory_move.num` | long | Document number · *დოკუმენტის ნომერი* |
| `inventory_move.waybill_num` | string | Waybill number (RS - Revenue Service) · *ზედნადების ნომერი (RS)* |
| `inventory_move.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `inventory_move.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `inventory_move.store_from` | int | Store Id (sender) · *საწყობის Id (გამგზავნი)* |
| `inventory_move.store_to` | int | Store Id (recipient) · *საწყობის Id (მიმღები)* |
| `inventory_move.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `inventory_move.staff` | int | Staff member Id · *თანამშრომლის Id* |
| `inventory_move.make_entry` | bool | Accounting entry status · *ბუღალტრული გატარების სტატუსი* |
| `inventory_move.t_type` | byte | Transportation type (1 - road, 2 - rail, 3 - air, 4 - other, 6 - foreign road, 7 - carrier road) · *ტრანსპორტირების ტიპი (1 - საავტომობილო, 2 - სარკინიგზო, 3 - საავიაციო, 4 - სხვა, 6 - საავტომობილო უცხო ქვეყნის, 7 - გადამზიდავი საავტომობილო)* |
| `inventory_move.t_payer` | byte | Payer of the transportation cost (1 - buyer, 2 - seller) · *ტრანსპორტირების ღირებულების გადამხდელი (1 - მყიდველი, 2 - გამყიდველი)* |
| `inventory_move.w_cost` | decimal | Transportation cost · *ტრანსპორტირების ხარჯი* |
| `inventory_move.foreign` | bool | Foreign citizen · *უცხო ქვეყნის მოქალაქე* |
| `inventory_move.drv_name` | string | Driver's first and last name · *მძღოლის სახელი, გვარი* |
| `inventory_move.tr_start` | string | Place where transportation starts · *ტრანსპორტირების დაწყების ადგილი* |
| `inventory_move.tr_end` | string | Place where transportation ends · *ტრანსპორტირების დასრულების ადგილი* |
| `inventory_move.driver_id` | string | Driver's personal number · *მძღოლის პირადი ნომერი* |
| `inventory_move.car_num` | string | Vehicle registration number · *ავტომობილის ნომერი* |
| `inventory_move.tr_text` | string | Trailer/carrier (if the transportation type is 7, the carrier's identification code; if the transportation type is 4, the transportation form; for road transport, the trailer number if there is one) · *მისაბმელი/გადამზიდავი (თუ ტრანსპორტირების ტიპი არის 7, გადამზიდავის საიდენტიფიკაციო კოდი, თუ ტრანსპორტირების ტიპი არის 4 - ტრანსპორტირების ფორმა, ხოლო საავტომობილოს შემთხვევაში - მისაბმელის ნომერი ასეთის არსებობის შემთხვევაში)* |
| `inventory_move.add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `inventory_move.add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `inventory_move.add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `inventory_move.inventories[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `inventory_move.inventories[].id` | int | Fixed asset Id · *ძირ. საშუალების Id* |
| `inventory_move.inventories[].self_cost` | decimal | Cost price of the fixed asset · *ძირ. საშუალების თვითღირებულება* |
| `inventory_move.inventories[].quantity` | decimal | Fixed asset quantity · *ძირ. საშუალების რაოდენობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getDocProvidedService

Provision of a service · *მომსახურების გაწევა*

Fetch a provided service · *გაწეული მომსახურების წამოღება*

**GET** `api/operation/getDocProvidedService/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
    "doc_providedservice": { 
        "id": 6564, 
        "date": "2019-05-29T16:10:26", 
        "num_pfx": "", 
        "num": 9, 
        "purpose": "მომსახურების გაწევა № 9", 
        "amount": 240.0, 
        "currency": "GEL", 
        "rate": 1.0, 
        "store": 1, 
        "customer": 6, 
        "user": 1, 
        "staff": 1, 
        "project": 1, 
        "is_vat": true, 
        "make_entry": true, 
        "pay_type": 1, 
        "overlap_type": 3, 
        "overlap_amount": 0.0, 
        "add_fields": [{ 
            "field": "usr_column_510", 
            "value": "" 
        }, { 
            "field": "usr_column_528", 
            "value": "" 
        }], 
        "services": [{ 
            "id": 11, 
            "price": 120.0, 
            "quantity": 2.0 
        }] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `doc_providedservice` | object | The service provision operation, consisting of: · *მომსახურების გაწევის ოპერაციაა რომელიც შედგება:* |
| `doc_providedservice.id` | int | Document id · *დოკუმენტის id* |
| `doc_providedservice.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `doc_providedservice.num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `doc_providedservice.num` | long | Document number · *დოკუმენტის ნომერი* |
| `doc_providedservice.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `doc_providedservice.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `doc_providedservice.currency` | string | Currency code · *ვალუტის კოდი* |
| `doc_providedservice.rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `doc_providedservice.store` | int | Store (warehouse) Id · *საწყობის Id* |
| `doc_providedservice.customer` | int | Customer Id · *მყიდველის Id* |
| `doc_providedservice.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `doc_providedservice.staff` | int | Staff member Id · *თანამშრომლის Id* |
| `doc_providedservice.project` | int | Project Id · *პროექტის Id* |
| `doc_providedservice.is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `doc_providedservice.make_entry` | bool | Accounting entry status · *ბუღალტრული გატარების სტატუსი* |
| `doc_providedservice.pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `doc_providedservice.overlap_type` | byte | Advance/VAT offset (0 - offset neither, 1 - offset the advance, VAT partially, 2 - offset the advance, VAT fully, 3 - offset the advance, not VAT) · *ავანსი/დღგ-ს გადახურვა (0 - არ გადაიხუროს არც ერთი, 1 - ავანსი გადაიხუროს, დღგ - ნაწილობრივ, 2 - ავანსი გადაიხუროს, დღგ - სრულად, 3 - ავანსი გადაიხუროს, დღგ - არა) * |
| `doc_providedservice.overlap_amount` | decimal | Offset VAT amount · *გადახურული დღგ- ს თანხა * |
| `doc_providedservice.add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `doc_providedservice.add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `doc_providedservice.add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `doc_providedservice.services[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `doc_providedservice.services[].id` | int | Provided service Id · *გაწეული მომსახურების Id* |
| `doc_providedservice.services[].quantity` | decimal | Quantity of the provided service · *გაწეული მომსახურების რაოდენობა* |
| `doc_providedservice.services[].price` | decimal | Unit price of the provided service · *გაწეული მომსახურების ერთეულის ფასი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getDocReceivedService

Receipt of a service · *მომსახურების მიღება*

Fetch a received service · *მიღებული მომსახურების წამოღება*

**GET** `api/operation/getDocReceivedService/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
    "doc_receivedservice": { 
        "id": 10756, 
        "date": "2019-12-09T16:22:04", 
        "num_pfx": "", 
        "num": 5, 
        "purpose": "მომსახურების მიღება № 5", 
        "amount": 2000.0, 
        "currency": "GEL", 
        "rate": 1.0, 
        "vendor": 24, 
        "user": 1, 
        "staff": 0, 
        "project": 1, 
        "is_vat": false, 
        "make_entry": true, 
        "pay_type": 2, 
        "overlap_type": 2, 
        "overlap_amount": 0.0, 
        "add_fields": [{ 
            "field": "usr_column_525", 
            "value": "uu" 
        }, { 
            "field": "usr_column_536", 
            "value": "0.12.2" 
        }], 
        "services": [{ 
            "id": 7, 
            "price": 1000.000, 
            "quantity": 2.000 
        }] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `doc_receivedservice` | object | The service receipt operation, consisting of: · *მომსახურების მიღების ოპერაციაა რომელიც შედგება:* |
| `doc_receivedservice.id` | int | Document id · *დოკუმენტის id* |
| `doc_receivedservice.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `doc_receivedservice.num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `doc_receivedservice.num` | long | Document number · *დოკუმენტის ნომერი* |
| `doc_receivedservice.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `doc_receivedservice.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `doc_receivedservice.currency` | string | Currency code · *ვალუტის კოდი* |
| `doc_receivedservice.rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `doc_receivedservice.vendor` | int | Vendor Id · *მომწოდებელი Id* |
| `doc_receivedservice.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `doc_receivedservice.staff` | int | Staff member Id · *თანამშრომლის Id* |
| `doc_receivedservice.project` | int | Project Id · *პროექტის Id* |
| `doc_receivedservice.is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `doc_receivedservice.make_entry` | bool | Accounting entry status · *ბუღალტრული გატარების სტატუსი* |
| `doc_receivedservice.pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `doc_receivedservice.overlap_type` | byte | Advance/VAT offset (0 - offset neither, 1 - offset the advance, VAT partially, 2 - offset the advance, VAT fully, 3 - offset the advance, not VAT) · *ავანსი/დღგ-ს გადახურვა (0 - არ გადაიხუროს არც ერთი, 1 - ავანსი გადაიხუროს, დღგ - ნაწილობრივ, 2 - ავანსი გადაიხუროს, დღგ - სრულად, 3 - ავანსი გადაიხუროს, დღგ - არა) * |
| `doc_receivedservice.overlap_amount` | decimal | Offset VAT amount · *გადახურული დღგ- ს თანხა * |
| `doc_receivedservice.add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `doc_receivedservice.add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `doc_receivedservice.add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `doc_receivedservice.services[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `doc_receivedservice.services[].id` | int | Received service Id · *მიღებული მომსახურების Id* |
| `doc_receivedservice.services[].quantity` | decimal | Quantity of the received service · *მიღებული მომსახურების რაოდენობა* |
| `doc_receivedservice.services[].price` | decimal | Unit price of the received service · *მიღებული მომსახურების ერთეულის ფასი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getDocProduction

Production, adding goods - repair · *წარმოება, საქონლის დამატება - რემონტი*

Fetch production of goods/fixed assets, adding goods - repair · *საქონლის/ძ.ს. წარმოების, საქონლის დამატება - რემონტის წამოღება*

**GET** `api/operation/getDocProduction/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
    "production": { 
        "id": 17060, 
        "date": "2021-01-14T18:44:57.187", 
        "num_pfx": "", 
        "num": 3, 
        "purpose": "წარმოება № 3", 
        "amount": 5.92, 
        "store": 1, 
        "user": 1, 
        "make_entry": true, 
        "production_type": 0, 
        "add_fields": [{ 
            "field": "usr_column_542", 
            "value": "" 
        }], 
        "materials": [{ 
            "id": 1, 
            "self_cost": 2.96005599195705, 
            "quantity": 2.0, 
            "consumeds": [{ 
                "id": 13, 
                "self_cost": 1.94915124141993, 
                "quantity": 2.0 
            }, { 
                "id": 12, 
                "self_cost": 1.01090475053712, 
                "quantity": 2.0 
            }], 
            "expenses": [{ 
                "type": 0, 
                "amount": 25 
            }, { 
                "type": 1, 
                "amount": 30 
            }] 
        }] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `production` | object | Production of goods/fixed assets, adding goods - repair, consisting of: · *საქონელი/ძ.ს. წარმოება, საქონლის დამატება - რემონტია რომელიც შედგება:* |
| `production.id` | int | Document id · *დოკუმენტის id* |
| `production.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `production.num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `production.num` | long | Document number · *დოკუმენტის ნომერი* |
| `production.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `production.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `production.store` | int | Store (warehouse) Id · *საწყობის Id* |
| `production.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `production.make_entry` | bool | Accounting entry status · *ბუღალტრული გატარების სტატუსი* |
| `production.production_type` | byte | Production type (0 - production, 2 - adding a part, repair) · *წარმოების ტიპი (0 - წარმოება, 2 - ნაწილის დამატება, რემონტი)* |
| `production.add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `production.add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `production.add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `production.materials[]` | collection | Collection of produced goods/fixed assets consisting of: · *ნაწარმოები საქონლის/ ძ.ს. კოლექცია შედგება:* |
| `production.materials[].id` | int | Id of the produced product / fixed asset · *ნაწარმოები საქონლის/ ძ.ს. Id* |
| `production.materials[].self_cost` | decimal | Cost price of the produced goods/fixed asset unit · *ნაწარმოები საქონლის/ ძ.ს. ერთეულის თვითღირებულება* |
| `production.materials[].quantity` | decimal | Quantity of produced goods/fixed assets · *ნაწარმოები საქონლის/ ძ.ს. რაოდენობა* |
| `production.materials[].consumeds[]` | collection | Collection of goods/fixed assets consumed for these produced goods/fixed assets, consisting of: · *მოცემული ნაწარმოები საქონელი/ძ.ს. სთვის გახარჯული საქონელი/ძ.ს. კოლექცია შედგება:* |
| `production.materials[].consumeds[].id` | int | Id of the consumed goods/fixed asset · *გახარჯული საქონლის/ ძ.ს. Id* |
| `production.materials[].consumeds[].self_cost` | decimal | Cost price of the consumed goods/fixed asset unit · *გახარჯული საქონლის/ ძ.ს. ერთეულის თვითღირებულება* |
| `production.materials[].consumeds[].quantity` | decimal | Total quantity of consumed goods/fixed assets · *გახარჯული საქონლის/ ძ.ს. სრული რაოდენობა* |
| `production.materials[].expenses[]` | collection | Collection of expenses charged for these produced goods/fixed assets, consisting of: · *მოცემული ნაწარმოები საქონელი/ძ.ს. სთვის დარიცხული ხარჯების კოლექია შედგება:* |
| `production.materials[].expenses[].type` | byte | Type of expense charged to production (0 - provided services, 1 - salaries, 2 - depreciation) · *წარმოებაზე დარიცხული ხარჯის ტიპი (0 - გაწეული მომსახურებები, 1 - ხელფასები , 2 - ცვეთები)* |
| `production.materials[].expenses[].amount` | decimal | Amount of the charged expense · *დარიცხული ხარჯის ოდენობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getDocAutoService

Auto service request · *ავტოსერვისის განაცხადი*

Fetch an auto service request · *ავტოსერვისის განაცხადის წამოღება*

**GET** `api/operation/getDocAutoService/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
    "autoservice": { 
        "id": 6563, 
        "date": "2019-05-16T15:28:19", 
        "num_pfx": "", 
        "num": 8624, 
        "waybill_num": "0418925004", 
        "purpose": "განაცხადი №", 
        "amount": 780.0, 
        "currency": "GEL", 
        "rate": 1.0, 
        "store": 2, 
        "customer": 1, 
        "user": 1, 
        "staff": 1, 
        "project": 2, 
        "is_vat": true, 
        "make_entry": true, 
        "pay_type": 2, 
        "w_type": 2, 
        "t_type": 1, 
        "t_payer": 1, 
        "w_cost": 0.0, 
        "foreign": false, 
        "drv_name": "რამინ ხოზრევანიძე", 
        "tr_start": "მცხეთის რაიონი, სოფ. წიწამური", 
        "tr_end": "მცხეთის რაიონი, სოფ. წიწამური", 
        "driver_id": "61006038420", 
        "car_num": "iu100iu", 
        "tr_text": "", 
        "sender": "", 
        "reciever": "", 
        "comment": "", 
        "mileage": 946176, 
        "in_date": "2019-05-15T15:28:19", 
        "box": 0, 
        "car": 18023, 
        "overlap_type": 0, 
        "overlap_amount": 0.0, 
        "add_fields": [{ 
            "field": "usr_column_510", 
            "value": "" 
        }, { 
            "field": "usr_column_527", 
            "value": "" 
        }, { 
            "field": "usr_column_528", 
            "value": "" 
        }], 
        "products": [{ 
            "id": 29, 
            "sub_id": 1, 
            "price": 4.5, 
            "quantity": 120.0 
        }, { 
            "id": 28, 
            "sub_id": 0, 
            "price": 20.0, 
            "quantity": 12.0 
        }], 
        "services": [] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `autoservice` | object | The auto service request, consisting of: · *ავტოსერვისის განაცხადია რომელიც შედგება:* |
| `autoservice.id` | int | Document id · *დოკუმენტის id* |
| `autoservice.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `autoservice.num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `autoservice.num` | long | Document number · *დოკუმენტის ნომერი* |
| `autoservice.waybill_num` | string | Waybill number (RS - Revenue Service) · *ზედნადების ნომერი (RS)* |
| `autoservice.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `autoservice.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `autoservice.currency` | string | Currency code · *ვალუტის კოდი* |
| `autoservice.rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `autoservice.store` | int | Store (warehouse) Id · *საწყობის Id* |
| `autoservice.customer` | int | Customer Id · *მყიდველის Id* |
| `autoservice.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `autoservice.staff` | int | Staff member Id · *თანამშრომლის Id* |
| `autoservice.project` | int | Project Id · *პროექტის Id* |
| `autoservice.is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `autoservice.make_entry` | bool | Accounting entry status · *ბუღალტრული გატარების სტატუსი* |
| `autoservice.pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `autoservice.w_type` | byte | Waybill type (2 - with transportation, 3 - without transportation) · *ზედნადების ტიპი (2 - ტრანსპორტირებით, 3 - ტრანსპორტირების გარეშე)* |
| `autoservice.t_type` | byte | Transportation type (1 - road, 2 - rail, 3 - air, 4 - other, 6 - foreign road, 7 - carrier road) · *ტრანსპორტირების ტიპი (1 - საავტომობილო, 2 - სარკინიგზო, 3 - საავიაციო, 4 - სხვა, 6 - საავტომობილო უცხო ქვეყნის, 7 - გადამზიდავი საავტომობილო)* |
| `autoservice.t_payer` | byte | Payer of the transportation cost (1 - buyer, 2 - seller) · *ტრანსპორტირების ღირებულების გადამხდელი (1 - მყიდველი, 2 - გამყიდველი)* |
| `autoservice.w_cost` | decimal | Transportation cost · *ტრანსპორტირების ხარჯი* |
| `autoservice.foreign` | bool | Foreign citizen · *უცხო ქვეყნის მოქალაქე* |
| `autoservice.drv_name` | string | Driver's first and last name · *მძღოლის სახელი, გვარი* |
| `autoservice.tr_start` | string | Place where transportation starts · *ტრანსპორტირების დაწყების ადგილი* |
| `autoservice.tr_end` | string | Place where transportation ends · *ტრანსპორტირების დასრულების ადგილი* |
| `autoservice.driver_id` | string | Driver's personal number · *მძღოლის პირადი ნომერი* |
| `autoservice.car_num` | string | Vehicle registration number · *ავტომობილის ნომერი* |
| `autoservice.tr_text` | string | Trailer/carrier (if the transportation type is 7, the carrier's identification code; if the transportation type is 4, the transportation form; for road transport, the trailer number if there is one) · *მისაბმელი/გადამზიდავი (თუ ტრანსპორტირების ტიპი არის 7, გადამზიდავის საიდენტიფიკაციო კოდი, თუ ტრანსპორტირების ტიპი არის 4 - ტრანსპორტირების ფორმა, ხოლო საავტომობილოს შემთხვევაში - მისაბმელის ნომერი ასეთის არსებობის შემთხვევაში)* |
| `autoservice.sender` | string | Deliverer · *ჩამბარებელი* |
| `autoservice.reciever` | string | Recipient · *მიმღები* |
| `autoservice.comment` | string | Comment · *კომენტარი* |
| `autoservice.mileage` | double | Mileage · *გარბენი* |
| `autoservice.in_date` | datetime | Receipt (incoming) date · *შემოსვლის თარიღი* |
| `autoservice.box` | int | Box (bay) Id · *ბოქსის Id* |
| `autoservice.car` | int | Vehicle Id · *ავტომობილის Id* |
| `autoservice.overlap_type` | byte | Advance/VAT offset (0 - offset neither, 1 - offset the advance, VAT partially, 2 - offset the advance, VAT fully, 3 - offset the advance, not VAT) · *ავანსი/დღგ-ს გადახურვა (0 - არ გადაიხუროს არც ერთი, 1 - ავანსი გადაიხუროს, დღგ - ნაწილობრივ, 2 - ავანსი გადაიხუროს, დღგ - სრულად, 3 - ავანსი გადაიხუროს, დღგ - არა) * |
| `autoservice.overlap_amount` | decimal | Offset VAT amount · *გადახურული დღგ- ს თანხა* |
| `autoservice.add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `autoservice.add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `autoservice.add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `autoservice.products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `autoservice.products[].id` | int | Product Id · *საქონლის Id* |
| `autoservice.products[].sub_id` | int | Product sub-code Id · *საქონლის ქვე-კოდის Id* |
| `autoservice.products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `autoservice.products[].price` | decimal | Unit price of the product · *საქონლის ერთეულის ფასი* |
| `autoservice.services[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `autoservice.services[].id` | int | Provided service Id · *გაწეული მომსახურების Id* |
| `autoservice.services[].quantity` | decimal | Quantity of the provided service · *გაწეული მომსახურების რაოდენობა* |
| `autoservice.services[].price` | decimal | Unit price of the provided service · *გაწეული მომსახურების ერთეულის ფასი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getDocAdvProduction

Complex production/disassembly · *რთული წარმოება/დაშლა*

Fetch a complex production/disassembly of goods · *საქონლის რთული წარმოების/დაშლის წამოღება*

**GET** `api/operation/getDocAdvProduction/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
  "adv_production": { 
    "id": 36095, 
    "date": "2026-06-25T14:17:45", 
    "num_pfx": "", 
    "num": 3, 
    "purpose": "რთული წარმოება/დაშლა", 
    "amount": 1961.17, 
    "portion": 2, 
    "store": 1, 
    "user": 1, 
    "make_entry": true, 
    "materials": [{ 
        "id": 4, 
        "quantity": 3 
      }], 
    "products": [{ 
        "id": 106, 
        "quantity": 1, 
        "cost_percent": 40 
      }, { 
        "id": 105, 
        "quantity": 2, 
        "cost_percent": 60 
      }]}, 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `adv_production` | object | The complex production/disassembly of goods, consisting of: · *საქონლის რთული წარმოების/დაშლაა რომელიც შედგება:* |
| `adv_production.id` | int | Document id · *დოკუმენტის id* |
| `adv_production.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `adv_production.num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `adv_production.num` | long | Document number · *დოკუმენტის ნომერი* |
| `adv_production.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `adv_production.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `adv_production.portion` | decimal | Quantity · *რაოდენობა* |
| `adv_production.store` | int | Store (warehouse) Id · *საწყობის Id* |
| `adv_production.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `adv_production.make_entry` | bool | Accounting entry status · *ბუღალტრული გატარების სტატუსი* |
| `adv_production.materials[]` | collection | Collection of consumed/disassembled goods consisting of: · *გახარჯული/დაშლილი საქონლის კოლექცია შედგება:* |
| `adv_production.materials[].id` | int | Id of the consumed/disassembled goods · *გახარჯული/დაშლილი საქონლის Id* |
| `adv_production.materials[].quantity` | decimal | Quantity of consumed/disassembled goods · *გახარჯული/დაშლილი საქონლის რაოდენობა* |
| `adv_production.products[]` | collection | Collection of produced products consisting of: · *ნაწარმოები საქონლის კოლექცია შედგება:* |
| `adv_production.products[].id` | int | Id of the produced product / fixed asset · *ნაწარმოები საქონლის/ ძ.ს. Id* |
| `adv_production.products[].quantity` | decimal | Quantity of produced goods, cost_percent - the percentage of cost price from the goods being disassembled attributed to the produced goods · *ნაწარმოები საქონლის რაოდენობა, cost_percent - დასაშლელი საქონლიდან თ/ღ პროცენტული მნიშვნელობა ნაწარმოები საქონლისთვის* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `cost_percent` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---
