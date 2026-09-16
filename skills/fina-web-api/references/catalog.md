# Products, services, fixed assets and their catalogues

27 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getProductGroups`](#getproductgroups) | GET | `api/operation/getProductGroups` | Product groups |
| [`getWebProductGroups`](#getwebproductgroups) | GET | `api/operation/getWebProductGroups` | Alternative (web) product groups |
| [`getProvidedServiceGroups`](#getprovidedservicegroups) | GET | `api/operation/getProvidedServiceGroups` | Provided service groups |
| [`getReceivedServiceGroups`](#getreceivedservicegroups) | GET | `api/operation/getReceivedServiceGroups` | Received service groups |
| [`getInventoryGroups`](#getinventorygroups) | GET | `api/operation/getInventoryGroups` | Fixed asset groups |
| [`getProducts`](#getproducts) | GET | `api/operation/getProducts` | Product catalogue |
| [`getProductsArray`](#getproductsarray) | POST | `api/operation/getProductsArray` | Selected product catalogue |
| [`getProductsAfter`](#getproductsafter) | GET | `api/operation/getProductsAfter/{after_date}` | Product catalogue |
| [`getProvidedServices`](#getprovidedservices) | GET | `api/operation/getProvidedServices` | Provided services catalogue |
| [`getReceivedServices`](#getreceivedservices) | GET | `api/operation/getReceivedServices` | Received services catalogue |
| [`getInventories`](#getinventories) | GET | `api/operation/getInventories` | Fixed assets catalogue |
| [`getProductAdditionalFields`](#getproductadditionalfields) | GET | `api/operation/getProductAdditionalFields` | Description of the product's additional fields |
| [`getProvidedServiceAdditionalFields`](#getprovidedserviceadditionalfields) | GET | `api/operation/getProvidedServiceAdditionalFields` | Description of the provided service's additional fields |
| [`getInventoryAdditionalFields`](#getinventoryadditionalfields) | GET | `api/operation/getInventoryAdditionalFields` | Description of the fixed asset's additional fields |
| [`getCharacteristics`](#getcharacteristics) | GET | `api/operation/getCharacteristics` | Description of product characteristics |
| [`getCharacteristicValues`](#getcharacteristicvalues) | GET | `api/operation/getCharacteristicValues` | Product characteristics |
| [`getCharacteristicValuesArray`](#getcharacteristicvaluesarray) | POST | `api/operation/getCharacteristicValuesArray` | Characteristics of selected products |
| [`getPackedProducts`](#getpackedproducts) | GET | `api/operation/getPackedProducts` | Products grouped together |
| [`getSubCodeTypes`](#getsubcodetypes) | GET | `api/operation/getSubCodeTypes` | Sub-code types |
| [`getProductSubCodes`](#getproductsubcodes) | GET | `api/operation/getProductSubCodes` | Product sub-codes |
| [`getProductPlaces`](#getproductplaces) | GET | `api/operation/getProductPlaces` | Product storage places |
| [`getProductImages`](#getproductimages) | GET | `api/operation/getProductImages/{product}` | Product images |
| [`getProductsImageArray`](#getproductsimagearray) | POST | `api/operation/getProductsImageArray` | Images of selected products |
| [`getProductsBarcodeArray`](#getproductsbarcodearray) | POST | `api/operation/getProductsBarcodeArray` | Barcodes of selected products |
| [`getProductsOnWay`](#getproductsonway) | GET | `api/operation/getProductsOnWay` | Pending product orders (goods in transit) |
| [`saveProduct`](#saveproduct) | POST | `api/operation/saveProduct` | Save a product |
| [`saveProvidedService`](#saveprovidedservice) | POST | `api/operation/saveProvidedService` | Save a provided service |

---

### getProductGroups

Product groups · *საქონლის ჯგუფები*

Fetch product groups · *საქონლის ჯგუფების წამოღება*

**GET** `api/operation/getProductGroups`

**Response**

```json
{ 
    "groups": [{ 
        "id": 10, 
        "parent_id": 1, 
        "order_id": 10, 
        "path": "0#1#10", 
        "name": "სასაქონლო–მატერიალური აქტივები" 
    }, { 
        "id": 11, 
        "parent_id": 10, 
        "order_id": 11, 
        "path": "0#1#10#11", 
        "name": "საქონელი" 
    }, { 
        "id": 16, 
        "parent_id": 10, 
        "order_id": 16, 
        "path": "0#1#10#16", 
        "name": "შენიშვნები" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `groups[]` | collection | Collection of product groups consisting of: · *საქონლის ჯგუფების კოლექციაა რომელიც შედგება:* |
| `groups[].id` | int | Group Id · *ჯგუფის Id* |
| `groups[].parent_id` | int | Parent group Id · *მშობელი ჯგუფის Id* |
| `groups[].order_id` | int | Sort order · *სორტირება* |
| `groups[].path` | string | Path of the group record · *ჯგუფის ჩანაწერის მისამართი* |
| `groups[].name` | string | Group name · *ჯგუფის დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getWebProductGroups

Alternative (web) product groups · *საქონლის ალტერნატიული (ვებ) ჯგუფები*

Fetch alternative (web) product groups · *საქონლის ალტერნატიული (ვებ) ჯგუფების წამოღება*

**GET** `api/operation/getWebProductGroups`

**Response**

```json
{ 
    "groups": [{ 
        "id": 10, 
        "parent_id": 1, 
        "order_id": 10, 
        "path": "0#1#10", 
        "image": null, 
        "name": "სასაქონლო ჯგუფები", 
        "name2": "", 
        "name3": "" 
    }, { 
        "id": 12, 
        "parent_id": 11, 
        "order_id": 13, 
        "path": "0#1#10#11#12", 
        "image": null, 
        "name": "ციტრუსი", 
        "name2": "", 
        "name3": "" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `groups[]` | collection | Collection of alternative product groups consisting of: · *საქონლის ალტერნატიული ჯგუფების კოლექციაა რომელიც შედგება:* |
| `groups[].id` | int | Group Id · *ჯგუფის Id* |
| `groups[].parent_id` | int | Parent group Id · *მშობელი ჯგუფის Id* |
| `groups[].order_id` | int | Sort order · *სორტირება* |
| `groups[].path` | string | Path of the group record · *ჯგუფის ჩანაწერის მისამართი* |
| `groups[].image` | string | Image (base64 of byte[]) · *სურათი (base64 of byte[]) * |
| `groups[].name` | string | Group name · *ჯგუფის დასახელება* |
| `groups[].name2` | string | Alternative name of the group · *ჯგუფის ალტერნატიული დასახელება* |
| `groups[].name3` | string | Alternative name of the group 3 · *ჯგუფის ალტერნატიული დასახელება3* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProvidedServiceGroups

Provided service groups · *გაწეული მომსახურების ჯგუფები*

Fetch provided service groups · *გაწეული მომსახურების ჯგუფების წამოღება*

**GET** `api/operation/getProvidedServiceGroups`

**Response**

```json
{ 
    "groups": [{ 
        "id": 110, 
        "parent_id": 2, 
        "order_id": 110, 
        "path": "0#2#110", 
        "name": "გაწეული მომსახურება" 
    }, { 
        "id": 135, 
        "parent_id": 110, 
        "order_id": 135, 
        "path": "0#2#110#135", 
        "name": "ქვე ჯგუფი" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `groups[]` | collection | Collection of provided service groups consisting of: · *გაწეული მომსახურების ჯგუფების კოლექციაა რომელიც შედგება:* |
| `groups[].id` | int | Group Id · *ჯგუფის Id* |
| `groups[].parent_id` | int | Parent group Id · *მშობელი ჯგუფის Id* |
| `groups[].order_id` | int | Sort order · *სორტირება* |
| `groups[].path` | string | Path of the group record · *ჯგუფის ჩანაწერის მისამართი* |
| `groups[].name` | string | Group name · *ჯგუფის დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getReceivedServiceGroups

Received service groups · *მიღებული მომსახურების ჯგუფები*

Fetch received service groups · *მიღებული მომსახურების ჯგუფების წამოღება*

**GET** `api/operation/getReceivedServiceGroups`

**Response**

```json
{ 
    "groups": [{ 
        "id": 120, 
        "parent_id": 2, 
        "order_id": 120, 
        "path": "0#2#120", 
        "name": "მიღებული მომსახურება" 
    }, { 
        "id": 121, 
        "parent_id": 120, 
        "order_id": 121, 
        "path": "0#2#120#121", 
        "name": "საიჯარო ქირა" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `groups[]` | collection | Collection of received service groups consisting of: · *მიღებული მომსახურების ჯგუფების კოლექციაა რომელიც შედგება:* |
| `groups[].id` | int | Group Id · *ჯგუფის Id* |
| `groups[].parent_id` | int | Parent group Id · *მშობელი ჯგუფის Id* |
| `groups[].order_id` | int | Sort order · *სორტირება* |
| `groups[].path` | string | Path of the group record · *ჯგუფის ჩანაწერის მისამართი* |
| `groups[].name` | string | Group name · *ჯგუფის დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getInventoryGroups

Fixed asset groups · *ძირითადი საშუალებების ჯგუფები*

Fetch fixed asset groups · *ძირითადი საშუალებების ჯგუფების წამოღება*

**GET** `api/operation/getInventoryGroups`

**Response**

```json
{ 
    "groups": [{ 
        "id": 40, 
        "parent_id": 3, 
        "order_id": 40, 
        "path": "0#3#40", 
        "name": "ძირითადი საშუალებები" 
    }, { 
        "id": 41, 
        "parent_id": 40, 
        "order_id": 41, 
        "path": "0#3#40#41", 
        "name": "მიწის ნაკვეთები" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `groups[]` | collection | Collection of fixed asset groups consisting of: · *ძირითადი საშუალების ჯგუფების კოლექციაა რომელიც შედგება:* |
| `groups[].id` | int | Group Id · *ჯგუფის Id* |
| `groups[].parent_id` | int | Parent group Id · *მშობელი ჯგუფის Id* |
| `groups[].order_id` | int | Sort order · *სორტირება* |
| `groups[].path` | string | Path of the group record · *ჯგუფის ჩანაწერის მისამართი* |
| `groups[].name` | string | Group name · *ჯგუფის დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProducts

Product catalogue · *საქონლის კატალოგი*

Fetch the product catalogue · *საქონლის კატალოგის წამოღება*

**GET** `api/operation/getProducts`

**Response**

```json
{ 
    "products": [{ 
        "id": 5, 
        "group_id": 11, 
        "web_group_id": 18, 
        "unit_id": 1, 
        "code": "00011111111111111105", 
        "name": "ანოს ასკილი", 
        "name_eng": null, 
        "name_rus": null, 
        "comment": "", 
        "partnumber": "", 
        "weight": 0, 
        "volume": 0, 
        "vat": 1, 
        "order_id": 1, 
        "min_quantity": "3", 
        "plu": 0, 
        "add_fields": [{ 
            "field": "usr_column_501", 
            "value": "" 
        }, { 
            "field": "usr_column_502", 
            "value": "უშაქრო" 
        }, { 
            "field": "usr_column_503", 
            "value": "" 
        }] 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `products[]` | collection | Collection of the product catalogue consisting of: · *საქონლის კატალოგის კოლექციაა რომელიც შედგება:* |
| `products[].id` | int | Product Id · *საქონლის Id* |
| `products[].group_id` | int | Product group Id · *საქონლის ჯგუფის Id* |
| `products[].web_group_id` | int | Alternative product group Id · *საქონლის ალტერნატიული ჯგუფის Id* |
| `products[].unit_id` | int | Product unit Id · *საქონლის ერთეულის Id* |
| `products[].code` | string | Product code · *საქონლის კოდი* |
| `products[].name` | string | Product name · *საქონლის დასახელება* |
| `products[].name_eng` | string | Product name in English · *საქონლის დასახელება ინგლისურ ენაზე* |
| `products[].name_rus` | string | Product name in Russian · *საქონლის დასახელება რუსულ ენაზე* |
| `products[].comment` | string | Comment · *კომენტარი* |
| `products[].partnumber` | string | Part number · *არტიკული* |
| `products[].weight` | double | Weight · *წონა* |
| `products[].volume` | double | Volume · *მოცულობა* |
| `products[].vat` | byte | VAT type (1 - taxable, 2 - zero-rated, 3 - non-taxable) · *დღგ-ს ტიპი (1 - იბეგრება, 2 - ნულოვანი, 3 - დაუბეგრავი)* |
| `products[].order_id` | int | Sort order · *სორტირება* |
| `products[].min_quantity` | string | Minimum quantity information · *მინიმალური რაოდენობის ინფორმაცია* |
| `products[].plu` | int | PLU code (for weighed goods) · *PLU კოდი (წონითი საქონლის შემთხვევაში)* |
| `products[].add_fields[]` | collection | Collection of the product's additional fields, where: · *საქონლის დამატებითი ველების კოლექცია სადაც:* |
| `products[].add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `products[].add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProductsArray

Selected product catalogue · *შერჩეული საქონლის კატალოგი*

Fetch the catalogue of selected products · *შერჩეული საქონლის კატალოგის წამოღება*

**POST** `api/operation/getProductsArray`

**Request body**

```json
[ 
    1, 2 
]
```

**Response** — identical to [`getProducts`](#getproducts).

> The returned product catalogue collection is identical to the collection returned by the getProducts method. (If the number of parameters passed exceeds 2000, calling the getProducts method is recommended)

> int[] - a collection of product Ids

---

### getProductsAfter

Product catalogue · *საქონლის კატალოგი*

Fetch the changed product catalogue · *შეცვლილი საქონლის კატალოგის წამოღება*

**GET** `api/operation/getProductsAfter/{after_date}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `after_date` | datetime | Date (yyyy-MM-ddTHH:mm:ss) after which changes are of interest · *თარიღი (yyyy-MM-ddTHH:mm:ss), რომლის შემდგომი ცვლილებებიც გვაინტერესებს* |

**Response** — identical to [`getProducts`](#getproducts).

> The returned product catalogue collection is identical to the collection returned by the getProducts method

---

### getProvidedServices

Provided services catalogue · *გაწეული მომსახურების კატალოგი*

Fetch the provided services catalogue · *გაწეული მომსახურების კატალოგის წამოღება*

**GET** `api/operation/getProvidedServices`

**Response**

```json
{ 
    "services": [{ 
        "id": 8, 
        "group_id": 110, 
        "unit_id": 17, 
        "code": "02", 
        "name": "მომსახურება", 
        "comment": "", 
        "vat": 1, 
        "add_fields": [] 
    }, { 
        "id": 11, 
        "group_id": 110, 
        "unit_id": 17, 
        "code": "", 
        "name": "Service", 
        "comment": "", 
        "vat": 1, 
        "add_fields": [] 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `services[]` | collection | Collection of the provided services catalogue consisting of: · *გაწეული მომსახურების კატალოგის კოლექციაა რომელიც შედგება:* |
| `services[].id` | int | Provided service Id · *გაწეული მომსახურების Id* |
| `services[].group_id` | int | Provided service group Id · *გაწეული მომსახურების ჯგუფის Id* |
| `services[].unit_id` | int | Provided service unit Id · *გაწეული მომსახურების ერთეულის Id* |
| `services[].code` | string | Provided service code · *გაწეული მომსახურების კოდი* |
| `services[].name` | string | Provided service name · *გაწეული მომსახურების დასახელება* |
| `services[].comment` | string | Comment · *კომენტარი* |
| `services[].vat` | byte | VAT type (1 - taxable, 2 - zero-rated, 3 - non-taxable) · *დღგ-ს ტიპი (1 - იბეგრება, 2 - ნულოვანი, 3 - დაუბეგრავი)* |
| `add_fields[]` | collection | Collection of the provided service's additional fields, where: · *გაწეული მომსახურების დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `field`, `value` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getReceivedServices

Received services catalogue · *მიღებული მომსახურების კატალოგი*

Fetch the received services catalogue · *მიღებული მომსახურების კატალოგის წამოღება*

**GET** `api/operation/getReceivedServices`

**Response**

```json
{ 
    "services": [{ 
        "id": 7, 
        "group_id": 132, 
        "unit_id": 17, 
        "code": "151515", 
        "name": "მასაჟი", 
        "comment": "", 
        "vat": 1, 
        "add_fields": [{ 
            "field": "usr_column_535", 
            "value": "13" 
        }] 
    }, { 
        "id": 17, 
        "group_id": 129, 
        "unit_id": 1, 
        "code": "00012", 
        "name": "ყავა", 
        "comment": "", 
        "vat": 1, 
        "add_fields": [{ 
            "field": "usr_column_535", 
            "value": "" 
        }] 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `services[]` | collection | Collection of the received services catalogue consisting of: · *მიღებული მომსახურების კატალოგის კოლექციაა რომელიც შედგება:* |
| `services[].id` | int | Received service Id · *მიღებული მომსახურების Id* |
| `services[].group_id` | int | Received service group Id · *მიღებული მომსახურების ჯგუფის Id* |
| `services[].unit_id` | int | Received service unit Id · *მიღებული მომსახურების ერთეულის Id* |
| `services[].code` | string | Received service code · *მიღებული მომსახურების კოდი* |
| `services[].name` | string | Received service name · *მიღებული მომსახურების დასახელება* |
| `services[].comment` | string | Comment · *კომენტარი* |
| `services[].vat` | byte | VAT type (1 - taxable, 2 - zero-rated, 3 - non-taxable) · *დღგ-ს ტიპი (1 - იბეგრება, 2 - ნულოვანი, 3 - დაუბეგრავი)* |
| `add_fields[]` | collection | Collection of the received service's additional fields, where: · *მიღებული მომსახურების დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getInventories

Fixed assets catalogue · *ძირითადი საშუალებების კატალოგი*

Fetch the fixed assets catalogue · *ძირითადი საშუალებების კატალოგის წამოღება*

**GET** `api/operation/getInventories`

**Response**

```json
{ 
    "inventories": [{ 
        "id": 14, 
        "group_id": 41, 
        "unit_id": 1, 
        "code": "00009", 
        "name": "inv1", 
        "comment": "", 
        "in_date": null, 
        "amortization_type": 0, 
        "service_term": 0.0, 
        "liquidation_cost": 0.0, 
        "add_fields": [{ 
            "field": "usr_column_532", 
            "value": "30.01" 
        }] 
    }, { 
        "id": 22, 
        "group_id": 48, 
        "unit_id": 1, 
        "code": "00124", 
        "name": "trans", 
        "comment": "", 
        "in_date": "2018-12-26T17:24:03", 
        "amortization_type": 1, 
        "service_term": 12.0, 
        "liquidation_cost": 50.0, 
        "add_fields": [{ 
            "field": "usr_column_532", 
            "value": "" 
        }] 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `inventories[]` | collection | Collection of the fixed assets catalogue consisting of: · *ძირითადი საშუალების კატალოგის კოლექციაა რომელიც შედგება:* |
| `inventories[].id` | int | Fixed asset Id · *ძირითადი საშუალების Id* |
| `inventories[].group_id` | int | Fixed asset group Id · *ძირითადი საშუალების ჯგუფის Id* |
| `inventories[].unit_id` | int | Fixed asset unit Id · *ძირითადი საშუალების ერთეულის Id* |
| `inventories[].code` | string | Fixed asset code · *ძირითადი საშუალების კოდი* |
| `inventories[].name` | string | Fixed asset name · *ძირითადი საშუალების დასახელება* |
| `inventories[].comment` | string | Comment · *კომენტარი* |
| `inventories[].in_date` | datetime? | Date of entry into service · *ექსპლუატაციაში შესვლის თარიღი* |
| `inventories[].amortization_type` | byte | Amortization method (0 - declining balance, 1 - straight line) · *ამორტიზაციის მეთოდი (0 - ნარჩენი ღირებულება, 1 - წრფივი)* |
| `inventories[].service_term` | double | Useful life (months) · *გამოყენების ვადა (თვე)* |
| `inventories[].liquidation_cost` | double | Liquidation (salvage) value · *სალიკვიდაციო ღირებულება* |
| `add_fields[]` | collection | Collection of the fixed asset's additional fields, where: · *ძირითადი საშუალების დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProductAdditionalFields

Description of the product's additional fields · *პროდუქტის დამატებითი ველების აღწერა*

Fetch the description of the product's additional fields · *პროდუქტის დამატებითი ველების აღწერის წამოღება*

**GET** `api/operation/getProductAdditionalFields`

**Response**

```json
{ 
    "fields": [{ 
        "name": "usr_column_501", 
        "header": "ველი1" 
    }, { 
        "name": "usr_column_502", 
        "header": "ველი2" 
    }, { 
        "name": "usr_column_503", 
        "header": "მწარმოებელი კომპანია" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `fields[]` | collection | Collection describing the product's additional fields consisting of: · *პროდუქტის დამატებითი ველების აღწერის კოლექციაა რომელიც შედგება:* |
| `fields[].name` | string | Name of the product's additional field in the database (Column) · *პროდუქტის დამატებითი ველის დასახელება მონაცემთა ბაზაში (Column)* |
| `fields[].header` | string | Name given by the user to the product's additional field · *მომხმარებლის მიერ პროდუქტის დამატებითი ველისთვის დარქმეული სახელი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProvidedServiceAdditionalFields

Description of the provided service's additional fields · *გაწეული მომსახურების დამატებითი ველების აღწერა*

Fetch the description of the provided service's additional fields · *გაწეული მომსახურების დამატებითი ველების აღწერის წამოღება*

**GET** `api/operation/getProvidedServiceAdditionalFields`

**Response**

```json
{ 
    "fields": [{ 
        "name": "usr_column_506", 
        "header": "About" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `fields.name` | string | Name of the provided service's additional field in the database (Column) · *გაწეული მომსახურების დამატებითი ველის დასახელება მონაცემთა ბაზაში (Column)* |
| `fields.header` | string | Name given by the user to the provided service's additional field · *მომხმარებლის მიერ გაწეული მომსახურების დამატებითი ველისთვის დარქმეული სახელი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `fields` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---

### getInventoryAdditionalFields

Description of the fixed asset's additional fields · *ძირითადი საშუალების დამატებითი ველების აღწერა*

Fetch the description of the fixed asset's additional fields · *ძირითადი საშუალების დამატებითი ველების აღწერის წამოღება*

**GET** `api/operation/getInventoryAdditionalFields`

**Response**

```json
{ 
    "fields": [{ 
        "name": "usr_column_532", 
        "header": "გახარჯვა" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `fields.name` | string | Name of the fixed asset's additional field in the database (Column) · *ძირითადი საშუალების დამატებითი ველის დასახელება მონაცემთა ბაზაში (Column)* |
| `fields.header` | string | Name given by the user to the fixed asset's additional field · *მომხმარებლის მიერ ძირითადი საშუალების დამატებითი ველისთვის დარქმეული სახელი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `fields` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---

### getCharacteristics

Description of product characteristics · *პროდუქტის მახასიათებლების აღწერა*

Fetch the description of product characteristics · *პროდუქტის მახასიათებლების აღწერის წამოღება*

**GET** `api/operation/getCharacteristics`

**Response**

```json
{ 
    "characteristics": [{ 
        "id": 1, 
        "tag": "COLOR", 
        "type": 0, 
        "name": "ფერი", 
        "name2": "Color", 
        "name3": "Колір" 
    }, { 
        "id": 4, 
        "tag": "POWER", 
        "type": 0, 
        "name": "სიმძლავრე", 
        "name2": "Power", 
        "name3": "потужність" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `characteristics[]` | collection | Collection describing product characteristics consisting of: · *პროდუქტის მახასიათებლების აღწერის კოლექციაა რომელიც შედგება:* |
| `characteristics[].id` | int | Characteristic id · *მახასიათებლის id* |
| `characteristics[].tag` | string | Characteristic tag (unique for every characteristic) · *მახასიათებლის tag (უნიკალური ყოველი მახასიათებლისთვის)* |
| `characteristics[].type` | byte | Characteristic type (0 - text, 1 - list) · *მახასიათებლის ტიპი (0 - ტექსტური, 1 - სია)* |
| `characteristics[].name` | string | Characteristic name · *მახასიათებლის დასახელება* |
| `characteristics[].name2` | string | Alternative name of the characteristic · *მახასიათებლის ალტერნატიული დასახელება* |
| `characteristics[].name3` | string | Alternative name of the characteristic · *მახასიათებლის ალტერნატიული დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getCharacteristicValues

Product characteristics · *პროდუქტის მახასიათებლები*

Fetch product characteristics · *პროდუქტის მახასიათებლების წამოღება*

**GET** `api/operation/getCharacteristicValues`

**Response**

```json
{ 
    "characteristic_values": [{ 
        "product_id": 43, 
        "characteristic_id": 1, 
        "value": "შავი", 
        "value2": "black", 
        "value3": "чорний" 
    }, { 
        "product_id": 43, 
        "characteristic_id": 4, 
        "value": "18 ვატი", 
        "value2": "18 watt", 
        "value3": "18 ватт" 
    }, { 
        "product_id": 44, 
        "characteristic_id": 1, 
        "value": "წითელი", 
        "value2": "red", 
        "value3": "Червоний" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `characteristic_values[]` | collection | Collection of product characteristics consisting of: · *პროდუქტის მახასიათებლების კოლექციაა რომელიც შედგება:* |
| `characteristic_values[].product_id` | int | Product id · *პროდუქტის id* |
| `characteristic_values[].characteristic_id` | int | Characteristic id · *მახასიათებლის id* |
| `characteristic_values[].value` | string | Value of the characteristic for the given product · *მახასიათებლის მნიშვნელობა მოცემული საქონლისთვის* |
| `characteristic_values[].value2` | string | Alternative value of the characteristic for the given product · *მახასიათებლის ალტერნატიული მნიშვნელობა მოცემული საქონლისთვის* |
| `characteristic_values[].value3` | string | Alternative value of the characteristic for the given product · *მახასიათებლის ალტერნატიული მნიშვნელობა მოცემული საქონლისთვის* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getCharacteristicValuesArray

Characteristics of selected products · *შერჩეული პროდუქტის მახასიათებლები*

Fetch the characteristics of selected products · *შერჩეული პროდუქტის მახასიათებლების წამოღება*

**POST** `api/operation/getCharacteristicValuesArray`

**Request body**

```json
[ 
    43, 44 
]
```

**Response** — identical to [`getCharacteristicValues`](#getcharacteristicvalues).

> The returned collection of product characteristics is identical to the collection returned by the getCharacteristicValues method

> int[] - a collection of product Ids

---

### getPackedProducts

Products grouped together · *ერთად დაჯგუფებული პროდუქტები*

Fetch products grouped together · *ერთად დაჯგუფებული პროდუქტების წამოღება*

**GET** `api/operation/getPackedProducts`

**Response**

```json
{ 
    "pack_info": [{ 
        "product_id": 1, 
        "pack_id": 1 
    }, { 
        "product_id": 2, 
        "pack_id": 1 
    }, { 
        "product_id": 3, 
        "pack_id": 1 
    }, { 
        "product_id": 4, 
        "pack_id": 3 
    }, { 
        "product_id": 5, 
        "pack_id": 3 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `pack_info[]` | collection | Collection of products grouped together consisting of: · *ერთად დაჯგუფებული პროდუქტის კოლექციაა რომელიც შედგება:* |
| `pack_info[].product_id` | int | Product id · *პროდუქტის id* |
| `pack_info[].pack_id` | int | Grouping id · *მაჯგუფებელი id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getSubCodeTypes

Sub-code types · *ქვე კოდის ტიპები*

Fetch sub-code types · *ქვე კოდის ტიპების წამოღება*

**GET** `api/operation/getSubCodeTypes`

**Response**

```json
{ 
    "types": [{ 
        "name": "sub_column_1", 
        "header": "სერია" 
    }, { 
        "name": "sub_column_2", 
        "header": "ვადა" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `types[]` | collection | Collection of sub-code types consisting of: · *ქვე კოდის ტიპების კოლექციაა რომელიც შედგება:* |
| `types[].name` | string | Name of the sub-code type in the database (Column) · *ქვე კოდის ტიპის დასახელება მონაცემთა ბაზაში (Column)* |
| `types[].header` | string | Name given by the user to the sub-code type · *მომხმარებლის მიერ ქვე კოდის ტიპის დარქმეული სახელი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProductSubCodes

Product sub-codes · *საქონლის ქვე კოდები*

Fetch product sub-codes · *საქონლის ქვე კოდების წამოღება*

**GET** `api/operation/getProductSubCodes`

**Response**

```json
{ 
    "sub_codes": [{ 
        "product_id": 9, 
        "sub_id": 1, 
        "barcode": "", 
        "sub_columns": [{ 
            "field": "sub_column_1", 
            "value": "001" 
        }, { 
            "field": "sub_column_2", 
            "value": "2018-09-04T00:00:00" 
        }] 
    }, { 
        "product_id": 9, 
        "sub_id": 2, 
        "barcode": "", 
        "sub_columns": [{ 
            "field": "sub_column_1", 
            "value": "002" 
        }, { 
            "field": "sub_column_2", 
            "value": "2019-09-04T00:00:00" 
        }] 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `sub_codes[]` | collection | Collection of product sub-codes consisting of: · *საქონლის ქვე კოდების კოლექციაა რომელიც შედგება:* |
| `sub_codes[].product_id` | int | Product id · *საქონლის id* |
| `sub_codes[].sub_id` | int | Product sub-code id · *საქონლის ქვე კოდის id* |
| `sub_codes[].barcode` | string | Barcode of the product sub-code · *საქონლის ქვე კოდის შტრიხკოდი* |
| `sub_columns[]` | collection | Values of the product sub-code's fields, consisting of: · *საქოლის ქვე კოდის ველების მნიშვნელობები რომელიც შედგება:* |
| `sub_columns[].field` | string | Name of the product sub-code field · *საქონლის ქვე კოდის ველის დასახელება* |
| `sub_columns[].value` | object | Value of the product sub-code field · *საქონლის ქვე კოდის ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProductPlaces

Product storage places · *საქონლის შენახვის ადგილები*

Fetch product storage places · *საქონლის შენახვის ადგილის წამოღება*

**GET** `api/operation/getProductPlaces`

**Response**

```json
{ 
    "places": [{ 
        "product_id": 10, 
        "store_id": 1, 
        "place": "თარო#5" 
    }, { 
        "product_id": 10, 
        "store_id": 2, 
        "place": "" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `places[]` | collection | Collection of product storage places consisting of: · *საქონლის შენახვის ადგილის კოლექციაა რომელიც შედგება:* |
| `places[].product_id` | int | Product id · *საქონლის id* |
| `places[].store_id` | int | Store (warehouse) id · *საწყობის id* |
| `places[].place` | string | Storage place of the product in the corresponding store · *საქონლის შენახვის ადგილი შესაბამისი საწყობისთვის* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProductImages

Product images · *საქონლის სურათები*

Fetch product images · *საქონლის სურათების წამოღება*

**GET** `api/operation/getProductImages/{product}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `product` | int | The product Id · *წარმოადგენს საქონლის Id-ს* |

**Response**

```json
{ 
    "images": [{ 
        "id": 1, 
        "image": "image base64 string" 
    }, { 
        "id": 2, 
        "image": "image base64 string2" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `images[]` | collection | Collection of product images consisting of: · *საქონლის სურათების კოლექციაა რომელიც შედგება:* |
| `images[].id` | int | Product image id · *საქონლის სურათის id* |
| `images[].image` | string | Product image (base64 of byte[]) · *საქონლის სურათი (base64 of byte[]) * |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProductsImageArray

Images of selected products · *შერჩეული საქონლის სურათები*

Fetch images of selected products · *შერჩეული საქონლის სურათების წამოღება*

**POST** `api/operation/getProductsImageArray`

**Request body**

```json
[ 
    5, 9 
]
```

**Response**

```json
{ 
    "images": [{ 
        "id": 26, 
        "product_id": 5, 
        "image": "image base64 string" 
    }, { 
        "id": 27, 
        "product_id": 5, 
        "image": "image base64 string" 
    }, { 
        "id": 29, 
        "product_id": 5, 
        "image": null 
    }, { 
        "id": 31, 
        "product_id": 9, 
        "image": "image base64 string" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `images[]` | collection | Collection of selected product images consisting of: · *შერჩეული საქონლის სურათების კოლექციაა რომელიც შედგება:* |
| `images[].id` | int | Product image id · *საქონლის სურათის id* |
| `images[].product_id` | int | Product id · *საქონლის id* |
| `images[].image` | string | Product image (base64 of byte[]) · *საქონლის სურათი (base64 of byte[]) * |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> int[] - a collection of product Ids (max 20 items recommended)

---

### getProductsBarcodeArray

Barcodes of selected products · *შერჩეული საქონლის შტრიხკოდები*

Fetch barcodes of selected products · *შერჩეული საქონლის შტრიხკოდების წამოღება*

**POST** `api/operation/getProductsBarcodeArray`

**Request body**

```json
[ 
    1, 2, 3 
]
```

**Response**

```json
{ 
    "barcodes": [{ 
        "product_id": 3, 
        "barcode": "34712051673775" 
    }, { 
        "product_id": 2, 
        "barcode": "67327054128376" 
    }, { 
        "product_id": 1, 
        "barcode": "1122" 
    }, { 
        "product_id": 1, 
        "barcode": " 3333" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `barcodes[]` | collection | Collection of selected product barcodes consisting of: · *შერჩეული საქონლის შტრიხკოდების კოლექციაა რომელიც შედგება:* |
| `barcodes[].product_id` | int | Product id · *საქონლის id* |
| `barcodes[].barcode` | string | Product barcode · *საქონლის შტრიხკოდი * |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> int[] - a collection of product Ids

---

### getProductsOnWay

Pending product orders (goods in transit) · *საქონლის მომლოდინე შეკვეთები (საქონელი გზაში)*

Fetch pending product orders (goods in transit) · *საქონლის მომლოდინე შეკვეთების (საქონელი გზაში) წამოღება*

**GET** `api/operation/getProductsOnWay`

**Response**

```json
{ 
    "on_way": [{ 
        "id": 10, 
        "date": "2018-09-19", 
        "quantity": 10 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `on_way[]` | collection | Collection of pending product orders consisting of: · *საქონლის მომლოდინე შეკვეთების კოლექციაა რომელიც შედგება:* |
| `on_way[].id` | int | Product id · *საქონლის id* |
| `on_way[].date` | date | Arrival date · *ჩამოსვლის თარიღი* |
| `on_way[].quantity` | decimal | Quantity of pending goods · *მომლოდინე საქონლის რაოდენობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### saveProduct

Save a product · *საქონლის შენახვა*

Save a product (insert, update) · *საქონლის შენახვა (insert, update)*

**POST** `api/operation/saveProduct`

**Request body**

```json
{ 
    "id": 0, 
    "code": "123456-1", 
    "name": "საქონელი X", 
    "name_eng": "", 
    "name_rus": "", 
    "group_id": 11, 
    "comment": "", 
    "vat": 1, 
    "plu": 0, 
    "unit": 1,  
    "weight": 0, 
    "prices": [{ 
        "id": 3, 
        "value": 10 
    }], 
    "barcodes": [ 
        "QK124", 
        "QK125" 
    ], 
    "images": ["image base64 string"], 
    "add_fields": [{ 
        "field": "usr_column_501", 
        "value": "თეთრი" 
    }, { 
        "field": "usr_column_502", 
        "value": "XXL" 
    }] 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Product Id. (pass 0 to create a new one) · *საქონლის Id. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `code` | string[50] | Product code · *საქონლის კოდი* |
| `name` | string[200] | Name · *დასახელება* |
| `name_eng` | string[200] | Name in English · *დასახელება ინგლისურ ენაზე* |
| `name_rus` | string[200] | Name in Russian · *დასახელება რუსულ ენაზე* |
| `group_id` | int | Product group Id. (default = 11) · *საქონლის ჯგუფის Id. (სტანდარტულად = 11)* |
| `comment` | string[500] | Comment · *კომენტარი* |
| `vat` | byte | VAT type (1 - taxable, 2 - zero-rated, 3 - non-taxable) · *დღგ-ს ტიპი (1 - იბეგრება, 2 - ნულოვანი, 3 - დაუბეგრავი)* |
| `plu` | int | PLU code for weighed goods > 0 · *plu კოდი წონითი საქონლისთვის > 0* |
| `unit` | int | Unit Id · *ერთეულის Id* |
| `weight` | double | Weight · *წონა* |
| `prices[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `prices[].id` | int | Price Id · *ფასის Id* |
| `prices[].value` | double | Price value · *ფასის მნიშვნელობა* |
| `barcodes` | string[] | Collection of barcodes · *შტრიხკოდების კოლექცია* |
| `images` | string[] | Collection of images (in base64 string format) · *სურათების კოლექცია (base64 string ფორმატში)* |
| `add_fields[]` | collection | Collection of the product's additional fields, where: · *საქონლის დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value (if the prices collection is not null, the corresponding values will be assigned for this product for the price types passed). (If the barcodes collection is not null, the product's existing barcodes will be deleted and the passed values saved.) (If the images collection is not null, the product's existing images will be deleted and the passed values saved.) · *დამატებითი ველის მნიშვნელობა (თუ prices კოლექცია არ არის null მოხდება მოცემული საქონლისთვის გადმოცემული ფაისის ტიპებისთვის შესაბამისი მნიშვნელობების მინიჭება). (თუ barcodes კოლექცია არ არის null მოხდება მოცემული საქონლისთვის არსებული შტრიხკოდების წაშლა და გადმოცემული მნიშვნელობების შენახვა). (თუ images კოლექცია არ არის null მოხდება მოცემული საქონლისთვის არსებული სურათების წაშლა და გადმოცემული მნიშვნელობების შენახვა)* |

**Response**

```json
{ 
    "id": 1, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the inserted (or updated) product · *დამატებული (ან დარედაქტირებული) საქონლის Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### saveProvidedService

Save a provided service · *გაწეული მომსახურების შენახვა*

Save a provided service (insert, update) · *გაწეული მომსახურების შენახვა (insert, update)*

**POST** `api/operation/saveProvidedService`

**Request body**

```json
{ 
    "id": 0, 
    "code": "123", 
    "name": "მომსახურება X", 
    "group_id": 110, 
    "comment": "", 
    "vat": 1, 
    "unit": 1, 
    "prices": [{ 
        "id": 3, 
        "value": 100 
    }], 
    "add_fields": [{ 
        "field": "usr_column_506", 
        "value": "XYZ" 
    }] 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Product Id. (pass 0 to create a new one) · *საქონლის Id. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `code` | string[50] | Provided service code · *გაწეული მომსახურების კოდი* |
| `name` | string[200] | Name · *დასახელება* |
| `group_id` | int | Provided service group Id. (default = 110) · *გაწეული მომსახურების ჯგუფის Id. (სტანდარტულად = 110)* |
| `comment` | string[500] | Comment · *კომენტარი* |
| `vat` | byte | VAT type (1 - taxable, 2 - zero-rated, 3 - non-taxable) · *დღგ-ს ტიპი (1 - იბეგრება, 2 - ნულოვანი, 3 - დაუბეგრავი)* |
| `unit` | int | Unit Id · *ერთეულის Id* |
| `prices[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `prices[].id` | int | Price Id · *ფასის Id* |
| `prices[].value` | double | Price value · *ფასის მნიშვნელობა* |
| `add_fields[]` | collection | Collection of the product's additional fields, where: · *საქონლის დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value (if the prices collection is not null, the corresponding values will be assigned for this provided service for the price types passed) · *დამატებითი ველის მნიშვნელობა (თუ prices კოლექცია არ არის null მოხდება მოცემული გაწეული მომსახურებისთვის გადმოცემული ფაისის ტიპებისთვის შესაბამისი მნიშვნელობების მინიჭება)* |

**Response**

```json
{ 
    "id": 2, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the inserted (or updated) provided service · *დამატებული (ან დარედაქტირებული) გაწეული მომსახურების Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---
