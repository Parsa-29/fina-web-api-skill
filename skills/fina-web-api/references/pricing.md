# Prices, price types, discounts and units

8 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getProductPrices`](#getproductprices) | GET | `api/operation/getProductPrices` | Product prices |
| [`getProvidedServicePrices`](#getprovidedserviceprices) | GET | `api/operation/getProvidedServicePrices` | Provided service prices |
| [`getProductUnits`](#getproductunits) | GET | `api/operation/getProductUnits` | Additional product units |
| [`getProductPricesAdvance`](#getproductpricesadvance) | POST | `api/operation/getProductPricesAdvance` | Prices of specified products |
| [`getProductPricesAfter`](#getproductpricesafter) | GET | `api/operation/getProductPricesAfter/{after_date}` | Updated product prices |
| [`getPriceTypes`](#getpricetypes) | GET | `api/operation/getPriceTypes` | Price types |
| [`getDiscountTypes`](#getdiscounttypes) | GET | `api/operation/getDiscountTypes` | Discount kinds |
| [`getUnits`](#getunits) | GET | `api/operation/getUnits` | Units of measurement |

---

### getProductPrices

Product prices · *საქონლის ფასები*

Fetch product prices · *საქონლის ფასების წამოღება*

**GET** `api/operation/getProductPrices`

**Response**

```json
{ 
    "prices": [{ 
        "product_id": 1, 
        "price_id": 3, 
        "price": 20.0, 
        "discount_price": 7.0, 
        "currency": "GEL", 
        "discount_start": "2018-12-03T00:00:00", 
        "discount_end": "2018-12-05T00:00:00" 
    }, { 
        "product_id": 1, 
        "price_id": 4, 
        "price": 1.0, 
        "discount_price": 0.0, 
        "currency": "GEL", 
        "discount_start": null, 
        "discount_end": null 
    }, { 
        "product_id": 2, 
        "price_id": 4, 
        "price": 0.0, 
        "discount_price": 0.0, 
        "currency": "GEL", 
        "discount_start": null, 
        "discount_end": null 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `prices[]` | collection | Collection of product prices consisting of: · *საქონლის ფასების კოლექციაა რომელიც შედგება:* |
| `prices[].product_id` | int | Product id · *საქონლის id* |
| `prices[].price_id` | int | Price type id · *ფასის ტიპის id* |
| `prices[].price` | double | Product price · *საქონლის ფასი* |
| `prices[].discount_price` | double | Discounted price of the product · *საქონლის ფადაკლებული ფასი* |
| `prices[].currency` | string | Currency code · *ვალუტის კოდი* |
| `prices[].discount_start` | datetime | Discount start date · *ფასდაკლების დაწყების თარიღი* |
| `prices[].discount_end` | datetime | Discount end date · *ფასდაკლების დასრულების თარიღი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProvidedServicePrices

Provided service prices · *გაწეული მომსახურების ფასები*

Fetch provided service prices · *გაწეული მომსახურების ფასების წამოღება*

**GET** `api/operation/getProvidedServicePrices`

**Response** — identical to [`getProductPrices`](#getproductprices).

> The returned collection of provided service prices is identical to the collection returned by the getProductPrices method

---

### getProductUnits

Additional product units · *საქონლის დამატებითი ერთეულები*

Fetch additional product units · *საქონლის დამატებითი ერთეულების წამოღება*

**GET** `api/operation/getProductUnits`

**Response**

```json
{ 
  "units": [ 
    { 
      "product_id": 1, 
      "unit_id": 1, 
      "quantity": 0.5, 
      "barcode": "555", 
       "unit_prices": [ 
        { 
          "field": "unit_price_3", 
          "value": 3 
        }, 
        { 
          "field": "unit_price_4", 
          "value": 2.5 
        }, 
        { 
          "field": "unit_price_5", 
          "value": 1.5 
        } 
      ] 
    }, 
    { 
      "product_id": 10, 
      "unit_id": 2, 
      "quantity": 11, 
      "barcode": "", 
      "unit_prices": [ 
        { 
          "field": "unit_price_3", 
          "value": 3 
        }, 
        { 
          "field": "unit_price_4", 
          "value": 2.5 
        }, 
        { 
          "field": "unit_price_5", 
          "value": 1.5 
        } 
      ] 
    } 
  ], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `units[]` | collection | Collection of additional product units consisting of: · *საქონლის დამატებითი ერთეულების კოლექციაა რომელიც შედგება:* |
| `units[].product_id` | int | Product id · *საქონლის id* |
| `units[].unit_id` | int | Additional unit id · *დამატებითი ერთეულის id* |
| `units[].quantity` | double | Quantity relative to the base unit · *რაოდენობა ძირითად ერთეულთან მიმართებაში* |
| `units[].price` | double | Price relative to the base unit · *ფასი ძირითად ერთეულთან მიმართებაში* |
| `units[].barcode` | string | Barcode for the additional unit · *შტრიხკოდი დამატებიტი ერთეულისთვის* |
| `unit_prices[]` | collection | Prices relative to the base unit, consisting of: · *ფასები ძირითად ერთეულთან მიმართებაში რომელიც შედგება:* |
| `unit_prices[].field` | string | Name of the product unit price field · *საქონლის ერთეულის ფასის ველის დასახელება* |
| `unit_prices[].value` | object | Value of the product unit price field · *საქონლის ერთეულის ფასის ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `price` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getProductPricesAdvance

Prices of specified products · *მითითებული საქონლის ფასები*

Fetch product prices with the specified filter · *საქონლის ფასების წამოღება მითითებული ფილტრით*

**POST** `api/operation/getProductPricesAdvance`

**Request body**

```json
{ 
    "prods": [1, 2], 
    "price": 3 
}
```

| Field | Type | Description |
|---|---|---|
| `prods` | int[] | A collection of product Ids · *საქონლის Id -ების კოლექციაა* |
| `price` | int | Price type Id (default 3 (retail price)) · *ფასის ტიპის Id (Default -3 (საცალო ფასი))* |

**Response** — identical to [`getProductPrices`](#getproductprices).

> The returned collection of product prices is identical to the collection returned by the getProductPrices method

---

### getProductPricesAfter

Updated product prices · *განახლებული საქონლის ფასები*

Fetch changed (updated) product prices · *შეცვლილი (განახლებული) საქონლის ფასების წამოღება*

**GET** `api/operation/getProductPricesAfter/{after_date}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `after_date` | datetime | Date (yyyy-MM-ddTHH:mm:ss) after which changes are of interest · *თარიღი (yyyy-MM-ddTHH:mm:ss), რომლის შემდგომი ცვლილებებიც გვაინტერესებს* |

**Response** — identical to [`getProductPrices`](#getproductprices).

> The returned collection of product prices is identical to the collection returned by the getProductPrices method

---

### getPriceTypes

Price types · *ფასის ტიპები*

Fetch price types · *ფასის ტიპების წამოღება*

**GET** `api/operation/getPriceTypes`

**Response**

```json
{ 
    "types": [{ 
        "id": 3, 
        "name": "საცალო" 
    }, { 
        "id": 4, 
        "name": "მცირე საბითუმო" 
    }, { 
        "id": 5, 
        "name": "საბითუმოX" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `types[]` | collection | Collection of price types consisting of: · *ფასის ტიპების კოლექციაა რომელიც შედგება:* |
| `types[].id` | int | Price type Id · *ფასის ტიპის Id* |
| `types[].name` | string | Price type name · *ფასის ტიპის დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getDiscountTypes

Discount kinds · *ფასდაკლების სახეობები*

Fetch discount kinds · *ფასდაკლების სახეობების წამოღება*

**GET** `api/operation/getDiscountTypes`

**Response**

```json
{ 
    "types": [{ 
        "id": 1, 
        "discount_percent": 15.2 
    }, { 
        "id": 2, 
        "discount_percent": 10.0 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `types[]` | collection | Collection of discount kinds consisting of: · *ფასდაკლების სახეობების კოლექციაა რომელიც შედგება:* |
| `types[].id` | int | Discount kind Id · *ფასდაკლების სახეობის Id* |
| `types[].discount_percent` | double | Discount value (%) · *ფასდაკლების მნიშვნელობა(%)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getUnits

Units of measurement · *საზომი ერთეულები*

Fetch units of measurement · *საზომი ერთეულების წამოღება*

**GET** `api/operation/getUnits`

**Response**

```json
{ 
    "units": [{ 
        "id": 1, 
        "name": "ც", 
        "full_name": "ცალი" 
    }, { 
        "id": 2, 
        "name": "კგ", 
        "full_name": "კილოგრამი" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `units[]` | collection | Collection of units of measurement consisting of: · *საზომი ერთეულების კოლექციაა რომელიც შედგება:* |
| `units[].id` | int | Unit Id · *ერთეულის Id* |
| `units[].name` | string | Short name of the unit · *ერთეულის მოკლე დასახელება* |
| `units[].full_name` | string | Full name of the unit · *ერთეულის სრული დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---
