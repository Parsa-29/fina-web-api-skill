# Writing documents — production

2 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`saveDocProduction`](#savedocproduction) | POST | `api/operation/saveDocProduction` | Production of goods |
| [`saveDocAdvProduction`](#savedocadvproduction) | POST | `api/operation/saveDocAdvProduction` | Complex production/disassembly of goods |

---

### saveDocProduction

Production of goods · *საქონლის წარმოება*

Save a production of goods (insert, update) · *საქონლის წარმოების შენახვა (insert, update)*

**POST** `api/operation/saveDocProduction`

**Request body**

```json
{ 
    "id": 0, 
    "date": "2026-03-03T13:00:00", 
    "num_pfx": "", 
    "num": 0, 
    "purpose": "წარმოება", 
    "type": 0, 
    "store": 1, 
    "user": 2, 
    "staff": 3, 
    "make_entry": true, 
    "add_fields": [{ 
        "field": "usr_column_526", 
        "value": "test string123" 
    }], 
      "products": [{ 
      "id": 107, 
      "sub_id": 0, 
      "quantity": 1, 
      "child_products": [{ 
          "id": 27, 
          "sub_id": 0, 
          "quantity": 2, 
          "price": 0 
        }, { 
          "id": 28, 
          "sub_id": 0, 
          "quantity": 3, 
          "price": 0 
        } ] 
    } ] 
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
| `type` | int | Production type (0 - production; 1 - disassembly; 2 - adding a part, repair; 3 - separating a part) · *წარმოების ტიპი (0 - წარმოება; 1 - დაშლა; 2 - ნაწილის დამატება, რემონტი, 3 - ნაწილის გამოყოფა)* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `staff` | int | Staff member Id (0 = take the staff member linked to the user) · *თანამშრომლის Id (0 = მომხმარებელზე მიბმული თანამშრომლის აღება)* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |
| `add_fields[]` | collection | Collection of additional fields, where: · *დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `products[]` | collection | Collection consisting of: · *კოლექცია შედგება:* |
| `products[].id` | int | Product Id · *საქონლის Id* |
| `products[].sub_id` | int | Product sub-code Id (default=0) · *საქონლის ქვე-კოდის Id, (default=0)* |
| `products[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `products[].child_products[]` | collection | Composition of the goods (calculation) consisting of: · *საქონლის შემცველობა, კალკულაცია რომელიც შედგება:* |
| `products[].child_products[].id` | int | Id of the component product · *შემცველი საქონლის Id* |
| `products[].child_products[].sub_id` | int | Sub-code Id of the component product (default=0) · *შემცველი საქონლის ქვე-კოდის Id, (default=0)* |
| `products[].child_products[].quantity` | decimal | Quantity of the component product per unit · *შემცველი საქონლის რაოდენობა ერთ ერთეულზე* |
| `products[].child_products[].price` | decimal | Value of the component product per unit (used for production types 1 - disassembly; 3 - separating a part) · *შემცველი საქონლის ღირებულება ერთ ერთეულზე (გამოიყენება წარმოების ტიპებისთვის 1 - დაშლა; 3 - ნაწილის გამოყოფა)* |

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

### saveDocAdvProduction

Complex production/disassembly of goods · *საქონლის რთული წარმოება/დაშლა*

Save a complete production/disassembly of goods (insert, update) · *საქონლის სრული წარმოება/დაშლის შენახვა (insert, update)*

**POST** `api/operation/saveDocAdvProduction`

**Request body**

```json
{ 
  "id": 0, 
  "date": "2026-06-25T14:17:45", 
  "num_pfx": "", 
  "num": 3, 
  "purpose": "რთული წარმოება/დაშლა", 
  "store": 1, 
  "portion": 2, 
  "user": 1, 
  "make_entry": true, 
  "materials": [{ 
      "id": 0, 
      "quantity": 0 
    }], 
  "products": [{ 
      "id": 0, 
      "quantity": 0, 
      "cost_percent": 0 
    } ] 
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
| `portion` | decimal | Quantity · *რაოდენობა* |
| `user` | int | User (creator) Id · *მომხმარებლის (შემქმნელი) Id* |
| `make_entry` | bool | Whether to post the accounting entry · *შესრულდეს თუ არა ბუღალტრული გატარება* |
| `materials[]` | collection | Collection to be consumed/disassembled consisting of: · *გასახარჯი/დასაშლელი კოლექცია შედგება:* |
| `materials[].id` | int | Product Id · *საქონლის Id* |
| `materials[].quantity` | decimal | Product quantity · *საქონლის რაოდენობა* |
| `products[]` | collection | Collection of produced products consisting of: · *ნაწარმოები საქონლის კოლექცია შედგება:* |
| `products[].id` | int | Id of the produced goods · *ნაწარმოები საქონლის Id* |
| `products[].quantity` | decimal | Quantity of the produced goods · *ნაწარმოები საქონლის რაოდენობა* |
| `products[].cost_percent` | decimal | Percentage of cost price from the goods being disassembled attributed to the produced goods · *დასაშლელი საქონლიდან თ/ღ პროცენტული მნიშვნელობა ნაწარმოები საქონლისთვის* |

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
