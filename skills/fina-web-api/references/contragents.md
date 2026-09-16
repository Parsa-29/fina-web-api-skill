# Customers, vendors and their attributes

16 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getCustomersByCode`](#getcustomersbycode) | GET | `api/operation/getCustomersByCode/{code}` | Customers by identification code |
| [`getVendorsByCode`](#getvendorsbycode) | GET | `api/operation/getVendorsByCode/{code}` | Vendors by identification code |
| [`getCustomers`](#getcustomers) | GET | `api/operation/getCustomers` | Customers |
| [`getVendors`](#getvendors) | GET | `api/operation/getVendors` | Vendors |
| [`getCustomerAdditionalFields`](#getcustomeradditionalfields) | GET | `api/operation/getCustomerAdditionalFields` | Description of the customer's additional fields |
| [`getVendorAdditionalFields`](#getvendoradditionalfields) | GET | `api/operation/getVendorAdditionalFields` | Description of the vendor's additional fields |
| [`getCustomerGroups`](#getcustomergroups) | GET | `api/operation/getCustomerGroups` | Customer groups |
| [`getVendorGroups`](#getvendorgroups) | GET | `api/operation/getVendorGroups` | Vendor groups |
| [`getCustomerAddresses`](#getcustomeraddresses) | GET | `api/operation/getCustomerAddresses` | Customer addresses |
| [`getVendorAddresses`](#getvendoraddresses) | GET | `api/operation/getVendorAddresses` | Vendor addresses |
| [`getCustomerAgreements`](#getcustomeragreements) | GET | `api/operation/getCustomerAgreements` | Customer agreements |
| [`getContragentSubAccountFields`](#getcontragentsubaccountfields) | GET | `api/operation/getContragentSubAccountFields` | Description of contragent sub-account fields |
| [`getCustomerSubAccounts`](#getcustomersubaccounts) | GET | `api/operation/getCustomerSubAccounts` | Customer sub-accounts |
| [`getVendorSubAccounts`](#getvendorsubaccounts) | GET | `api/operation/getVendorSubAccounts` | Vendor sub-accounts |
| [`saveCustomer`](#savecustomer) | POST | `api/operation/saveCustomer` | Save a customer |
| [`saveVendor`](#savevendor) | POST | `api/operation/saveVendor` | Save a vendor |

---

### getCustomersByCode

Customers by identification code · *მყიდველები საიდენტ. კოდის მიხედვით*

Fetch customers by identification code · *მყიდველების წამოღება საიდენტიფიკაციო კოდის მიხედვით*

**GET** `api/operation/getCustomersByCode/{code}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `code` | string | The customer's identification code · *წარმოადგენს მყიდველის საიდენტიფიკაციო კოდს* |

**Response**

```json
{ 
    "contragents": [{ 
        "id": 1, 
        "group_id": 5, 
        "code": "12345678910", 
        "name": "სატესტო სატესტო", 
        "address": "", 
        "phone": "", 
        "email": "", 
        "is_company": true, 
        "is_resident": true, 
        "vat_type": 1, 
        "cons_period": 30, 
        "birth_date": "2018-08-21T00:00:00", 
        "marketing_promotions": true, 
        "add_fields": [{ 
            "field": "usr_column_515", 
            "value": "" 
        }] 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `contragents[]` | collection | Collection of customers consisting of: · *მყიდველების კოლექციაა რომელიც შედგება:* |
| `contragents[].id` | int | Customer Id · *მყიდველის Id* |
| `contragents[].group_id` | int | Customer group Id · *მყიდველის ჯგუფის Id* |
| `contragents[].code` | string[50] | Customer's identification code or personal number · *მყიდველის საიდენტიფიკაციო კოდი ან პირადი ნომერი* |
| `contragents[].name` | string[200] | Name · *დასახელება* |
| `contragents[].address` | string[200] | Address · *მისამართი* |
| `contragents[].tel` | string[50] | Phone number · *ტელეფონის ნომერი* |
| `contragents[].mail` | string[50] | Email · *ელ. ფოსტა* |
| `contragents[].is_company` | bool | Customer type (true - legal entity, false - natural person) · *მყიდველის ტიპი (true - იურიდიული პირი, false - ფიზიკური პირი)* |
| `contragents[].is_resident` | bool | Resident (true - local, false - foreign citizen) · *რეზიდენტი (true - ადგილობრივი, false - უცხო ქვეყნის მოქალაქე)* |
| `contragents[].vat_type` | byte | VAT type (0 - not a VAT payer, 1 - VAT payer, 2 - exempt with the right of deduction, 3 - exempt without the right of deduction) · *დღგ-ს ტიპი (0 - არ არის დღგ-ს გადამხდელი, 1 - დღგ-ს გადამხდელი, 2 - განთავისუფლებული ჩათვლის უფლებით, 3 - განთავისუფლებული ჩათვლის უფლების გარეშე)* |
| `contragents[].cons_period` | int | Consignment term (days) · *კონსიგნაციის ვადა (დღე)* |
| `contragents[].birth_date` | datetime | Date of birth · *დაბადების თარიღი* |
| `contragents[].marketing_promotions` | bool | Permission to use in marketing campaigns · *მარკეტინგულ აქციებში გამოყენების ნებართვა* |
| `contragents[].add_fields[]` | collection | Collection of the customer's additional fields, where: · *მყიდველის დამატებითი ველების კოლექცია სადაც:* |
| `contragents[].add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `contragents[].add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `email`, `phone` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `mail`, `tel` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getVendorsByCode

Vendors by identification code · *მომწოდებლები საიდენტ. კოდის მიხედვით*

Fetch vendors by identification code · *მომწოდებლების წამოღება საიდენტიფიკაციო კოდის მიხედვით*

**GET** `api/operation/getVendorsByCode/{code}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `code` | string | The vendor's identification code · *წარმოადგენს მომწოდებლის საიდენტიფიკაციო კოდს* |

**Response**

```json
{ 
    "contragents": [{ 
        "id": 2, 
        "group_id": 3, 
        "code": "00112233665", 
        "name": "X ვენდორ", 
        "address": "", 
        "phone": "", 
        "email": "", 
        "is_company": true, 
        "is_resident": true, 
        "vat_type": 1, 
        "cons_period": 30, 
        "birth_date": "2018-08-21T00:00:00", 
        "marketing_promotions": true, 
        "add_fields": [{ 
            "field": "usr_column_515", 
            "value": "" 
        }] 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `contragents[]` | collection | Collection of vendors consisting of: · *მომწოდებლების კოლექციაა რომელიც შედგება:* |
| `contragents[].id` | int | Vendor Id · *მომწოდებლის Id* |
| `contragents[].group_id` | int | Vendor group Id · *მომწოდებლის ჯგუფის Id* |
| `contragents[].code` | string[50] | Vendor's identification code or personal number · *მომწოდებლის საიდენტიფიკაციო კოდი ან პირადი ნომერი* |
| `contragents[].name` | string[200] | Name · *დასახელება* |
| `contragents[].address` | string[200] | Address · *მისამართი* |
| `contragents[].tel` | string[50] | Phone number · *ტელეფონის ნომერი* |
| `contragents[].mail` | string[50] | Email · *ელ. ფოსტა* |
| `contragents[].is_company` | bool | Vendor type (true - legal entity, false - natural person) · *მომწოდებლის ტიპი (true - იურიდიული პირი, false - ფიზიკური პირი)* |
| `contragents[].is_resident` | bool | Resident (true - local, false - foreign citizen) · *რეზიდენტი (true - ადგილობრივი, false - უცხო ქვეყნის მოქალაქე)* |
| `contragents[].vat_type` | byte | VAT type (0 - not a VAT payer, 1 - VAT payer, 2 - exempt with the right of deduction, 3 - exempt without the right of deduction) · *დღგ-ს ტიპი (0 - არ არის დღგ-ს გადამხდელი, 1 - დღგ-ს გადამხდელი, 2 - განთავისუფლებული ჩათვლის უფლებით, 3 - განთავისუფლებული ჩათვლის უფლების გარეშე)* |
| `contragents[].cons_period` | int | Consignment term (days) · *კონსიგნაციის ვადა (დღე)* |
| `contragents[].birth_date` | datetime | Date of birth · *დაბადების თარიღი* |
| `contragents[].marketing_promotions` | bool | Permission to use in marketing campaigns · *მარკეტინგულ აქციებში გამოყენების ნებართვა* |
| `contragents[].add_fields[]` | collection | Collection of the vendor's additional fields, where: · *მომწოდებლის დამატებითი ველების კოლექცია სადაც:* |
| `contragents[].add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `contragents[].add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `email`, `phone` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `mail`, `tel` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getCustomers

Customers · *მყიდველები*

Fetch customers · *მყიდველების წამოღება*

**GET** `api/operation/getCustomers`

**Response**

```json
{ 
  "contragents": [ 
    { 
      "id": 1, 
      "group_id": 5, 
      "code": "12345678910", 
      "name": "სატესტო სატესტო", 
      "address": "", 
      "phone": "", 
      "email": "", 
      "is_company": true, 
      "is_resident": true, 
      "vat_type": 1, 
      "cons_period": 30, 
      "birth_date": "2011-08-21T00:00:00", 
      "marketing_promotions": true, 
      "add_fields": [ 
        { 
          "field": "usr_column_515", 
          "value": "" 
        }] 
    }], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `contragents[]` | collection | Collection of customers consisting of: · *მყიდველების კოლექციაა რომელიც შედგება:* |
| `contragents[].id` | int | Customer Id · *მყიდველის Id* |
| `contragents[].group_id` | int | Customer group Id · *მყიდველის ჯგუფის Id* |
| `contragents[].code` | string[50] | Customer's identification code or personal number · *მყიდველის საიდენტიფიკაციო კოდი ან პირადი ნომერი* |
| `contragents[].name` | string[200] | Name · *დასახელება* |
| `contragents[].address` | string[200] | Address · *მისამართი* |
| `contragents[].tel` | string[50] | Phone number · *ტელეფონის ნომერი* |
| `contragents[].mail` | string[50] | Email · *ელ. ფოსტა* |
| `contragents[].is_company` | bool | Customer type (true - legal entity, false - natural person) · *მყიდველის ტიპი (true - იურიდიული პირი, false - ფიზიკური პირი)* |
| `contragents[].is_resident` | bool | Resident (true - local, false - foreign citizen) · *რეზიდენტი (true - ადგილობრივი, false - უცხო ქვეყნის მოქალაქე)* |
| `contragents[].vat_type` | byte | VAT type (0 - not a VAT payer, 1 - VAT payer, 2 - exempt with the right of deduction, 3 - exempt without the right of deduction) · *დღგ-ს ტიპი (0 - არ არის დღგ-ს გადამხდელი, 1 - დღგ-ს გადამხდელი, 2 - განთავისუფლებული ჩათვლის უფლებით, 3 - განთავისუფლებული ჩათვლის უფლების გარეშე)* |
| `contragents[].cons_period` | int | Consignment term (days) · *კონსიგნაციის ვადა (დღე)* |
| `contragents[].birth_date` | datetime | Date of birth · *დაბადების თარიღი* |
| `contragents[].marketing_promotions` | bool | Permission to use in marketing campaigns · *მარკეტინგულ აქციებში გამოყენების ნებართვა* |
| `contragents[].add_fields[]` | collection | Collection of the customer's additional fields, where: · *მყიდველის დამატებითი ველების კოლექცია სადაც:* |
| `contragents[].add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `contragents[].add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `email`, `phone` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `mail`, `tel` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getVendors

Vendors · *მომწოდებლები*

Fetch vendors · *მომწოდებლების წამოღება*

**GET** `api/operation/getVendors`

**Response**

```json
{ 
  "contragents": [ 
    { 
      "id": 2, 
      "group_id": 3, 
      "code": "00112233665", 
      "name": "X ვენდორ", 
      "address": "", 
      "phone": "", 
      "email": "", 
      "is_company": true, 
      "is_resident": true, 
      "vat_type": 1, 
      "cons_period": 30, 
      "birth_date": "2018-08-21T00:00:00", 
      "marketing_promotions": true, 
      "add_fields": [ 
        { 
          "field": "usr_column_515", 
          "value": "" 
        }] 
    }], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `contragents[]` | collection | Collection of vendors consisting of: · *მომწოდებლების კოლექციაა რომელიც შედგება:* |
| `contragents[].id` | int | Vendor Id · *მომწოდებლის Id* |
| `contragents[].group_id` | int | Vendor group Id · *მომწოდებლის ჯგუფის Id* |
| `contragents[].code` | string[50] | Vendor's identification code or personal number · *მომწოდებლის საიდენტიფიკაციო კოდი ან პირადი ნომერი* |
| `contragents[].name` | string[200] | Name · *დასახელება* |
| `contragents[].address` | string[200] | Address · *მისამართი* |
| `contragents[].tel` | string[50] | Phone number · *ტელეფონის ნომერი* |
| `contragents[].mail` | string[50] | Email · *ელ. ფოსტა* |
| `contragents[].is_company` | bool | Vendor type (true - legal entity, false - natural person) · *მომწოდებლის ტიპი (true - იურიდიული პირი, false - ფიზიკური პირი)* |
| `contragents[].is_resident` | bool | Resident (true - local, false - foreign citizen) · *რეზიდენტი (true - ადგილობრივი, false - უცხო ქვეყნის მოქალაქე)* |
| `contragents[].vat_type` | byte | VAT type (0 - not a VAT payer, 1 - VAT payer, 2 - exempt with the right of deduction, 3 - exempt without the right of deduction) · *დღგ-ს ტიპი (0 - არ არის დღგ-ს გადამხდელი, 1 - დღგ-ს გადამხდელი, 2 - განთავისუფლებული ჩათვლის უფლებით, 3 - განთავისუფლებული ჩათვლის უფლების გარეშე)* |
| `contragents[].cons_period` | int | Consignment term (days) · *კონსიგნაციის ვადა (დღე)* |
| `contragents[].birth_date` | datetime | Date of birth · *დაბადების თარიღი* |
| `contragents[].marketing_promotions` | bool | Permission to use in marketing campaigns · *მარკეტინგულ აქციებში გამოყენების ნებართვა* |
| `contragents[].add_fields[]` | collection | Collection of the vendor's additional fields, where: · *მომწოდებლის დამატებითი ველების კოლექცია სადაც:* |
| `contragents[].add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `contragents[].add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `email`, `phone` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `mail`, `tel` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getCustomerAdditionalFields

Description of the customer's additional fields · *მყიდველის დამატებითი ველების აღწერა*

Fetch the description of the customer's additional fields · *მყიდველის დამატებითი ველების აღწერის წამოღება*

**GET** `api/operation/getCustomerAdditionalFields`

**Response**

```json
{ 
    "fields": [{ 
        "name": "usr_column_515", 
        "header": "ლიმიტი" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `fields[]` | collection | Collection describing the customer's additional fields consisting of: · *მყიდველის დამატებითი ველების აღწერის კოლექციაა რომელიც შედგება:* |
| `fields[].name` | string | Name of the customer's additional field in the database (Column) · *მყიდველის დამატებითი ველის დასახელება მონაცემთა ბაზაში (Column)* |
| `fields[].header` | string | Name given by the user to the customer's additional field · *მომხმარებლის მიერ მყიდველის დამატებითი ველისთვის დარქმეული სახელი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getVendorAdditionalFields

Description of the vendor's additional fields · *მომწოდებლის დამატებითი ველების აღწერა*

Fetch the description of the vendor's additional fields · *მომწოდებლის დამატებითი ველების აღწერის წამოღება*

**GET** `api/operation/getVendorAdditionalFields`

**Response**

```json
{ 
    "fields": [{ 
        "name": "usr_column_515", 
        "header": "ლიმიტი" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `fields[]` | collection | Collection describing the vendor's additional fields consisting of: · *მომწოდებლის დამატებითი ველების აღწერის კოლექციაა რომელიც შედგება:* |
| `fields[].name` | string | Name of the vendor's additional field in the database (Column) · *მომწოდებლის დამატებითი ველის დასახელება მონაცემთა ბაზაში (Column)* |
| `fields[].header` | string | Name given by the user to the vendor's additional field · *მომხმარებლის მიერ მომწოდებლის დამატებითი ველისთვის დარქმეული სახელი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getCustomerGroups

Customer groups · *მყიდველის ჯგუფები*

Fetch customer groups · *მყიდველის ჯგუფების წამოღება*

**GET** `api/operation/getCustomerGroups`

**Response**

```json
{ 
    "groups": [{ 
        "id": 5, 
        "parent_id": 2, 
        "path": "0#2#5", 
        "name": "მყიდველები" 
    }, { 
        "id": 22, 
        "parent_id": 5, 
        "path": "0#2#5#22", 
        "name": "მყიდველები Level2" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `groups[]` | collection | Collection of customer groups consisting of: · *მყიდველის ჯგუფების კოლექციაა რომელიც შედგება:* |
| `groups[].id` | int | Group Id · *ჯგუფის Id* |
| `groups[].parent_id` | int | Parent group Id · *მშობელი ჯგუფის Id* |
| `groups[].path` | string | Path of the group record · *ჯგუფის ჩანაწერის მისამართი* |
| `groups[].name` | string | Group name · *ჯგუფის დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getVendorGroups

Vendor groups · *მომწოდებლის ჯგუფები*

Fetch vendor groups · *მომწოდებლის ჯგუფების წამოღება*

**GET** `api/operation/getVendorGroups`

**Response**

```json
{ 
    "groups": [{ 
        "id": 3, 
        "parent_id": 1, 
        "path": "0#1#3", 
        "name": "მომწოდებლები" 
    }, { 
        "id": 23, 
        "parent_id": 3, 
        "path": "0#1#3#23", 
        "name": "იმპორტიორები" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `groups[]` | collection | Collection of vendor groups consisting of: · *მომწოდებლის ჯგუფების კოლექციაა რომელიც შედგება:* |
| `groups[].id` | int | Group Id · *ჯგუფის Id* |
| `groups[].parent_id` | int | Parent group Id · *მშობელი ჯგუფის Id* |
| `groups[].path` | string | Path of the group record · *ჯგუფის ჩანაწერის მისამართი* |
| `groups[].name` | string | Group name · *ჯგუფის დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getCustomerAddresses

Customer addresses · *მყიდველის მისამართები*

Fetch customer addresses · *მყიდველის მისამართების წამოღება*

**GET** `api/operation/getCustomerAddresses`

**Response**

```json
{ 
    "addresses": [{ 
        "id": 5, 
        "contragent_id": 2, 
        "address": "ქ. თბილისი" 
    }, { 
        "id": 15, 
        "contragent_id": 3, 
        "address": "ქ. ბათუმი" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `addresses[]` | collection | Collection of customer addresses consisting of: · *მყიდველის მისამართების კოლექციაა რომელიც შედგება:* |
| `addresses[].id` | int | Address Id · *მისამართის Id* |
| `addresses[].contragent_id` | int | Customer Id · *მყიდველის Id* |
| `addresses[].address` | string | Address · *მისამართი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getVendorAddresses

Vendor addresses · *მომწოდებლის მისამართები*

Fetch vendor addresses · *მომწოდებლის მისამართების წამოღება*

**GET** `api/operation/getVendorAddresses`

**Response**

```json
{ 
    "addresses": [{ 
        "id": 51, 
        "contragent_id": 32, 
        "address": "ქ. თბილისი" 
    }, { 
        "id": 165, 
        "contragent_id": 33, 
        "address": "ქ. ბათუმი" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `addresses[]` | collection | Collection of vendor addresses consisting of: · *მომწოდებლის მისამართების კოლექციაა რომელიც შედგება:* |
| `addresses[].id` | int | Address Id · *მისამართის Id* |
| `addresses[].contragent_id` | int | Vendor Id · *მომწოდებლის Id* |
| `addresses[].address` | string | Address · *მისამართი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getCustomerAgreements

Customer agreements · *მყიდველის ხელშეკრულებები*

Fetch customer agreements · *მყიდველის ხელშეკრულებების წამოღება*

**GET** `api/operation/getCustomerAgreements`

**Response**

```json
{ 
    "agreements": [{ 
        "id": 5, 
        "contragent_id": 2, 
        "price_id": 3, 
        "name": "დასახელება_1", 
        "description": "", 
        "discount": 10, 
        "is_active": true 
    }, { 
        "id": 6, 
        "contragent_id": 2, 
        "price_id": 4, 
        "name": "დასახელება_2", 
        "description": "", 
        "discount": 15, 
        "is_active": true 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `agreements[]` | collection | Collection of customer agreements consisting of: · *მყიდველის ხელშეკრულებების კოლექციაა რომელიც შედგება:* |
| `agreements[].id` | int | Agreement Id · *ხელშეკრულების Id* |
| `agreements[].contragent_id` | int | Customer Id · *მყიდველის Id* |
| `agreements[].price_id` | int | Price type Id · *ფასის ტიპის Id* |
| `agreements[].name` | string | Name · *დასახელება* |
| `agreements[].description` | string | Description · *აღწერა* |
| `agreements[].discount` | double | Discount (%) · *ფასდაკლება (%)* |
| `agreements[].is_active` | bool | Status, whether it is active · *სტატუსი, აქტიურია თუ არა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getContragentSubAccountFields

Description of contragent sub-account fields · *კონტრაგენტის ქვე ანგარიშების ველების აღწერა*

Fetch the description of contragent sub-account fields · *კონტრაგენტის ქვე ანგარიშების ველების აღწერის წამოღება*

**GET** `api/operation/getContragentSubAccountFields`

**Response**

```json
{ 
  "fields": [{ 
      "name": "usr_column_551", 
      "header": "სახელმწიფო ნომერი" 
    },{ 
      "name": "usr_column_552", 
      "header": "VIN კოდი" 
    },{ 
      "name": "usr_column_554", 
      "header": "მარკა" 
    }], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `fields[]` | collection | Collection describing contragent sub-account fields consisting of: · *კონტრაგენტის ქვე ანგარიშების ველების აღწერის კოლექციაა რომელიც შედგება:* |
| `fields[].name` | string | Name of the contragent sub-account field in the database (Column) · *კონტრაგენტის ქვე ანგარიშების ველების დასახელება მონაცემთა ბაზაში (Column)* |
| `fields[].header` | string | Name given by the user to the contragent sub-account field · *მომხმარებლის მიერ კონტრაგენტის ქვე ანგარიშების ველისთვის დარქმეული სახელი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getCustomerSubAccounts

Customer sub-accounts · *მყიდველების ქვე ანგარიშები*

Fetch customer sub-accounts · *მყიდველების ქვე ანგარიშების წამოღება*

**GET** `api/operation/getCustomerSubAccounts`

**Response**

```json
{ 
  "contragent_sub_accounts": [{ 
      "id": 43, 
      "contragent_id": 837, 
      "sub_accounts": [{ 
          "field": "usr_column_551", 
          "value": "UBU115" 
        },{ 
          "field": "usr_column_552", 
          "value": "WDB9540321K214212" 
        },{ 
          "field": "usr_column_554", 
          "value": "მერსედესი" 
        } ] 
    },{ 
      "id": 88, 
      "contragent_id": 845, 
      "sub_accounts": [{ 
          "field": "usr_column_551", 
          "value": "00038BA" 
        },{ 
          "field": "usr_column_552", 
          "value": "XLRTE47XS0E472538" 
        },{ 
          "field": "usr_column_554", 
          "value": "დაფი" 
        }] 
    }], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Customer sub-account Id · *მყიდველის ქვე ანგარიშის Id* |
| `contragent_id` | int | Customer Id · *მყიდველის Id* |
| `sub_accounts[]` | collection | Collection of the customer sub-account's fields, where: · *მყიდველის ქვე ანგარიშის ველების კოლექცია სადაც:* |
| `sub_accounts[].field` | string | Field name · *ველის დასახელება* |
| `sub_accounts[].value` | string | Field value · *ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `contragent_sub_accounts` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---

### getVendorSubAccounts

Vendor sub-accounts · *მომწოდებლების ქვე ანგარიშები*

Fetch vendor sub-accounts · *მომწოდებლების ქვე ანგარიშების წამოღება*

**GET** `api/operation/getVendorSubAccounts`

**Response**

```json
{ 
  "contragent_sub_accounts": [{ 
      "id": 143, 
      "contragent_id": 1837, 
      "sub_accounts": [{ 
          "field": "usr_column_551", 
          "value": "UBU115" 
        },{ 
          "field": "usr_column_552", 
          "value": "WDB9540321K214212" 
        },{ 
          "field": "usr_column_554", 
          "value": "მერსედესი" 
        } ] 
    },{ 
      "id": 188, 
      "contragent_id": 1845, 
      "sub_accounts": [{ 
          "field": "usr_column_551", 
          "value": "00038BA" 
        },{ 
          "field": "usr_column_552", 
          "value": "XLRTE47XS0E472538" 
        },{ 
          "field": "usr_column_554", 
          "value": "დაფი" 
        }] 
    }], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Vendor sub-account Id · *მომწოდებლის ქვე ანგარიშის Id* |
| `contragent_id` | int | Vendor Id · *მომწოდებლის Id* |
| `sub_accounts[]` | collection | Collection of the vendor sub-account's fields, where: · *მომწოდებლის ქვე ანგარიშის ველების კოლექცია სადაც:* |
| `sub_accounts[].field` | string | Field name · *ველის დასახელება* |
| `sub_accounts[].value` | string | Field value · *ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `contragent_sub_accounts` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---

### saveCustomer

Save a customer · *მყიდველის შენახვა*

Save a customer (insert, update) · *მყიდველის შენახვა (insert, update)*

**POST** `api/operation/saveCustomer`

**Request body**

```json
{ 
    "id": 0, 
    "code": "12345678910", 
    "name": "name1", 
    "group_id": 5, 
    "address": "Address1", 
    "phone": "+99555000000", 
    "email": "test@test.com", 
    "vat_type": 1, 
    "is_resident": false, 
    "is_company": true, 
    "cons_period": 30, 
    "birth_date": "2010-11-08T18:00:00", 
    "marketing_promotions": false, 
    "add_fields": [{ 
        "field": "usr_column_515", 
        "value": "20" 
    }] 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Customer Id. (pass 0 to create a new one) · *მყიდველის Id. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `code` | string[50] | Customer's identification code or personal number · *მყიდველის საიდენტიფიკაციო კოდი ან პირადი ნომერი* |
| `name` | string[200] | Name · *დასახელება* |
| `group_id` | int | Customer group Id. (default = 5) · *მყიდველის ჯგუფის Id. (სტანდარტულად = 5)* |
| `address` | string[200] | Address · *მისამართი* |
| `phone` | string[50] | Phone number · *ტელეფონის ნომერი* |
| `email` | string[50] | Email · *ელ. ფოსტა* |
| `vat_type` | byte | VAT type (0 - not a VAT payer, 1 - VAT payer, 2 - exempt with the right of deduction, 3 - exempt without the right of deduction) · *დღგ-ს ტიპი (0 - არ არის დღგ-ს გადამხდელი, 1 - დღგ-ს გადამხდელი, 2 - განთავისუფლებული ჩათვლის უფლებით, 3 - განთავისუფლებული ჩათვლის უფლების გარეშე)* |
| `is_resident` | bool | Resident (true - local, false - foreign citizen) · *რეზიდენტი (true - ადგილობრივი, false - უცხო ქვეყნის მოქალაქე)* |
| `is_company` | bool | Customer type (true - legal entity, false - natural person) · *მყიდველის ტიპი (true - იურიდიული პირი, false - ფიზიკური პირი)* |
| `cons_period` | int | Consignment period (days) · *კონსიგნაციის პერიოდი (დღე)* |
| `birth_date` | datetime | Date of birth · *დაბადების თარიღი* |
| `marketing_promotions` | bool | Permission to use in marketing campaigns · *მარკეტინგულ აქციებში გამოყენების ნებართვა* |
| `add_fields[]` | collection | Collection of the customer's additional fields, where: · *მყიდველის დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |

**Response**

```json
{ 
    "id": 15, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the inserted (or updated) customer · *დამატებული (ან დარედაქტირებული) მყიდველის Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### saveVendor

Save a vendor · *მომწოდებლის შენახვა*

Save a vendor (insert, update) · *მომწოდებლის შენახვა (insert, update)*

**POST** `api/operation/saveVendor`

**Request body**

```json
{ 
    "id": 0, 
    "code": "21345678910", 
    "name": "name2", 
    "group_id": 3, 
    "address": "Address2", 
    "phone": "+99555000001", 
    "email": "test2@test.com", 
    "vat_type": 1, 
    "is_resident": false, 
    "is_company": true, 
    "cons_period": 10, 
    "birth_date": "2010-11-08T18:00:00", 
    "marketing_promotions": true, 
    "add_fields": [{ 
        "field": "usr_column_515", 
        "value": "20" 
    }] 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Vendor Id. (pass 0 to create a new one) · *მომწოდებლის Id. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `code` | string[50] | Vendor's identification code or personal number · *მომწოდებლის საიდენტიფიკაციო კოდი ან პირადი ნომერი* |
| `name` | string[200] | Name · *დასახელება* |
| `group_id` | int | Vendor group Id. (default = 3) · *მომწოდებლის ჯგუფის Id. (სტანდარტულად = 3)* |
| `address` | string[200] | Address · *მისამართი* |
| `phone` | string[50] | Phone number · *ტელეფონის ნომერი* |
| `email` | string[50] | Email · *ელ. ფოსტა* |
| `vat_type` | byte | VAT type (0 - not a VAT payer, 1 - VAT payer, 2 - exempt with the right of deduction, 3 - exempt without the right of deduction) · *დღგ-ს ტიპი (0 - არ არის დღგ-ს გადამხდელი, 1 - დღგ-ს გადამხდელი, 2 - განთავისუფლებული ჩათვლის უფლებით, 3 - განთავისუფლებული ჩათვლის უფლების გარეშე)* |
| `is_resident` | bool | Resident (true - local, false - foreign citizen) · *რეზიდენტი (true - ადგილობრივი, false - უცხო ქვეყნის მოქალაქე)* |
| `is_company` | bool | Vendor type (true - legal entity, false - natural person) · *მომწოდებლის ტიპი (true - იურიდიული პირი, false - ფიზიკური პირი)* |
| `cons_period` | int | Consignment period (days) · *კონსიგნაციის პერიოდი (დღე)* |
| `birth_date` | datetime | Date of birth · *დაბადების თარიღი* |
| `marketing_promotions` | bool | Permission to use in marketing campaigns · *მარკეტინგულ აქციებში გამოყენების ნებართვა* |
| `add_fields[]` | collection | Collection of the vendor's additional fields, where: · *მომწოდებლის დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |

**Response**

```json
{ 
    "id": 16, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the inserted (or updated) vendor · *დამატებული (ან დარედაქტირებული) მომწოდებლის Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---
