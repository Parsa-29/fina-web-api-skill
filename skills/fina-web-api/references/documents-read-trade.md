# Reading documents — sales, orders and returns

9 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getDocTypes`](#getdoctypes) | GET | `api/operation/getDocTypes` | List of operations |
| [`getDocAdditionalFields`](#getdocadditionalfields) | GET | `api/operation/getDocAdditionalFields/{type}` | Description of the document's additional fields |
| [`getDocDiscountCard`](#getdocdiscountcard) | GET | `api/operation/getDocDiscountCard/{id}` | Issued discount card |
| [`getDocCustomerOrder`](#getdoccustomerorder) | GET | `api/operation/getDocCustomerOrder/{id}` | Order received from a customer |
| [`getDocProductOut`](#getdocproductout) | GET | `api/operation/getDocProductOut/{id}` | Goods sale |
| [`getDocProductOutSingle`](#getdocproductoutsingle) | GET | `api/operation/getDocProductOutSingle/{id}` | Retail sale |
| [`getDocInventoryOut`](#getdocinventoryout) | GET | `api/operation/getDocInventoryOut/{id}` | Fixed asset sale |
| [`getDocCustomerReturn`](#getdoccustomerreturn) | GET | `api/operation/getDocCustomerReturn/{id}` | Return from a customer |
| [`getDocCustomerInventoryReturn`](#getdoccustomerinventoryreturn) | GET | `api/operation/getDocCustomerInventoryReturn/{id}` | Return of a fixed asset from a customer |

---

### getDocTypes

List of operations · *ოპერაციების სია*

Fetch the description of operations available in FINA · *FINA ში არსებული ოპერაციების აღწერის წამოღება*

**GET** `api/operation/getDocTypes`

**Response**

```json
{ 
    "doc_types": [{ 
        "type": 1, 
        "name": "ავანსის გადახურვა", 
        "api_supported": false 
    }, { 
        "type": 8, 
        "name": "შეკვეთა მყიდველისგან", 
        "api_supported": true 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `doc_types[]` | collection | Collection describing the operations available in FINA consisting of: · *FINA ში არსებული ოპერაციების აღწერის კოლექციაა რომელიც შედგება:* |
| `doc_types[].type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `doc_types[].name` | string | Document (operation) name · *დოკუმენტის (ოპერაციის) დასახელება* |
| `doc_types[].api_supported` | bool | Status (whether it is supported in the API) · *სტატუსი (მხარდაჭერილია თუ არა API ში)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getDocAdditionalFields

Description of the document's additional fields · *დოკუმენტის დამატებითი ველების აღწერა*

Fetch the description of the document's additional fields · *დოკუმენტის დამატებითი ველების აღწერის წამოღება*

**GET** `api/operation/getDocAdditionalFields/{type}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `type` | int | The corresponding document type · *წარმოადგენს შესაბამის დოკუმენტის ტიპს* |

**Response**

```json
{ 
    "fields": [{ 
        "name": "usr_column_511", 
        "header": "ლოკაცია" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `fields.name` | string | Name of the document's additional field in the database (Column) · *დოკუმენტის დამატებითი ველის დასახელება მონაცემთა ბაზაში (Column)* |
| `fields.header` | string | Name given by the user to the additional field · *მომხმარებლის მიერ დამატებითი ველისთვის დარქმეული სახელი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `fields` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---

### getDocDiscountCard

Issued discount card · *გაცემული ფასდაკლების ბარათი*

Fetch an issued discount card · *გაცემული ფასდაკლების ბარათის წამოღება*

**GET** `api/operation/getDocDiscountCard/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამის ოპერაციის Id-ს* |

**Response**

```json
{ 
    "discount_card": { 
        "id": 8733, 
        "date": "2019-11-08T18:00:00", 
        "num_pfx": "", 
        "num": 15, 
        "purpose": "ფასდაკლების ბარათის გაცემა", 
        "amount": 823.44, 
        "store": 1, 
        "customer": 31, 
        "user": 1, 
        "staff": 0, 
        "card_code": "2311", 
        "discount_id": 2, 
        "status": true, 
        "ref_operatons": [8737, 8738] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `discount_card` | object | The issued discount card, consisting of: · *გაცემული ფასდაკლების ბარათია რომელიც შედგება:* |
| `discount_card.id` | int | Operation (card) id · *ოპერაციის (ბარათის) id* |
| `discount_card.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `discount_card.num_pfx` | string | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `discount_card.num` | long | Document number · *დოკუმენტის ნომერი* |
| `discount_card.purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `discount_card.amount` | decimal | Amount accumulated by the customer (sum of the transactions in which this card participated) · *მყიდველის მიერ დაგროვილი თანხა (ტრანსაზციების თანხის ჯამი, რომელშიც აღნიშნული ბარათი მონაწილეობდა)* |
| `discount_card.store_id` | int | Id of the store from which the card was issued · *საწყობის id რომლიდანაც მოხდა ბარათის გაცემა* |
| `discount_card.customer_id` | int | Customer id · *მყიდველის id* |
| `discount_card.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `discount_card.staff_id` | int | Staff member id · *თანამშრომლის id* |
| `discount_card.card_code` | string | Card code · *ბარათის კოდი* |
| `discount_card.discount_id` | int | Discount id · *ფასდაკლების id* |
| `discount_card.status` | bool | Card status (whether it is active) · *ბარათის სტატუსი (აქტიურია თუ არა)* |
| `discount_card.ref_operatons` | int[] | Operations in which this card participated · *ოპერაციები რომელშიც მონაწილეობდა აღნიშნული ბარათი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `customer`, `staff`, `store` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `customer_id`, `staff_id`, `store_id` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getDocCustomerOrder

Order received from a customer · *მყიდველისგან მიღებული შეკვეთა*

Fetch an order received from a customer · *მყიდველისგან მიღებული შეკვეთის წამოღება*

**GET** `api/operation/getDocCustomerOrder/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
    "customer_order": { 
        "id": 4165, 
        "date": "2018-12-03T11:50:45.517", 
        "num_pfx": "t", 
        "num": 8, 
        "purpose": "შეკვეთა მყიდველისგან № 8", 
        "amount": 4.58, 
        "currency": "USD", 
        "rate": 2.6744, 
        "store": 1, 
        "customer": 1, 
        "user": 1, 
        "staff": 3, 
        "project": 1, 
        "is_vat": true, 
        "pay_type": 1, 
        "tr_start": "", 
        "tr_end": "", 
        "reserved": true, 
        "order_status": 1, 
        "add_fields": [{ 
            "field": "usr_column_511", 
            "value": "41.710456, 44.769520" 
        }], 
        "products": [{ 
            "id": 2, 
            "sub_id": 1, 
            "price": 0.93, 
            "quantity": 2 
        }, { 
            "id": 1, 
            "sub_id": 0, 
            "price": 2.71, 
            "quantity": 1 
        }], 
        "services": [] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `customer_order` | object | The order received from a customer, consisting of: · *მყიდველისგან მიღებული შეკვეთაა რომელიც შედგება:* |
| `customer_order.id` | int | Document id · *დოკუმენტის id* |
| `customer_order.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `customer_order.num_pfx` | string | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `customer_order.num` | long | Document number · *დოკუმენტის ნომერი* |
| `customer_order.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `customer_order.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `customer_order.currency` | string | Currency code · *ვალუტის კოდი* |
| `customer_order.rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `customer_order.store` | int | Store (warehouse) Id · *საწყობის Id* |
| `customer_order.customer` | int | Customer Id · *მყიდველის Id* |
| `customer_order.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `customer_order.staff` | int | Staff member Id · *თანამშრომლის Id* |
| `customer_order.project` | int | Project Id · *პროექტის Id* |
| `customer_order.is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `customer_order.pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `customer_order.tr_start` | string | Place where transportation starts · *ტრანსპორტირების დაწყების ადგილი* |
| `customer_order.tr_end` | string | Place where transportation ends · *ტრანსპორტირების დასრულების ადგილი* |
| `customer_order.reserved` | bool | Reservation status · *რეზერვაციის სტატუსი* |
| `customer_order.order_status` | byte | Order status (1 - active, 2 - received, 3 - cancelled) · *შეკვეთის სტატუსი (1 - აქტიური, 2 - მიღებული, 3 - გაუქმებული)* |
| `customer_order.add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `customer_order.add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `customer_order.add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `customer_order.products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `customer_order.products[].id` | int | Product Id · *საქონლის Id* |
| `customer_order.products[].sub_id` | int | Product sub-code Id · *საქონლის ქვე-კოდის Id* |
| `customer_order.products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `customer_order.products[].price` | decimal | Unit price of the product · *საქონლის ერთეულის ფასი* |
| `customer_order.services[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `customer_order.services[].id` | int | Provided service Id · *გაწეული მომსახურების Id* |
| `customer_order.services[].quantity` | decimal | Quantity of the provided service · *გაწეული მომსახურების რაოდენობა* |
| `customer_order.services[].price` | decimal | Unit price of the provided service · *გაწეული მომსახურების ერთეულის ფასი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getDocProductOut

Goods sale · *საქონლის რეალიზაცია*

Fetch a goods sale · *საქონლის რეალიზაციის წამოღება*

**GET** `api/operation/getDocProductOut/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
    "product_out": { 
        "id": 6563, 
        "date": "2019-05-16T15:28:19", 
        "num_pfx": "", 
        "num": 8624, 
        "waybill_num": "0418925004", 
        "purpose": "საქონლის  გაყიდვა №", 
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
        "price_type": 3, 
        "w_type": 2, 
        "t_type": 1, 
        "t_payer": 1, 
        "w_cost": 0.0, 
        "foreign": false, 
        "drv_name": "რამინ ხოზრევანიძე", 
        "tr_start": "ქ.ქუთაისი / \"+1\"¿ს ბაზარი eee", 
        "tr_end": "წერეტლიე4", 
        "driver_id": "61006038420", 
        "car_num": "iu100iu", 
        "tr_text": "", 
        "sender": "", 
        "reciever": "", 
        "comment": "", 
        "overlap_type": 0, 
        "overlap_amount": 0.0, 
        "check_status": true, 
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
| `product_out` | object | The goods sale, consisting of: · *საქონლის რეალიზაციაა რომელიც შედგება:* |
| `product_out.id` | int | Document id · *დოკუმენტის id* |
| `product_out.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `product_out.num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `product_out.num` | long | Document number · *დოკუმენტის ნომერი* |
| `product_out.waybill_num` | string | Waybill number (RS - Revenue Service) · *ზედნადების ნომერი (RS)* |
| `product_out.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `product_out.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `product_out.currency` | string | Currency code · *ვალუტის კოდი* |
| `product_out.rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `product_out.store` | int | Store (warehouse) Id · *საწყობის Id* |
| `product_out.customer` | int | Customer Id · *მყიდველის Id* |
| `product_out.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `product_out.staff` | int | Staff member Id · *თანამშრომლის Id* |
| `product_out.project` | int | Project Id · *პროექტის Id* |
| `product_out.is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `product_out.make_entry` | bool | Accounting entry status · *ბუღალტრული გატარების სტატუსი* |
| `product_out.pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `product_out.price_type` | int | Price type Id · *ფასის ტიპის Id* |
| `product_out.w_type` | byte | Waybill type (2 - with transportation, 3 - without transportation) · *ზედნადების ტიპი (2 - ტრანსპორტირებით, 3 - ტრანსპორტირების გარეშე)* |
| `product_out.t_type` | byte | Transportation type (1 - road, 2 - rail, 3 - air, 4 - other, 6 - foreign road, 7 - carrier road) · *ტრანსპორტირების ტიპი (1 - საავტომობილო, 2 - სარკინიგზო, 3 - საავიაციო, 4 - სხვა, 6 - საავტომობილო უცხო ქვეყნის, 7 - გადამზიდავი საავტომობილო)* |
| `product_out.t_payer` | byte | Payer of the transportation cost (1 - buyer, 2 - seller) · *ტრანსპორტირების ღირებულების გადამხდელი (1 - მყიდველი, 2 - გამყიდველი)* |
| `product_out.w_cost` | decimal | Transportation cost · *ტრანსპორტირების ხარჯი* |
| `product_out.foreign` | bool | Foreign citizen · *უცხო ქვეყნის მოქალაქე* |
| `product_out.drv_name` | string | Driver's first and last name · *მძღოლის სახელი, გვარი* |
| `product_out.tr_start` | string | Place where transportation starts · *ტრანსპორტირების დაწყების ადგილი* |
| `product_out.tr_end` | string | Place where transportation ends · *ტრანსპორტირების დასრულების ადგილი* |
| `product_out.driver_id` | string | Driver's personal number · *მძღოლის პირადი ნომერი* |
| `product_out.car_num` | string | Vehicle registration number · *ავტომობილის ნომერი* |
| `product_out.tr_text` | string | Trailer/carrier (if the transportation type is 7, the carrier's identification code; if the transportation type is 4, the transportation form; for road transport, the trailer number if there is one) · *მისაბმელი/გადამზიდავი (თუ ტრანსპორტირების ტიპი არის 7, გადამზიდავის საიდენტიფიკაციო კოდი, თუ ტრანსპორტირების ტიპი არის 4 - ტრანსპორტირების ფორმა, ხოლო საავტომობილოს შემთხვევაში - მისაბმელის ნომერი ასეთის არსებობის შემთხვევაში)* |
| `product_out.sender` | string | Deliverer · *ჩამბარებელი* |
| `product_out.reciever` | string | Recipient · *მიმღები* |
| `product_out.comment` | string | Comment · *კომენტარი* |
| `product_out.overlap_type` | byte | Advance/VAT offset (0 - offset neither, 1 - offset the advance, VAT partially, 2 - offset the advance, VAT fully, 3 - offset the advance, not VAT) · *ავანსი/დღგ-ს გადახურვა (0 - არ გადაიხუროს არც ერთი, 1 - ავანსი გადაიხუროს, დღგ - ნაწილობრივ, 2 - ავანსი გადაიხუროს, დღგ - სრულად, 3 - ავანსი გადაიხუროს, დღგ - არა) * |
| `product_out.overlap_amount` | decimal | Offset VAT amount · *გადახურული დღგ- ს თანხა* |
| `product_out.check_status` | bool | Check status · *შემოწმების სტატუსი* |
| `product_out.add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `product_out.add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `product_out.add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `product_out.products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `product_out.products[].id` | int | Product Id · *საქონლის Id* |
| `product_out.products[].sub_id` | int | Product sub-code Id · *საქონლის ქვე-კოდის Id* |
| `product_out.products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `product_out.products[].price` | decimal | Unit price of the product · *საქონლის ერთეულის ფასი* |
| `product_out.services[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `product_out.services[].id` | int | Provided service Id · *გაწეული მომსახურების Id* |
| `product_out.services[].quantity` | decimal | Quantity of the provided service · *გაწეული მომსახურების რაოდენობა* |
| `product_out.services[].price` | decimal | Unit price of the provided service · *გაწეული მომსახურების ერთეულის ფასი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getDocProductOutSingle

Retail sale · *საცალო რეალიზაცია*

Fetch a retail goods sale · *საქონლის საცალო რეალიზაციის წამოღება*

**GET** `api/operation/getDocProductOutSingle/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
    "product_out_single": { 
        "id": 16902, 
        "date": "2020-08-26T23:59:58", 
        "num_pfx": "", 
        "num": 20, 
        "purpose": "დაჯგუფებული საცალო გაყიდვა staff1", 
        "amount": 11.0, 
        "currency": "GEL", 
        "rate": 1.0, 
        "store": 1, 
        "user": 1, 
        "staff": 2, 
        "project": 1, 
        "is_vat": true, 
        "make_entry": true, 
        "pay_type": 6, 
        "add_fields": [], 
        "products": [{ 
            "id": 1, 
            "sub_id": 0, 
            "price": 5.0, 
            "quantity": 1.0 
        }, { 
            "id": 1, 
            "sub_id": 0, 
            "price": 6.0, 
            "quantity": 1.0 
        }] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `product_out_single` | object | The retail goods sale, consisting of: · *საქონლის საცალო რეალიზაციაა რომელიც შედგება:* |
| `product_out_single.id` | int | Document id · *დოკუმენტის id* |
| `product_out_single.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `product_out_single.num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `product_out_single.num` | long | Document number · *დოკუმენტის ნომერი* |
| `product_out_single.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `product_out_single.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `product_out_single.currency` | string | Currency code · *ვალუტის კოდი* |
| `product_out_single.rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `product_out_single.store` | int | Store (warehouse) Id · *საწყობის Id* |
| `product_out_single.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `product_out_single.staff` | int | Staff member Id · *თანამშრომლის Id* |
| `product_out_single.project` | int | Project Id · *პროექტის Id* |
| `product_out_single.is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `product_out_single.make_entry` | bool | Accounting entry status · *ბუღალტრული გატარების სტატუსი* |
| `product_out_single.pay_type` | byte | Payment type (0 - cash, 1 - cashless, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 6 - სხვა)* |
| `product_out_single.add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `product_out_single.add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `product_out_single.add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `product_out_single.products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `product_out_single.products[].id` | int | Product Id · *საქონლის Id* |
| `product_out_single.products[].sub_id` | int | Product sub-code Id · *საქონლის ქვე-კოდის Id* |
| `product_out_single.products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `product_out_single.products[].price` | decimal | Unit price of the product · *საქონლის ერთეულის ფასი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `field`, `value` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getDocInventoryOut

Fixed asset sale · *ძირითადი საშუალების რეალიზაცია*

Fetch a fixed asset sale · *ძირითადი საშუალების რეალიზაციის წამოღება*

**GET** `api/operation/getDocInventoryOut/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
    "inventory_out": { 
        "id": 6536, 
        "date": "2019-04-23T15:07:53", 
        "num_pfx": "", 
        "num": 23, 
        "waybill_num": null, 
        "purpose": "ძირითადი საშუალების გაყიდვა № 23", 
        "amount": 114.0, 
        "currency": "GEL", 
        "rate": 1.0, 
        "store": 2, 
        "customer": 8, 
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
        "drv_name": "", 
        "tr_start": "", 
        "tr_end": "empty", 
        "driver_id": "", 
        "car_num": "", 
        "tr_text": "", 
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
        "inventories": [{ 
            "id": 24, 
            "price": 114.0, 
            "self_cost": 5000.0, 
            "quantity": 1.0 
        }] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `inventory_out` | object | The fixed asset sale, consisting of: · *ძირითადი საშუალების რეალიზაციაა რომელიც შედგება:* |
| `inventory_out.id` | int | Document id · *დოკუმენტის id* |
| `inventory_out.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `inventory_out.num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `inventory_out.num` | long | Document number · *დოკუმენტის ნომერი* |
| `inventory_out.waybill_num` | string | Waybill number (RS - Revenue Service) · *ზედნადების ნომერი (RS)* |
| `inventory_out.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `inventory_out.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `inventory_out.currency` | string | Currency code · *ვალუტის კოდი* |
| `inventory_out.rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `inventory_out.store` | int | Store (warehouse) Id · *საწყობის Id* |
| `inventory_out.customer` | int | Customer Id · *მყიდველის Id* |
| `inventory_out.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `inventory_out.staff` | int | Staff member Id · *თანამშრომლის Id* |
| `inventory_out.project` | int | Project Id · *პროექტის Id* |
| `inventory_out.is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `inventory_out.make_entry` | bool | Accounting entry status · *ბუღალტრული გატარების სტატუსი* |
| `inventory_out.pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `inventory_out.w_type` | byte | Waybill type (2 - with transportation, 3 - without transportation) · *ზედნადების ტიპი (2 - ტრანსპორტირებით, 3 - ტრანსპორტირების გარეშე)* |
| `inventory_out.t_type` | byte | Transportation type (1 - road, 2 - rail, 3 - air, 4 - other, 6 - foreign road, 7 - carrier road) · *ტრანსპორტირების ტიპი (1 - საავტომობილო, 2 - სარკინიგზო, 3 - საავიაციო, 4 - სხვა, 6 - საავტომობილო უცხო ქვეყნის, 7 - გადამზიდავი საავტომობილო)* |
| `inventory_out.t_payer` | byte | Payer of the transportation cost (1 - buyer, 2 - seller) · *ტრანსპორტირების ღირებულების გადამხდელი (1 - მყიდველი, 2 - გამყიდველი)* |
| `inventory_out.w_cost` | decimal | Transportation cost · *ტრანსპორტირების ხარჯი* |
| `inventory_out.foreign` | bool | Foreign citizen · *უცხო ქვეყნის მოქალაქე* |
| `inventory_out.drv_name` | string | Driver's first and last name · *მძღოლის სახელი, გვარი* |
| `inventory_out.tr_start` | string | Place where transportation starts · *ტრანსპორტირების დაწყების ადგილი* |
| `inventory_out.tr_end` | string | Place where transportation ends · *ტრანსპორტირების დასრულების ადგილი* |
| `inventory_out.driver_id` | string | Driver's personal number · *მძღოლის პირადი ნომერი* |
| `inventory_out.car_num` | string | Vehicle registration number · *ავტომობილის ნომერი* |
| `inventory_out.tr_text` | string | Trailer/carrier (if the transportation type is 7, the carrier's identification code; if the transportation type is 4, the transportation form; for road transport, the trailer number if there is one) · *მისაბმელი/გადამზიდავი (თუ ტრანსპორტირების ტიპი არის 7, გადამზიდავის საიდენტიფიკაციო კოდი, თუ ტრანსპორტირების ტიპი არის 4 - ტრანსპორტირების ფორმა, ხოლო საავტომობილოს შემთხვევაში - მისაბმელის ნომერი ასეთის არსებობის შემთხვევაში)* |
| `inventory_out.add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `inventory_out.add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `inventory_out.add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `inventory_out.inventories[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `inventory_out.inventories[].id` | int | Fixed asset Id · *ძირითადი საშუალების Id* |
| `inventory_out.inventories[].quantity` | decimal | Fixed asset quantity · *ძირითადი საშუალების რაოდენობა* |
| `inventory_out.inventories[].price` | decimal | Unit price of the fixed asset · *ძირითადი საშუალების ერთეულის ფასი* |
| `inventory_out.inventories[].self_cost` | decimal | Cost price of the fixed asset unit · *ძირითადი საშუალების ერთეულის თვითღირებულება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getDocCustomerReturn

Return from a customer · *დაბრუნება მყიდველისგან*

Fetch goods returned from a customer · *მყიდველისგან მობრუნებული საქონლის წამოღება*

**GET** `api/operation/getDocCustomerReturn/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
    "customer_return": { 
        "id": 6552, 
        "date": "2019-05-01T14:25:00", 
        "num_pfx": "", 
        "num": 10, 
        "waybill_num": "0526302888", 
        "purpose": "dabruneba", 
        "amount": 65.7, 
        "currency": "GEL", 
        "rate": 1.0, 
        "store": 1, 
        "customer": 8, 
        "user": 2, 
        "staff": 3, 
        "project": 2, 
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
            "price": 35.7, 
            "self_cost": 1.69491525423729, 
            "quantity": 1.0, 
            "out_id": 6547 
        }, { 
            "id": 3, 
            "sub_id": 0, 
            "price": 10.0, 
            "self_cost": 8.47457627118644, 
            "quantity": 3.0, 
            "out_id": 0 
        }] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `customer_return` | object | The return from a customer, consisting of: · *მყიდველისგან დაბრუნებაა რომელიც შედგება:* |
| `customer_return.id` | int | Document id · *დოკუმენტის id* |
| `customer_return.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `customer_return.num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `customer_return.num` | long | Document number · *დოკუმენტის ნომერი* |
| `customer_return.waybill_num` | string | Waybill number (RS - Revenue Service) · *ზედნადების ნომერი (RS)* |
| `customer_return.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `customer_return.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `customer_return.currency` | string | Currency code · *ვალუტის კოდი* |
| `customer_return.rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `customer_return.store` | int | Store (warehouse) Id · *საწყობის Id* |
| `customer_return.customer` | int | Customer Id · *მყიდველის Id* |
| `customer_return.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `customer_return.staff` | int | Staff member Id · *თანამშრომლის Id* |
| `customer_return.project` | int | Project Id · *პროექტის Id* |
| `customer_return.is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `customer_return.make_entry` | bool | Accounting entry status · *ბუღალტრული გატარების სტატუსი* |
| `customer_return.pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `customer_return.t_type` | byte | Transportation type (1 - road, 2 - rail, 3 - air, 4 - other, 6 - foreign road, 7 - carrier road) · *ტრანსპორტირების ტიპი (1 - საავტომობილო, 2 - სარკინიგზო, 3 - საავიაციო, 4 - სხვა, 6 - საავტომობილო უცხო ქვეყნის, 7 - გადამზიდავი საავტომობილო)* |
| `customer_return.t_payer` | byte | Payer of the transportation cost (1 - buyer, 2 - seller) · *ტრანსპორტირების ღირებულების გადამხდელი (1 - მყიდველი, 2 - გამყიდველი)* |
| `customer_return.w_cost` | decimal | Transportation cost · *ტრანსპორტირების ხარჯი* |
| `customer_return.foreign` | bool | Foreign citizen · *უცხო ქვეყნის მოქალაქე* |
| `customer_return.drv_name` | string | Driver's first and last name · *მძღოლის სახელი, გვარი* |
| `customer_return.tr_start` | string | Place where transportation starts · *ტრანსპორტირების დაწყების ადგილი* |
| `customer_return.tr_end` | string | Place where transportation ends · *ტრანსპორტირების დასრულების ადგილი* |
| `customer_return.driver_id` | string | Driver's personal number · *მძღოლის პირადი ნომერი* |
| `customer_return.car_num` | string | Vehicle registration number · *ავტომობილის ნომერი* |
| `customer_return.tr_text` | string | Trailer/carrier (if the transportation type is 7, the carrier's identification code; if the transportation type is 4, the transportation form; for road transport, the trailer number if there is one) · *მისაბმელი/გადამზიდავი (თუ ტრანსპორტირების ტიპი არის 7, გადამზიდავის საიდენტიფიკაციო კოდი, თუ ტრანსპორტირების ტიპი არის 4 - ტრანსპორტირების ფორმა, ხოლო საავტომობილოს შემთხვევაში - მისაბმელის ნომერი ასეთის არსებობის შემთხვევაში)* |
| `customer_return.products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `customer_return.products[].id` | int | Product Id · *საქონლის Id* |
| `customer_return.products[].sub_id` | int | Product sub-code Id · *საქონლის ქვე-კოდის Id* |
| `customer_return.products[].price` | decimal | Unit price of the product · *საქონლის ერთეულის ფასი* |
| `customer_return.products[].self_cost` | decimal | Cost price of the product unit (on return) · *საქონლის ერთეულის (დაბრუნების) თვითღირებულება* |
| `customer_return.products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `customer_return.products[].out_id` | int | Id of the sale operation being returned (which specific sale is being returned, default=0) · *გაყიდვის ოპერაციის Id (თუ რომელი გაყიდვის დაბრუნება ხდება კონკრეტულად, default=0)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getDocCustomerInventoryReturn

Return of a fixed asset from a customer · *ძირითადი საშუალების დაბრუნება მყიდველისგან*

Fetch a fixed asset returned from a customer · *მყიდველისგან მობრუნებული ძირითადი საშუალების წამოღება*

**GET** `api/operation/getDocCustomerInventoryReturn/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The Id of the corresponding operation · *წარმოადგენს შესაბამისი ოპერაციის Id-ს* |

**Response**

```json
{ 
    "customer_inventory_return": { 
        "id": 8743, 
        "date": "2019-11-12T11:24:37", 
        "num_pfx": "", 
        "num": 11, 
        "waybill_num": null, 
        "purpose": "ძირითადი საშუალების უკან დაბრუნება № 0", 
        "amount": 20.0, 
        "currency": "GEL", 
        "rate": 1.0, 
        "store": 2, 
        "customer": 30, 
        "user": 1, 
        "staff": 1, 
        "project": 2, 
        "is_vat": true, 
        "make_entry": true, 
        "pay_type": 1, 
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
        "inventories": [{ 
            "id": 34, 
            "price": 3.5, 
            "self_cost": 1.9, 
            "quantity": 2.0 
        }] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `customer_inventory_return` | object | The fixed asset return from a customer, consisting of: · *მყიდველისგან ძირ. საშ. დაბრუნებაა რომელიც შედგება:* |
| `customer_inventory_return.id` | int | Document id · *დოკუმენტის id* |
| `customer_inventory_return.date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `customer_inventory_return.num_pfx` | string[20] | Document number prefix · *დოკუმენტის ნომრის პრეფიქსი* |
| `customer_inventory_return.num` | long | Document number · *დოკუმენტის ნომერი* |
| `customer_inventory_return.waybill_num` | string | Waybill number (RS - Revenue Service) · *ზედნადების ნომერი (RS)* |
| `customer_inventory_return.purpose` | string | Document content (comment) · *დოკუმენტის შინაარსი (კომენტარი)* |
| `customer_inventory_return.amount` | decimal | Total value of the operation · *ოპერაციის ჯამური ღირებულება* |
| `customer_inventory_return.currency` | string | Currency code · *ვალუტის კოდი* |
| `customer_inventory_return.rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `customer_inventory_return.store` | int | Store (warehouse) Id · *საწყობის Id* |
| `customer_inventory_return.customer` | int | Customer Id · *მყიდველის Id* |
| `customer_inventory_return.user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `customer_inventory_return.staff` | int | Staff member Id · *თანამშრომლის Id* |
| `customer_inventory_return.project` | int | Project Id · *პროექტის Id* |
| `customer_inventory_return.is_vat` | bool | Whether it includes VAT · *დღგ-ს შეიცავს თუ არა* |
| `customer_inventory_return.make_entry` | bool | Accounting entry status · *ბუღალტრული გატარების სტატუსი* |
| `customer_inventory_return.pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `customer_inventory_return.t_type` | byte | Transportation type (1 - road, 2 - rail, 3 - air, 4 - other, 6 - foreign road, 7 - carrier road) · *ტრანსპორტირების ტიპი (1 - საავტომობილო, 2 - სარკინიგზო, 3 - საავიაციო, 4 - სხვა, 6 - საავტომობილო უცხო ქვეყნის, 7 - გადამზიდავი საავტომობილო)* |
| `customer_inventory_return.t_payer` | byte | Payer of the transportation cost (1 - buyer, 2 - seller) · *ტრანსპორტირების ღირებულების გადამხდელი (1 - მყიდველი, 2 - გამყიდველი)* |
| `customer_inventory_return.w_cost` | decimal | Transportation cost · *ტრანსპორტირების ხარჯი* |
| `customer_inventory_return.foreign` | bool | Foreign citizen · *უცხო ქვეყნის მოქალაქე* |
| `customer_inventory_return.drv_name` | string | Driver's first and last name · *მძღოლის სახელი, გვარი* |
| `customer_inventory_return.tr_start` | string | Place where transportation starts · *ტრანსპორტირების დაწყების ადგილი* |
| `customer_inventory_return.tr_end` | string | Place where transportation ends · *ტრანსპორტირების დასრულების ადგილი* |
| `customer_inventory_return.driver_id` | string | Driver's personal number · *მძღოლის პირადი ნომერი* |
| `customer_inventory_return.car_num` | string | Vehicle registration number · *ავტომობილის ნომერი* |
| `customer_inventory_return.tr_text` | string | Trailer/carrier (if the transportation type is 7, the carrier's identification code; if the transportation type is 4, the transportation form; for road transport, the trailer number if there is one) · *მისაბმელი/გადამზიდავი (თუ ტრანსპორტირების ტიპი არის 7, გადამზიდავის საიდენტიფიკაციო კოდი, თუ ტრანსპორტირების ტიპი არის 4 - ტრანსპორტირების ფორმა, ხოლო საავტომობილოს შემთხვევაში - მისაბმელის ნომერი ასეთის არსებობის შემთხვევაში)* |
| `customer_inventory_return.inventories[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `customer_inventory_return.inventories[].id` | int | Fixed asset Id · *ძირითადი საშუალების Id* |
| `customer_inventory_return.inventories[].quantity` | decimal | Fixed asset quantity · *ძირითადი საშუალების რაოდენობა* |
| `customer_inventory_return.inventories[].price` | decimal | Unit price of the fixed asset · *ძირითადი საშუალების ერთეულის ფასი* |
| `customer_inventory_return.inventories[].self_cost` | decimal | Cost price of the fixed asset unit (on return) · *ძირითადი საშუალების ერთეულის (დაბრუნების) თვითღირებულება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---
