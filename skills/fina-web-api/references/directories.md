# Stores, users, staff and other directories

14 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getStoreGroups`](#getstoregroups) | GET | `api/operation/getStoreGroups` | Store groups |
| [`getStores`](#getstores) | GET | `api/operation/getStores` | Stores (warehouses) |
| [`getProjects`](#getprojects) | GET | `api/operation/getProjects` | Projects |
| [`getTerminals`](#getterminals) | GET | `api/operation/getTerminals` | POS terminals |
| [`getCashes`](#getcashes) | GET | `api/operation/getCashes` | Cash registers |
| [`getUsers`](#getusers) | GET | `api/operation/getUsers` | Users |
| [`getUserPermissions`](#getuserpermissions) | GET | `api/operation/getUserPermissions/{user}` | User permissions |
| [`getBankAccounts`](#getbankaccounts) | GET | `api/operation/getBankAccounts` | Bank accounts |
| [`getCreditBanks`](#getcreditbanks) | GET | `api/operation/getCreditBanks` | Installment banks |
| [`getStaffGroups`](#getstaffgroups) | GET | `api/operation/getStaffGroups` | Staff groups |
| [`getStaffs`](#getstaffs) | GET | `api/operation/getStaffs` | Staff members |
| [`getTransportationMeans`](#gettransportationmeans) | GET | `api/operation/getTransportationMeans` | Transportation means |
| [`getStaffAdditionalFields`](#getstaffadditionalfields) | GET | `api/operation/getStaffAdditionalFields` | Description of the staff member's additional fields |
| [`saveStaff`](#savestaff) | POST | `api/operation/saveStaff` | Save a staff member |

---

### getStoreGroups

Store groups · *საწყობის ჯგუფები*

Fetch store groups · *საწყობის ჯგუფების წამოღება*

**GET** `api/operation/getStoreGroups`

**Response**

```json
{ 
    "groups": [{ 
        "id": 2, 
        "parent_id": 1, 
        "path": "0#1#2", 
        "name": "საწყობები" 
    }, { 
        "id": 3, 
        "parent_id": 1, 
        "path": "0#1#3", 
        "name": "მაღაზიები" 
    }, { 
        "id": 4, 
        "parent_id": 1, 
        "path": "0#1#4", 
        "name": "ბორტები" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `groups[]` | collection | Collection of store groups consisting of: · *საწყობის ჯგუფების კოლექციაა რომელიც შედგება:* |
| `groups[].id` | int | Group Id · *ჯგუფის Id* |
| `groups[].parent_id` | int | Parent group Id · *მშობელი ჯგუფის Id* |
| `groups[].path` | string | Path of the group record · *ჯგუფის ჩანაწერის მისამართი* |
| `groups[].name` | string | Group name · *ჯგუფის დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getStores

Stores (warehouses) · *საწყობები*

Fetch stores · *საწყობების წამოღება*

**GET** `api/operation/getStores`

**Response**

```json
{ 
    "stores": [{ 
        "id": 1, 
        "group_id": 2, 
        "name": "მთავარი საწყობი", 
        "address": "", 
        "project_id": 1 
    }, { 
        "id": 2, 
        "group_id": 2, 
        "name": "საწყობი 2", 
        "address": "", 
        "project_id": 2 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `stores[]` | collection | Collection of stores consisting of: · *საწყობების კოლექციაა რომელიც შედგება:* |
| `stores[].id` | int | Store (warehouse) Id · *საწყობის Id* |
| `stores[].group_id` | int | Store group Id · *საწყობის ჯგუფის Id* |
| `stores[].name` | string | Store name · *საწყობის დასახელება* |
| `stores[].address` | string | Store address · *საწყობის მისამართი* |
| `stores[].project_id` | int | Project Id · *პროექტის Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProjects

Projects · *პროექტები*

Fetch projects · *პროექტების წამოღება*

**GET** `api/operation/getProjects`

**Response**

```json
{ 
    "projects": [{ 
        "id": 1, 
        "name": "ძირითადი პროექტი" 
    }, { 
        "id": 2, 
        "name": "პროექტი2" 
    }, { 
        "id": 3, 
        "name": "პროექტი3" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `projects[]` | collection | Collection of projects consisting of: · *პროექტების კოლექციაა რომელიც შედგება:* |
| `projects[].id` | int | Project Id · *პროექტის Id* |
| `projects[].name` | string | Project name · *პროექტის დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getTerminals

POS terminals · *POS ტერმინალები*

Fetch POS terminals · *POS ტერმინალების წამოღება*

**GET** `api/operation/getTerminals`

**Response**

```json
{ 
    "terminals": [{ 
        "id": 10, 
        "name": "POS 1" 
    }, { 
        "id": 14, 
        "name": "POS 2" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `terminals[]` | collection | Collection of POS terminals consisting of: · *POS ტერმინალების კოლექციაა რომელიც შედგება:* |
| `terminals[].id` | int | POS terminal Id · *POS ტერმინალის Id* |
| `terminals[].name` | string | POS terminal name · *POS ტერმინალის დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getCashes

Cash registers · *სალაროები*

Fetch cash registers · *სალაროების წამოღება*

**GET** `api/operation/getCashes`

**Response**

```json
{ 
    "cashes": [{ 
        "id": 1, 
        "name": "მთავარი სალარო" 
    }, { 
        "id": 2, 
        "name": "სალარო #2" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `cashes[]` | collection | Collection of cash registers consisting of: · *სალაროების კოლექციაა რომელიც შედგება:* |
| `cashes[].id` | int | Cash register Id · *სალაროს Id* |
| `cashes[].name` | string | Cash register name · *სალაროს დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getUsers

Users · *მომხმარებლები*

Fetch users · *მომხმარებლების წამოღება*

**GET** `api/operation/getUsers`

**Response**

```json
{ 
    "users": [{ 
        "id": 1, 
        "name": "ადმინისტრატორი ", 
        "type": 1 
    }, { 
        "id": 2, 
        "name": "სატესტო მოლარე", 
        "type": 3 
    }, { 
        "id": 3, 
        "name": "ოპერატორი ოპერატორი", 
        "type": 2 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `users[]` | collection | Collection of users consisting of: · *მომხმარებლების კოლექციაა რომელიც შედგება:* |
| `users[].id` | int | User Id · *მომხმარებლის Id* |
| `users[].name` | string | User's first and last name · *მომხმარებლის სახელი, გვარი* |
| `users[].type` | byte | User type (1 - administrator, 2 - operator, 3 - cashier operator) · *მომხმარებლის ტიპი (1 - ადმინისტრატორი, 2 - ოპერატორი, 3 - მოლარე ოპერატორი)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getUserPermissions

User permissions · *მომხმარებლის პრივილეგიები*

Fetch user permissions · *მომხმარებლის პრივილეგიების წამოღება*

**GET** `api/operation/getUserPermissions/{user}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `user` | int | The user Id · *წარმოადგენს მომხმარებლის Id-ს* |

**Response**

```json
{ 
    "permissions": { 
        "default_store": 1, 
        "default_cash": 1, 
        "default_price": 3, 
        "max_discount": 10.0, 
        "max_moneyin": 50000.0, 
        "fiscal_print": 1, 
        "stores": [1], 
        "cashes": [1], 
        "price_types": [3], 
        "users": [1, 2, 3] 
    }, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `permissions` | object | Collection of user permissions consisting of: · *მომხმარებლის პრივილეგიების კოლექციაა რომელიც შედგება:* |
| `permissions.default_store` | int | Store Id (default store for this user) · *საწყობის Id (default საწყობი მოცემული მომხმარებლისთვის)* |
| `permissions.default_cash` | int | Cash register Id (default cash register for this user) · *სალაროს Id (default სალარო მოცემული მომხმარებლისთვის)* |
| `permissions.default_price` | int | Price type Id (default price type for this user) · *ფასის ტიპის Id (default ფასის ტიპი მოცემული მომხმარებლისთვის)* |
| `permissions.max_discount` | decimal | Maximum allowed discount value (%) · *ფასდაკლების მაქსიმალურად დასაშვები მნიშვნელობა (%) * |
| `permissions.max_moneyin` | decimal | Maximum allowed amount of money received · *მიღებული თანხის მაქსიმალურად დასაშვები მნიშვნელობა * |
| `permissions.fiscal_print` | byte | Fiscal receipt printing mode (0 - do not print, 1 - detailed, 2 - total) · *ფისკალური ჩეკის ამობეჭდვის რეჟიმი (0 - არ დაიბეჭდოს, 1 - დეტალური, 2 - ჯამური)* |
| `permissions.stores` | int[] | Collection of stores this user is allowed to access · *საწყობების კოლექცია რომელთან წვდომაც დაშვებულია მოცემული მომხმარებლისთვის* |
| `permissions.cashes` | int[] | Collection of cash registers this user is allowed to access · *სალაროების კოლექცია რომელთან წვდომაც დაშვებულია მოცემული მომხმარებლისთვის* |
| `permissions.price_types` | int[] | Collection of price types this user is allowed to access (1 - purchase price, 2 - cost price, every other number >=3 is the Id of the corresponding price type) · *ფასის ტიპების კოლექცია რომელთან წვდომაც დაშვებულია მოცემული მომხმარებლისთვის (1 - მიღების ფასი, 2- თვითღირებულება, ყველა სხვა ციფრი რომელიც >=3 - შესაბამისი ფასის ტიპის Id -ა)* |
| `permissions.users` | int[] | Collection of users whose posted operations this user is allowed to access (ReadOnly) · *მომხმარებლების კოლექცია რომელთა გატარებულ ოპერაციებზეც წვდომა დაშვებულია მოცემული მომხმარებლისთვის (ReadOnly)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getBankAccounts

Bank accounts · *საბანკო ანგარიშები*

Fetch bank accounts · *საბანკო ანგარიშების წამოღება*

**GET** `api/operation/getBankAccounts`

**Response**

```json
{ 
    "accounts": [{ 
        "id": 1, 
        "code": "TBCBGE22", 
        "name": "თიბისი ბანკი", 
        "account": "GE218541545456554551", 
        "currency": "GEL" 
    }, { 
        "id": 2, 
        "code": "TBCBGE22", 
        "name": "თიბისი ბანკი", 
        "account": "GE218541545456554551", 
        "currency": "USD" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `accounts[]` | collection | Collection of bank accounts consisting of: · *საბანკო ანგარიშების კოლექციაა რომელიც შედგება:* |
| `accounts[].id` | int | Account Id · *ანგარიშის Id* |
| `accounts[].code` | string | Bank code · *ბანკის კოდი* |
| `accounts[].name` | string | Bank name · *ბანკის დასახელება* |
| `accounts[].account` | string | Account · *ანგარიში* |
| `accounts[].currency` | string | Account currency · *ანგარიშის ვალუტა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getCreditBanks

Installment banks · *განვადების ბანკები*

Fetch installment banks · *განვადების ბანკების წამოღება*

**GET** `api/operation/getCreditBanks`

**Response**

```json
{ 
    "credits": [{ 
        "id": 11, 
        "name": "PCBG განვადება" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `accounts[]` | collection | Collection of installment banks consisting of: · *განვადების ბანკების კოლექციაა რომელიც შედგება:* |
| `credits.id` | int | Installment bank Id · *განვადების ბანკის Id* |
| `credits.name` | string | Installment bank name · *განვადების ბანკის დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `credits` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `accounts` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getStaffGroups

Staff groups · *თანამშრომლის ჯგუფები*

Fetch staff groups · *თანამშრომლის ჯგუფების წამოღება*

**GET** `api/operation/getStaffGroups`

**Response**

```json
{ 
    "groups": [{ 
        "id": 2, 
        "parent_id": 1, 
        "path": "0#1#2", 
        "name": "თანამშრომლები" 
    }, { 
        "id": 3, 
        "parent_id": 2, 
        "path": "0#1#2#3", 
        "name": "level1" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `groups[]` | collection | Collection of staff groups consisting of: · *თანამშრომლის ჯგუფების კოლექციაა რომელიც შედგება:* |
| `groups[].id` | int | Group Id · *ჯგუფის Id* |
| `groups[].parent_id` | int | Parent group Id · *მშობელი ჯგუფის Id* |
| `groups[].path` | string | Path of the group record · *ჯგუფის ჩანაწერის მისამართი* |
| `groups[].name` | string | Group name · *ჯგუფის დასახელება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getStaffs

Staff members · *თანამშრომლები*

Fetch staff members · *თანამშრომლების წამოღება*

**GET** `api/operation/getStaffs`

**Response**

```json
{ 
    "staffs": [{ 
        "id": 1, 
        "group_id": 2, 
        "name": "თანამშრომელი1", 
        "private_num": "11111111111", 
        "passport_num": "xx123465", 
        "address": "მისამართი", 
        "tel": "+99500000000", 
        "comment": "დამატებითი ინფორმაცია", 
        "add_fields": [{ 
            "field": "usr_column_507", 
            "value": "30" 
        }] 
    }, { 
        "id": 5, 
        "group_id": 2, 
        "name": "თანამშრომელი2", 
        "private_num": "11111111112", 
        "passport_num": "xx1234652", 
        "address": "მისამართი2", 
        "tel": "+99500000002", 
        "comment": "დამატებითი ინფორმაცია2", 
        "add_fields": [{ 
            "field": "usr_column_507", 
            "value": "30" 
        }] 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `staffs[]` | collection | Collection of staff members consisting of: · *თანამშრომლების კოლექციაა რომელიც შედგება:* |
| `staffs[].id` | int | Staff member Id · *თანამშრომლის Id* |
| `staffs[].group_id` | int | Staff group Id · *თანამშრომლის ჯგუფის Id* |
| `staffs[].name` | string | Staff member name · *თანამშრომლის დასახელება* |
| `staffs[].private_num` | string | Staff member's personal number · *თანამშრომლის პირადი ნომერი* |
| `staffs[].passport_num` | string | Staff member's passport number · *თანამშრომლის პასპორტის ნომერი* |
| `staffs[].address` | string | Staff member's address · *თანამშრომლის მისამართი* |
| `staffs[].tel` | string | Staff member's phone · *თანამშრომლის ტელეფონი* |
| `staffs[].comment` | string | Comment · *კომენტარი* |
| `add_fields[]` | collection | Collection of the staff member's additional fields, where: · *თანამშრომლის დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getTransportationMeans

Transportation means · *სატრანსპორტო საშუალებები*

Fetch transportation means · *სატრანსპორტო საშუალებების წამოღება*

**GET** `api/operation/getTransportationMeans`

**Response**

```json
{ 
  "transportation_means": [ 
    { 
      "id": 1, 
      "model": "alfa", 
      "num": "xx123yy", 
      "driver_name": "nika", 
      "driver_num": "0101020203", 
      "fuel_consumption": 12, 
      "consumption_type": 0, 
      "staff_id": 1, 
      "trailer": "მისაბმელი" 
    } 
  ], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `transportation_means[]` | collection | Collection of transportation means consisting of: · *სატრანსპორტო საშუალების კოლექციაა რომელიც შედგება:* |
| `transportation_means[].id` | int | Transportation means Id · *სატრანსპორტო საშუალების Id* |
| `transportation_means[].model` | string | Make of the transportation means · *სატრანსპორტო საშუალების მარკა* |
| `transportation_means[].num` | string | Number of the transportation means · *სატრანსპორტო საშუალების ნომერი* |
| `transportation_means[].driver_name` | string | Driver's first and last name · *მძღოლის სახელი, გვარი* |
| `transportation_means[].fuel_consumption` | double | Fuel consumption · *საწვავის ხარჯი* |
| `transportation_means[].consumption_type` | byte | Fuel consumption type (0 - consumption per 100 km; 1 - consumption per hour) · *საწვავის ხარჯის ტიპი (0 - ხარჯი 100კმ-ზე; 1 - ხარჯი საათში)* |
| `transportation_means[].staff_id` | int | Staff member Id · *თანამშრომლის Id* |
| `transportation_means[].trailer` | string | Trailer · *მისაბმელი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `driver_num` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---

### getStaffAdditionalFields

Description of the staff member's additional fields · *თანამშრომლის დამატებითი ველების აღწერა*

Fetch the description of the staff member's additional fields · *თანამშრომლის დამატებითი ველების აღწერის წამოღება*

**GET** `api/operation/getStaffAdditionalFields`

**Response**

```json
{ 
    "fields": [{ 
        "name": "usr_column_507", 
        "header": "ასაკი" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `fields[]` | collection | Collection describing the staff member's additional fields consisting of: · *თანამშრომლის დამატებითი ველების აღწერის კოლექციაა რომელიც შედგება:* |
| `fields[].name` | string | Name of the staff member's additional field in the database (Column) · *თანამშრომლის დამატებითი ველის დასახელება მონაცემთა ბაზაში (Column)* |
| `fields[].header` | string | Name given by the staff member to the customer's additional field · *თანამშრომლის მიერ მყიდველის დამატებითი ველისთვის დარქმეული სახელი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### saveStaff

Save a staff member · *თანამშრომლის შენახვა*

Save a staff member (insert, update) · *თანამშრომლის შენახვა (insert, update)*

**POST** `api/operation/saveStaff`

**Request body**

```json
{ 
     "id": 0, 
     "group_id": 2, 
     "name": "თანამშრომელი X", 
     "private_num": "1122332211", 
     "address": "", 
     "tel": "+995551000", 
     "comment": "კომენტარი", 
     "add_fields": [{ 
         "field": "usr_column_508", 
         "value": "დამატებით ველი2 " 
     }] 
 }
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Staff member Id. (pass 0 to create a new one) · *თანამშრომლის Id. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `group_id` | int | Staff group Id. (default = 2) · *თანამშრომლის ჯგუფის Id. (სტანდარტულად = 2)* |
| `name` | string[200] | Name · *დასახელება* |
| `private_num` | string[50] | Personal number · *პირადი ნომერი* |
| `address` | string[200] | Address · *მისამართი* |
| `tel` | string[200] | Phone · *ტელეფონი* |
| `comment` | string[200] | Comment · *კომენტარი* |
| `add_fields[]` | collection | Collection of the staff member's additional fields, where: · *თანამშრომლის დამატებითი ველების კოლექცია სადაც:* |
| `add_fields[].field` | string | Additional field name · *დამატებითი ველის დასახელება* |
| `add_fields[].value` | string | Additional field value · *დამატებითი ველის მნიშვნელობა* |

**Response**

```json
{ 
    "id": 1, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the inserted (or updated) staff member · *დამატებული (ან დარედაქტირებული) თანამშრომლის Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---
