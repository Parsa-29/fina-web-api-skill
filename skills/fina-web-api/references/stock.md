# Stock balances and cost

13 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getProductsRest`](#getproductsrest) | GET | `api/operation/getProductsRest` | Current product stock balance for each store |
| [`getProductsRestAfter`](#getproductsrestafter) | GET | `api/operation/getProductsRestAfter/{after_date}` | Current stock balance for products involved in a changed operation, for each store |
| [`getProductsRestArray`](#getproductsrestarray) | POST | `api/operation/getProductsRestArray` | Current stock balance of selected products for each store |
| [`getProductsRestByStore`](#getproductsrestbystore) | GET | `api/operation/getProductsRestByStore/{store}` | Current product stock balance for a specific store |
| [`getProductsRestSummary`](#getproductsrestsummary) | POST | `api/operation/getProductsRestSummary` | Total product stock balance |
| [`getProductsRestByStoreAfter`](#getproductsrestbystoreafter) | GET | `api/operation/getProductsRestByStoreAfter/{store}/{after_date}` | Current stock balance for products involved in a changed operation, for a specific store |
| [`getProductsRestAdvance`](#getproductsrestadvance) | POST | `api/operation/getProductsRestAdvance` | Current product stock balance with price |
| [`getSubProductsRest`](#getsubproductsrest) | GET | `api/operation/getSubProductsRest` | Current stock balance of product sub-codes for each store |
| [`getInventoriesRest`](#getinventoriesrest) | GET | `api/operation/getInventoriesRest` | Current fixed asset stock balance for each store |
| [`getInventoriesRestArray`](#getinventoriesrestarray) | POST | `api/operation/getInventoriesRestArray` | Current stock balance of selected fixed assets for each store |
| [`getInventoriesRestByStore`](#getinventoriesrestbystore) | GET | `api/operation/getInventoriesRestByStore/{store}` | Current fixed asset stock balance for a specific store |
| [`getInventoriesRestAdvance`](#getinventoriesrestadvance) | POST | `api/operation/getInventoriesRestAdvance` | Current fixed asset stock balance with price |
| [`getProductsSelfCost`](#getproductsselfcost) | POST | `api/operation/getProductsSelfCost` | Product cost price |

---

### getProductsRest

Current product stock balance for each store · *საქონლის მიმდინარე ნაშთი თითოეული საწყობისთვის*

Fetch current product stock balances (for each store) · *საქონლის მიმდინარე ნაშთის წამოღება (თითოეული საწყობისთვის)*

**GET** `api/operation/getProductsRest`

**Response**

```json
{ 
    "rest": [{ 
        "id": 1, 
        "store": 1, 
        "rest": 0, 
        "reserve": 2 
    }, { 
        "id": 1, 
        "store": 2, 
        "rest": 1, 
        "reserve": 0 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `rest[]` | collection | Collection of product stock balances consisting of: · *საქონლის ნაშთის კოლექციაა რომელიც შედგება:* |
| `rest[].id` | int | Product Id · *საქონლის Id* |
| `rest[].store` | int | Store (warehouse) Id · *საწყობის Id* |
| `rest[].rest` | decimal | Product stock balance (taking the reserve into account) · *საქონლის ნაშთი (რეზერვის გათვალისწინებით)* |
| `rest[].reserve` | decimal | Product reserve · *საქონლის რეზერვი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProductsRestAfter

Current stock balance for products involved in a changed operation, for each store · *ოპერაციაში ცვლილების მონაწილე საქონლის მიმდინარე ნაშთი თითოეული საწყობისთვის*

Fetch current stock balances for products involved in a changed operation (for each store) · *ოპერაციაში ცვლილების მონაწილე საქონლის მიმდინარე ნაშთის წამოღება (თითოეული საწყობისთვის)*

**GET** `api/operation/getProductsRestAfter/{after_date}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `after_date` | datetime | Date (yyyy-MM-ddTHH:mm:ss) after which the stock balances of products involved in changes are of interest · *თარიღი (yyyy-MM-ddTHH:mm:ss), რომლის შემდგომი ცვლილებების მონაწილე საქონლის ნაშთიც გვაინტერესებს* |

**Response** — identical to [`getProductsRest`](#getproductsrest).

> The returned collection of product stock balances is structurally identical to the collection returned by the getProductsRest method

---

### getProductsRestArray

Current stock balance of selected products for each store · *შერჩეული საქონლის მიმდინარე ნაშთი თითოეული საწყობისთვის*

Fetch current stock balances of selected products (for each store) · *შერჩეული საქონლის მიმდინარე ნაშთის წამოღება (თითოეული საწყობისთვის)*

**POST** `api/operation/getProductsRestArray`

**Request body**

```json
{ 
    "prods": [1, 2] 
}
```

| Field | Type | Description |
|---|---|---|
| `prods` | int[] | A collection of product Ids · *საქონლის Id -ების კოლექციაა* |

**Response** — identical to [`getProductsRest`](#getproductsrest).

> The returned collection of product stock balances is structurally identical to the collection returned by the getProductsRest method

---

### getProductsRestByStore

Current product stock balance for a specific store · *საქონლის მიმდინარე ნაშთი კონკრეტული საწყობისთვის*

Fetch current product stock balances (for a specific store) · *საქონლის მიმდინარე ნაშთის წამოღება (კონკრეტული საწყობისთვის)*

**GET** `api/operation/getProductsRestByStore/{store}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `store` | int | The store (warehouse) Id · *წარმოადგენს საწყობის Id-ს* |

**Response**

```json
{ 
    "store_rest": [{ 
        "id": 1, 
        "rest": 0 
    }, { 
        "id": 2, 
        "rest": 1 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `store_rest[]` | collection | Collection of product stock balances consisting of: · *საქონლის ნაშთის კოლექციაა რომელიც შედგება:* |
| `store_rest[].id` | int | Product Id · *საქონლის Id* |
| `store_rest[].rest` | decimal | Product stock balance in the specified store · *საქონლის ნაშთი მითითებულ საწყობში* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProductsRestSummary

Total product stock balance · *საქონლის ჯამური ნაშთი*

Fetch total product stock balances · *საქონლის ჯამური ნაშთის წამოღება*

**POST** `api/operation/getProductsRestSummary`

**Request body**

```json
{ 
    "prods": [1, 2], 
    "stores": [1, 2, 3], 
    "date": "2025-11-05T20:25:10" 
}
```

| Field | Type | Description |
|---|---|---|
| `date` | datetime | Date (yyyy-MM-ddTHH:mm:ss) for which the product stock balance is of interest · *თარიღი (yyyy-MM-ddTHH:mm:ss), რომლისთვისაც გვაინტერესებს საქონლის ნაშთი* |

**Response**

```json
{ 
    "store_rest": [{ 
        "id": 1, 
        "rest": 0 
    }, { 
        "id": 2, 
        "rest": 1 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `store_rest[]` | collection | Collection of product stock balances consisting of: · *საქონლის ნაშთის კოლექციაა რომელიც შედგება:* |
| `store_rest[].id` | int | Product Id · *საქონლის Id* |
| `store_rest[].rest` | decimal | Total product stock balance in the specified stores · *საქონლის ჯამური ნაშთი მითითებულ საწყობებში* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `prods`, `stores` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---

### getProductsRestByStoreAfter

Current stock balance for products involved in a changed operation, for a specific store · *ოპერაციაში ცვლილების მონაწილე საქონლის მიმდინარე ნაშთი კონკრეტული საწყობისთვის*

Fetch current stock balances for products involved in a changed operation (for a specific store) · *ოპერაციაში ცვლილების მონაწილე საქონლის მიმდინარე ნაშთის წამოღება (კონკრეტული საწყობისთვის)*

**GET** `api/operation/getProductsRestByStoreAfter/{store}/{after_date}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `store` | int | The store (warehouse) Id · *წარმოადგენს საწყობის Id-ს* |
| `after_date` | datetime | Date (yyyy-MM-ddTHH:mm:ss) after which the stock balances of products involved in changes are of interest · *თარიღი (yyyy-MM-ddTHH:mm:ss), რომლის შემდგომი ცვლილებების მონაწილე საქონლის ნაშთიც გვაინტერესებს* |

**Response** — identical to [`getProductsRestByStore`](#getproductsrestbystore).

> The returned collection of product stock balances is structurally identical to the collection returned by the getProductsRestByStore method

---

### getProductsRestAdvance

Current product stock balance with price · *საქონლის მიმდინარე ნაშთი ფასით*

Fetch current product stock balances together with prices (for a specific store) · *საქონლის მიმდინარე ნაშთის და ფასის წამოღება (კონკრეტული საწყობისთვის)*

**POST** `api/operation/getProductsRestAdvance`

**Request body**

```json
{ 
    "prods": [1, 2], 
    "store": 1, 
    "price": 3 
}
```

| Field | Type | Description |
|---|---|---|
| `prods` | int[] | A collection of product Ids · *საქონლის Id -ების კოლექციაა* |
| `store` | int | Store Id (0 - all stores combined) · *საწყობის Id (0 - ყველა საწყობში ერთად აღებული)* |
| `price` | int | Price type Id (default 3 (retail price)) · *ფასის ტიპის Id (Default -3 (საცალო ფასი))* |

**Response**

```json
{ 
    "rest_info": [{ 
        "id": 1, 
        "rest": 0, 
        "price": 7.25 
    }, { 
        "id": 2, 
        "rest": 1, 
        "price": 2.5 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `rest_info[]` | collection | Collection of product stock balances consisting of: · *საქონლის ნაშთის კოლექციაა რომელიც შედგება:* |
| `rest_info[].id` | int | Product Id · *საქონლის Id* |
| `rest_info[].rest` | decimal | Product stock balance in the specified store · *საქონლის ნაშთი მითითებულ საწყობში* |
| `rest_info[].price` | double | Selling price of the product · *საქონლის გასაყიდი ფასი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getSubProductsRest

Current stock balance of product sub-codes for each store · *საქონლის ქვე კოდების მიმდინარე ნაშთი თითოეული საწყობისთვის*

Fetch current stock balances of product sub-codes (for each store) · *საქონლის ქვე კოდების მიმდინარე ნაშთის წამოღება (თითოეული საწყობისთვის)*

**GET** `api/operation/getSubProductsRest`

**Response**

```json
{ 
    "rest": [{ 
        "id": 9, 
        "sub_id": 1, 
        "store": 1, 
        "rest": 6, 
        "reserve": 0 
    }, { 
        "id": 9, 
        "sub_id": 1, 
        "store": 2, 
        "rest": 0, 
        "reserve": 0 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `rest[]` | collection | Collection of product stock balances consisting of: · *საქონლის ნაშთების კოლექციაა რომელიც შედგება:* |
| `rest[].id` | int | Product Id · *საქონლის Id* |
| `rest[].sub_id` | int | Product sub-code Id · *საქონლის ქვე კოდის Id* |
| `rest[].store` | int | Store (warehouse) Id · *საწყობის Id* |
| `rest[].rest` | decimal | Stock balance of the product sub-code (taking the reserve into account) · *საქონლის ქვე კოდის ნაშთი (რეზერვის გათვალისწინებით)* |
| `rest[].reserve` | decimal | Reserve of the product sub-code · *საქონლის ქვე კოდის რეზერვი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getInventoriesRest

Current fixed asset stock balance for each store · *ძირითადი საშუალების მიმდინარე ნაშთი თითოეული საწყობისთვის*

Fetch current fixed asset stock balances (for each store) · *ძ/ს მიმდინარე ნაშთის წამოღება (თითოეული საწყობისთვის)*

**GET** `api/operation/getInventoriesRest`

**Response**

```json
{ 
    "rest": [{ 
        "id": 14, 
        "store": 1, 
        "rest": 0, 
        "reserve": 2 
    }, { 
        "id": 14, 
        "store": 2, 
        "rest": 1, 
        "reserve": 0 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `rest[]` | collection | Collection of fixed asset stock balances consisting of: · *ძირითადი საშუალების ნაშთის კოლექციაა რომელიც შედგება:* |
| `rest[].id` | int | Fixed asset Id · *ძირითადი საშუალების Id* |
| `rest[].store` | int | Store (warehouse) Id · *საწყობის Id* |
| `rest[].rest` | decimal | Fixed asset stock balance (taking the reserve into account) · *ძირითადი საშუალების ნაშთი (რეზერვის გათვალისწინებით)* |
| `rest[].reserve` | decimal | Fixed asset reserve · *ძირითადი საშუალების რეზერვი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getInventoriesRestArray

Current stock balance of selected fixed assets for each store · *შერჩეული ძირითადი საშუალების მიმდინარე ნაშთი თითოეული საწყობისთვის*

Fetch current stock balances of selected fixed assets (for each store) · *შერჩეული ძ/ს მიმდინარე ნაშთის წამოღება (თითოეული საწყობისთვის)*

**POST** `api/operation/getInventoriesRestArray`

**Request body**

```json
{ 
    "prods": [14, 21] 
}
```

| Field | Type | Description |
|---|---|---|
| `prods` | int[] | A collection of fixed asset Ids · *ძირითადი საშუალების Id -ების კოლექციაა* |

**Response** — identical to [`getInventoriesRest`](#getinventoriesrest).

> The returned collection of fixed asset stock balances is identical to the collection returned by the getInventoriesRest method

---

### getInventoriesRestByStore

Current fixed asset stock balance for a specific store · *ძირითადი საშუალების მიმდინარე ნაშთი კონკრეტული საწყობისთვის*

Fetch current fixed asset stock balances (for a specific store) · *ძ/ს მიმდინარე ნაშთის წამოღება (კონკრეტული საწყობისთვის)*

**GET** `api/operation/getInventoriesRestByStore/{store}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `store` | int | The store (warehouse) Id · *წარმოადგენს საწყობის Id-ს* |

**Response**

```json
{ 
    "store_rest": [{ 
        "id": 14, 
        "rest": 0 
    }, { 
        "id": 21, 
        "rest": 1 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `store_rest[]` | collection | Collection of fixed asset stock balances consisting of: · *ძირითადი საშუალების ნაშთის კოლექციაა რომელიც შედგება:* |
| `store_rest[].id` | int | Fixed asset Id · *ძირითადი საშუალების Id* |
| `store_rest[].rest` | decimal | Fixed asset stock balance in the specified store · *ძირითადი საშუალების ნაშთი მითითებულ საწყობში* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getInventoriesRestAdvance

Current fixed asset stock balance with price · *ძირითადი საშუალების მიმდინარე ნაშთი ფასით*

Fetch current fixed asset stock balances together with prices (for a specific store) · *ძ/ს მიმდინარე ნაშთის და ფასის წამოღება (კონკრეტული საწყობისთვის)*

**POST** `api/operation/getInventoriesRestAdvance`

**Request body**

```json
{ 
    "prods": [1, 2], 
    "store": 1, 
    "price": 3 
}
```

| Field | Type | Description |
|---|---|---|
| `prods` | int[] | A collection of fixed asset Ids · *ძირითადი საშუალების Id -ების კოლექციაა* |
| `store` | int | Store Id (0 - all stores combined) · *საწყობის Id (0 - ყველა საწყობში ერთად აღებული)* |
| `price` | int | Price type Id (default 3 (retail price)) · *ფასის ტიპის Id (Default -3 (საცალო ფასი))* |

**Response**

```json
{ 
    "rest_info": [{ 
        "id": 1, 
        "rest": 0, 
        "price": 7.25 
    }, { 
        "id": 2, 
        "rest": 1, 
        "price": 2.5 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `rest_info[]` | collection | Collection of fixed asset stock balances consisting of: · *ძირითადი საშუალების ნაშთის კოლექციაა რომელიც შედგება:* |
| `rest_info[].id` | int | Fixed asset Id · *ძირითადი საშუალების Id* |
| `rest_info[].rest` | decimal | Fixed asset stock balance in the specified store · *ძირითადი საშუალების ნაშთი მითითებულ საწყობში* |
| `rest_info[].price` | double | Selling price of the fixed asset · *ძირითადი საშუალების გასაყიდი ფასი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProductsSelfCost

Product cost price · *საქონლის თვითღირებულება*

Fetch product cost price (AVERAGE) · *საქონლის თვითღირებულების (AVERAGE) წამოღება*

**POST** `api/operation/getProductsSelfCost`

**Request body**

```json
{ 
    "prods": [1, 2], 
    "date": "2018-11-15T23:59:59" 
}
```

| Field | Type | Description |
|---|---|---|
| `prods` | int[] | A collection of product Ids · *საქონლის Id -ების კოლექციაა* |
| `date` | datetime | Date for which the cost price is calculated · *თარიღი, რა დროისთვისაც ხდება თვითღირებულების გამოთვლა* |

**Response**

```json
{ 
    "cost_info": [{ 
        "id": 1, 
        "cost": 32.751412429378533 
    }, { 
        "id": 2, 
        "cost": 4.0 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `cost_info[]` | collection | Collection of product cost prices consisting of: · *საქონლის თვითღირებულების კოლექციაა რომელიც შედგება:* |
| `cost_info[].id` | int | Product Id · *საქონლის Id* |
| `cost_info[].cost` | double | Product cost price · *საქონლის თვითღირებულება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---
