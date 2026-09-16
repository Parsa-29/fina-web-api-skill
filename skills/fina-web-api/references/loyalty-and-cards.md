# Gift cards, bonus cards and loyalty

15 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getGiftCards`](#getgiftcards) | GET | `api/operation/getGiftCards` | Gift cards |
| [`getGiftCardInfoByCode`](#getgiftcardinfobycode) | GET | `api/operation/getGiftCardInfoByCode/{code}` | Gift card information |
| [`getBonusCoeff`](#getbonuscoeff) | GET | `api/operation/getBonusCoeff` | Bonus coefficient |
| [`getLoyaltyCardsByHolder`](#getloyaltycardsbyholder) | GET | `api/operation/getLoyaltyCardsByHolder/{holder_code}` | Loyalty cards |
| [`getBonusCardRestByCode`](#getbonuscardrestbycode) | GET | `api/operation/getBonusCardRestByCode/{code}` | Bonus card balance |
| [`getLoyaltyCustomers`](#getloyaltycustomers) | GET | `api/operation/getLoyaltyCustomers` | Loyalty (Cloud) cards |
| [`getLoyaltyCustomer`](#getloyaltycustomer) | GET | `api/operation/getLoyaltyCustomer/{id}` | Loyalty (Cloud) card |
| [`getLoyaltyCustomerPrograms`](#getloyaltycustomerprograms) | GET | `api/operation/getLoyaltyCustomerPrograms` | Loyalty (Cloud) programs |
| [`getLoyaltyCustomerGroups`](#getloyaltycustomergroups) | GET | `api/operation/getLoyaltyCustomerGroups` | Loyalty (Cloud) groups |
| [`getLoyaltyCustomerBalances`](#getloyaltycustomerbalances) | GET | `api/operation/getLoyaltyCustomerBalances` | Loyalty (Cloud) card balances |
| [`getLoyaltyCustomerBalance`](#getloyaltycustomerbalance) | GET | `api/operation/getLoyaltyCustomerBalance/{qr_code}` | Loyalty (Cloud) card balance |
| [`getLoyaltyBonusHistory`](#getloyaltybonushistory) | GET | `api/operation/getLoyaltyBonusHistory/{qr_code}` | Loyalty (Cloud) card accrual/spending history |
| [`saveLoyaltyCustomer`](#saveloyaltycustomer) | POST | `api/operation/saveLoyaltyCustomer` | Save a loyalty (Cloud) card |
| [`saveLoyaltyGroup`](#saveloyaltygroup) | POST | `api/operation/saveLoyaltyGroup` | Save a loyalty (Cloud) group |
| [`saveLoyaltyBonusPoint`](#saveloyaltybonuspoint) | POST | `api/operation/saveLoyaltyBonusPoint` | Grant / deduct loyalty (Cloud) points |

---

### getGiftCards

Gift cards · *სასაჩუქრე ბარათები*

Fetch gift cards · *სასაჩუქრე ბარათების წამოღება*

**GET** `api/operation/getGiftCards`

**Response**

```json
{ 
  "gifts": [ 
    { 
      "id": 513449, 
      "store": 27, 
      "code": "0067631", 
      "acc": "3121", 
      "issuance_date": "2017-01-01 11:50:17", 
      "amount": 200, 
      "pay_amount": 200, 
      "rest_amount": 85 
    }, 
    { 
      "id": 513451, 
      "store": 2, 
      "code": "0069342", 
      "acc": "3121", 
      "issuance_date": "2017-01-01 13:35:27", 
      "amount": 200, 
      "pay_amount": 200, 
      "rest_amount": 200 
    } 
  ], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `gifts[]` | collection | Collection of gift cards consisting of: · *სასაჩუქრე ბარათების კოლექციაა რომელიც შედგება:* |
| `gifts[].id` | int | Card Id · *ბარათის Id* |
| `gifts[].store` | int | Id of the issuing shop (store) · *გამცემი მაღაზიის (საწყობის) Id* |
| `gifts[].code` | string | Card code · *ბარათის კოდი* |
| `gifts[].acc` | string | Accounting account of the card · *ბარათის ბუღალტრული ანგარიში* |
| `gifts[].issuance_date` | datetime | Issue date · *გაცემის თარიღი* |
| `gifts[].amount` | decimal | Gift card value · *სასაჩუქრე ბარათის ღირებულება* |
| `gifts[].pay_amount` | decimal | Amount actually paid · *რეალურად გადახდილი თანხა* |
| `gifts[].rest_amount` | decimal | Balance available on the card · *ბარათზე არსებული ნაშთი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getGiftCardInfoByCode

Gift card information · *სასაჩუქრე ბარათის ინფორმაცია*

Fetch gift card information by card code · *სასაჩუქრე ბარათის ინფორმაციის წამოღება ბარათის კოდის მიხედვით*

**GET** `api/operation/getGiftCardInfoByCode/{code}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `code` | string | The gift card code · *წარმოადგენს სასაჩუქრე ბარათის კოდს* |

**Response**

```json
{ 
  "gift": { 
    "id": 100009, 
    "store": 1, 
    "code": "IQ41", 
    "acc": "3121", 
    "issuance_date": "2024-05-21 10:37:56", 
    "amount": 100, 
    "pay_amount": 100, 
    "rest_amount": 85 
  }, 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `gift` | object | Gift card object consisting of: · *სასაჩუქრე ბარათის ობიექტია რომელიც შედგება:* |
| `gift.id` | int | Card Id · *ბარათის Id* |
| `gift.store` | int | Id of the issuing shop (store) · *გამცემი მაღაზიის (საწყობის) Id* |
| `gift.code` | string | Card code · *ბარათის კოდი* |
| `gift.acc` | string | Accounting account of the card · *ბარათის ბუღალტრული ანგარიში* |
| `gift.issuance_date` | datetime | Issue date · *გაცემის თარიღი* |
| `gift.amount` | decimal | Gift card value · *სასაჩუქრე ბარათის ღირებულება* |
| `gift.pay_amount` | decimal | Amount actually paid · *რეალურად გადახდილი თანხა* |
| `gift.rest_amount` | decimal | Balance available on the card · *ბარათზე არსებული ნაშთი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getBonusCoeff

Bonus coefficient · *ბონუსის კოეფიციენტი*

Fetch the bonus coefficient · *ბონუს კოეფიციენტის წამოღება*

**GET** `api/operation/getBonusCoeff`

**Response**

```json
{ 
    "coeff": 1.8, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `coeff` | double | The bonus coefficient · *წარმოადგენს ბონუს კოეფიციენტს* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getLoyaltyCardsByHolder

Loyalty cards · *ლოიალობის ბარათები*

Fetch (active) loyalty cards by the holder's identification code. · *ლოიალობის ბარათების (აქტიური) წამოღება მფლობელის ს/კ მიხედვით.*

**GET** `api/operation/getLoyaltyCardsByHolder/{holder_code}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `holder_code` | string | The holder's identification code · *წარმოადგენს მფლობელის საიდენტიფიკაციო კოდს* |

**Response**

```json
{ 
    "cards": [{ 
        "id": 2013, 
        "holder_id": 41, 
        "type_id": 1, 
        "discount_id": 0, 
        "price_id": 0, 
        "code": "BC123", 
        "info_code": "", 
        "info_name": "", 
        "info_address": "", 
        "info_tel": "" 
    }, { 
        "id": 2014, 
        "holder_id": 41, 
        "type_id": 2, 
        "discount_id": 2, 
        "price_id": 0, 
        "code": "BC123", 
        "info_code": "", 
        "info_name": "", 
        "info_address": "", 
        "info_tel": "" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `cards[]` | collection | Collection of loyalty cards consisting of: · *ლოიალობის ბარათების კოლექციაა რომელიც შედგება:* |
| `cards[].id` | int | Card Id · *ბარათის Id* |
| `cards[].holder_id` | int | Id of the card holder (contragent) · *ბარათის მფლობელის (კონტრაგენტის) Id* |
| `cards[].type_id` | int | Card type (1 - accrual, 2 - discount, 5 - price type, 7 - cashback) · *ბარათის ტიპი (1 - დაგროვება, 2 - ფასდაკლება, 5 - ფასის ტიპი, 7 - cashback)* |
| `cards[].discount_id` | int | Discount Id (when type_id = 2) · *ფასდაკლების Id (იმ შემთხვევაში როცა type_id = 2)* |
| `cards[].price_id` | int | Price type Id (when type_id = 5) · *ფასის ტიპის Id (იმ შემთხვევაში როცა type_id = 5)* |
| `cards[].code` | string | Card code · *ბარათის კოდი* |
| `cards[].info_code` | string | Additional information about the card holder's code · *დამატებითი ინფორმაცია ბარათის მფლობელის კოდზე* |
| `cards[].info_name` | string | Additional information about the card holder's name · *დამატებითი ინფორმაცია ბარათის მფლობელის სახელზე* |
| `cards[].info_address` | string | Additional information about the card holder's address · *დამატებითი ინფორმაცია ბარათის მფლობელის მისამართზე* |
| `cards[].info_tel` | string | Additional information about the card holder's phone · *დამატებითი ინფორმაცია ბარათის მფლობელის ტელეფონზე;* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getBonusCardRestByCode

Bonus card balance · *ბონუს ბარათის ნაშთი*

Fetch the balance available on a bonus card by card code. · *ბონუს ბარათზე არსებული ნაშთის წამოღება ბარათის კოდის მიხედვით.*

**GET** `api/operation/getBonusCardRestByCode/{code}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `code` | string | The card code · *წარმოადგენს ბარათის კოდს* |

**Response**

```json
{ 
    "rest": 17.0, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `rest` | decimal | The card balance · *წარმოადგენს ბარათის ნაშთს* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getLoyaltyCustomers

Loyalty (Cloud) cards · *ლოიალობის(Cloud) ბარათები*

Fetch loyalty cards. · *ლოიალობის ბარათების წამოღება.*

**GET** `api/operation/getLoyaltyCustomers`

**Response**

```json
{ 
  "loyalty_customers": [ 
    { 
      "id": 1, 
      "code": "1", 
      "name": "ელენე1234", 
      "qr_code": "1", 
      "tel": "99551121061", 
      "birth_day": "2025-05-28T16:55:01.507", 
      "email": "sdcsdcsdcsc@gmail.com", 
      "sex": false, 
      "comment": "", 
      "allow_promotions": false, 
      "cerate_date": "2025-06-03T16:55:01.51" 
    }, 
    { 
      "id": 2, 
      "code": "2", 
      "name": "ლევანი", 
      "qr_code": "2", 
      "tel": "599705803", 
      "birth_day": "2025-06-05T00:00:00", 
      "email": "beqauri", 
      "sex": true, 
      "comment": "test", 
      "allow_promotions": false, 
      "cerate_date": "2025-06-05T12:59:56.837" 
    } 
  ], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `loyalty_customers[]` | collection | Collection of loyalty cards consisting of: · *ლოიალობის ბარათების კოლექციაა რომელიც შედგება:* |
| `loyalty_customers[].id` | int | Card Id · *ბარათის Id* |
| `loyalty_customers[].code` | string | Personal number · *პირადი ნომერი* |
| `loyalty_customers[].name` | string | First and last name · *სახელი, გვარი* |
| `loyalty_customers[].qr_code` | string | Unique number of the loyalty card · *ლოიალობის ბარათის უნიკალური ნომერი* |
| `loyalty_customers[].tel` | string | Phone number · *ტელ. ნომერი* |
| `loyalty_customers[].birth_day` | datetime | Date of birth · *დაბადების თარიღი* |
| `loyalty_customers[].email` | string | Email · *ელ. ფოსტა* |
| `loyalty_customers[].sex` | bool | Gender (true - male, false - female) · *სქესი (true - მამრობითი, false - მდედრობითი)* |
| `loyalty_customers[].comment` | string | Comment · *კომენტარი* |
| `loyalty_customers[].allow_promotions` | bool | Consent to marketing messages · *ნებართვა მარკეტინგულ შეტყობინებებზე* |
| `loyalty_customers[].cerate_date` | datetime | Creation date · *შექმნის თარიღი;* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getLoyaltyCustomer

Loyalty (Cloud) card · *ლოიალობის(Cloud) ბარათი*

Fetch a loyalty card. · *ლოიალობის ბარათის წამოღება.*

**GET** `api/operation/getLoyaltyCustomer/{id}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `id` | int | The card Id · *წარმოადგენს ბარათის Id -ს* |

**Response**

```json
{ 
  "loyalty_customer": { 
    "id": 44, 
    "code": "01001042222", 
    "name": "როლანდ რეიგანი", 
    "qr_code": "777888", 
    "tel": "+995598583444", 
    "birth_day": "1991-10-06T10:17:40", 
    "email": "", 
    "sex": true, 
    "comment": "კომენატიიიიიიი", 
    "allow_promotions": true, 
    "cerate_date": "2026-07-08T10:20:01.173", 
    "loyalty_programs": [ 
      { 
        "id": 391, 
        "program_id": 63, 
        "start_date": "2026-07-08T11:12:45.637", 
        "end_date": null, 
        "status": true 
      }], 
    "loyalty_groups": [ 
      { 
        "id": 595, 
        "group_id": 35 
      }] 
  }, 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `loyalty_customer` | object | The returned loyalty card, consisting of: · *დაბრუნებული ლოიალობის ბარათია რომელიც შედგება:* |
| `loyalty_customer.id` | int | Card Id · *ბარათის Id* |
| `loyalty_customer.code` | string | Personal number · *პირადი ნომერი* |
| `loyalty_customer.name` | string | First and last name · *სახელი, გვარი* |
| `loyalty_customer.qr_code` | string | Unique number of the loyalty card · *ლოიალობის ბარათის უნიკალური ნომერი* |
| `loyalty_customer.tel` | string | Phone number · *ტელ. ნომერი* |
| `loyalty_customer.birth_day` | datetime | Date of birth · *დაბადების თარიღი* |
| `loyalty_customer.email` | string | Email · *ელ. ფოსტა* |
| `loyalty_customer.sex` | bool | Gender (true - male, false - female) · *სქესი (true - მამრობითი, false - მდედრობითი)* |
| `loyalty_customer.comment` | string | Comment · *კომენტარი* |
| `loyalty_customer.allow_promotions` | bool | Consent to marketing messages · *ნებართვა მარკეტინგულ შეტყობინებებზე* |
| `loyalty_customer.cerate_date` | datetime | Creation date · *შექმნის თარიღი;* |
| `loyalty_customer.loyalty_programs[]` | collection | Collection of campaigns the card participates in: · *აქციების კოლექცია რომელშიც ბარათია ჩართული:* |
| `loyalty_customer.loyalty_programs[].id` | int | Id of the campaign record linked to the card · *ბარათზე მიბმული აქციის ჩანაწერის id* |
| `loyalty_customer.loyalty_programs[].program_id` | int | Loyalty program id · *ლოიალობის პროგრამის id* |
| `loyalty_customer.loyalty_programs[].start_date` | datetime | Start date · *დაწყების თარიღი* |
| `loyalty_customer.loyalty_programs[].end_date` | datetime | End date · *დასრულების თარიღი* |
| `loyalty_customer.loyalty_programs[].status` | bool | Status (true - active, false - inactive) · *სტატუსი (true - აქტიური, false - არააქტიური)* |
| `loyalty_customer.loyalty_groups[]` | collection | Collection of groups the card belongs to: · *ჯგუფების კოლექცია რომელშიც ბარათია ჩართული:* |
| `loyalty_customer.loyalty_groups[].id` | int | Id of the group record the card belongs to · *ჯგუფის ჩანაწერის id, რომელშიც ბარათია ჩართული* |
| `loyalty_customer.loyalty_groups[].group_id` | int | Group id · *ჯგუფის id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getLoyaltyCustomerPrograms

Loyalty (Cloud) programs · *ლოიალობის(Cloud) პროგრამები*

Fetch loyalty programs. · *ლოიალობის პროგრამების წამოღება.*

**GET** `api/operation/getLoyaltyCustomerPrograms`

**Response**

```json
{ 
  "programs": [ 
    { 
      "id": 59, 
      "name": "აქცია", 
      "start_date": "2026-05-05T00:00:00", 
      "end_date": "2026-08-01T23:59:59", 
      "comment": "", 
      "status": true, 
      "program_type": 1, 
      "usage_type": 1 
    }, 
    { 
      "id": 61, 
      "name": "ხვ", 
      "start_date": "2026-06-17T00:00:00", 
      "end_date": "2026-08-01T23:59:59", 
      "comment": "", 
      "status": true, 
      "program_type": 2, 
      "usage_type": 0 
    } 
  ], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `programs[]` | collection | Collection of loyalty programs consisting of: · *ლოიალობის პროგრამების კოლექციაა რომელიც შედგება:* |
| `programs[].id` | int | Program Id · *პროგრამის Id* |
| `programs[].name` | string | Name · *დასახელება* |
| `programs[].start_date` | datetime | Start date · *დაწყების თარიღი* |
| `programs[].end_date` | datetime | End date · *დასრულების თარიღი* |
| `programs[].comment` | string | Description · *აღწერა* |
| `programs[].status` | bool | Status (true - active, false - inactive) · *სტატუსი (true - აქტიური, false - არააქტიური)* |
| `programs[].program_type` | byte | Program type (1 - discount, 2 - accrual, 3 - campaign, 4 - price type) · *პროგრამის ტიპი (1 - ფასდაკლება, 2 - დაგროვება, 3 - აქცია, 4 - ფასის ტიპი)* |
| `programs[].usage_type` | byte | Usage type (0 - on the selected card, 1 - on all cards, 2 - without a card) · *გამოყენების ტიპი (0 - არჩეულ ბარათზე, 1 - ყველა ბარათზე, 2 - ბარათის გარეშე)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getLoyaltyCustomerGroups

Loyalty (Cloud) groups · *ლოიალობის(Cloud) ჯგუფები*

Fetch loyalty groups. · *ლოიალობის ჯგუფების წამოღება.*

**GET** `api/operation/getLoyaltyCustomerGroups`

**Response**

```json
{ 
  "loyalty_groups": [ 
    { 
      "id": 35, 
      "name": "პირველი ჯგუფი", 
      "comment": "" 
    }, 
    { 
      "id": 36, 
      "name": "მეორე ჯგუფი", 
      "comment": "" 
    } 
  ], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `programs[]` | collection | Collection of loyalty groups consisting of: · *ლოიალობის ჯგუფების კოლექციაა რომელიც შედგება:* |
| `programs[].id` | int | Group Id · *ჯგუფის Id* |
| `programs[].name` | string | Name · *დასახელება* |
| `programs[].comment` | string | Description · *აღწერა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `loyalty_groups` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `programs` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getLoyaltyCustomerBalances

Loyalty (Cloud) card balances · *ლოიალობის(Cloud) ბარათების ნაშთი*

Fetch loyalty card balances. · *ლოიალობის ბარათების ბალანსის წამოღება.*

**GET** `api/operation/getLoyaltyCustomerBalances`

**Response**

```json
{ 
  "loyalty_balances": [ 
    { 
      "id": 1, 
      "code": "1", 
      "name": "ელენე1234", 
      "tel": "99551121061", 
      "qr_code": "1", 
      "balance": 79.88 
    }, 
    { 
      "id": 39, 
      "code": "852", 
      "name": "eli", 
      "tel": "", 
      "qr_code": "852", 
      "balance": 0.03 
    } 
  ], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `loyalty_balances[]` | collection | Collection of loyalty card balances consisting of: · *ლოიალობის ბარათების ბალანსის კოლექციაა რომელიც შედგება:* |
| `loyalty_balances[].id` | int | Card Id · *ბარათის Id* |
| `loyalty_balances[].code` | string | Personal number · *პირადი ნომერი* |
| `loyalty_balances[].name` | string | First and last name · *სახელი, გვარი* |
| `loyalty_balances[].tel` | string | Phone number · *ტელ. ნომერი* |
| `loyalty_balances[].qr_code` | string | Unique number of the loyalty card · *ლოიალობის ბარათის უნიკალური ნომერი* |
| `loyalty_balances[].balance` | decimal | Balance · *ბალანსი;* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getLoyaltyCustomerBalance

Loyalty (Cloud) card balance · *ლოიალობის(Cloud) ბარათის ნაშთი*

Fetch a loyalty card's balance by card code. · *ლოიალობის ბარათის ბალანსის წამოღება ბარათის კოდის მიხედვით.*

**GET** `api/operation/getLoyaltyCustomerBalance/{qr_code}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `qr_code` | string | The unique code of the card · *წარმოადგენს ბარათის უნიკალურ კოდს* |

**Response**

```json
{ 
  "loyalty_balance": { 
    "id": 1, 
    "code": "1", 
    "name": "ელენე1234", 
    "tel": "99551121061", 
    "qr_code": "1", 
    "balance": 79.88 
  }, 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `loyalty_balance` | object | Loyalty card balance object consisting of: · *ლოიალობის ბარათის ბალანსის ობიექტია რომელიც შედგება:* |
| `loyalty_balance.id` | int | Card Id · *ბარათის Id* |
| `loyalty_balance.code` | string | Personal number · *პირადი ნომერი* |
| `loyalty_balance.name` | string | First and last name · *სახელი, გვარი* |
| `loyalty_balance.tel` | string | Phone number · *ტელ. ნომერი* |
| `loyalty_balance.qr_code` | string | Unique number of the loyalty card · *ლოიალობის ბარათის უნიკალური ნომერი* |
| `loyalty_balance.balance` | decimal | Balance · *ბალანსი;* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getLoyaltyBonusHistory

Loyalty (Cloud) card accrual/spending history · *ლოიალობის(Cloud) ბარათის დაგროვება/გახარჯვის ისტორია*

Fetch a loyalty card's history by card code. · *ლოიალობის ბარათის ისტორიის წამოღება ბარათის კოდის მიხედვით.*

**GET** `api/operation/getLoyaltyBonusHistory/{qr_code}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `qr_code` | string | The unique code of the card · *წარმოადგენს ბარათის უნიკალურ კოდს* |

**Response**

```json
{ 
  "bonus_history": [ 
    { 
      "tdate": "2026-07-10T12:51:25.93", 
      "amount": 18, 
      "bonus": 0.18, 
      "coeff": 1, 
      "comment": null, 
      "id": 1299, 
      "products": [{ 
          "id": 5, 
          "quantity": 3, 
          "price": 6 
        }] 
    }, 
    { 
      "tdate": "2026-07-10T13:01:26.49", 
      "amount": 0, 
      "bonus": 1, 
      "coeff": -1, 
      "comment": "ჩამოწერა", 
      "id": null, 
      "products": [] 
    } 
  ], 
  "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `bonus_history[]` | collection | Collection of the loyalty card's history consisting of: · *ლოიალობის ბარათის ისტორიის კოლექციაა რომელიც შედგება:* |
| `bonus_history[].id` | int? | Id of the corresponding operation posted in the system on which the accrual/spending was based · *სისტემაში გატარებული შესაბამისი ოპერაციის Id, რომლის საფუძველზეც მოხდა დაგროვება/გახარჯვა* |
| `bonus_history[].tdate` | datetime | Posting date · *გატარების თარიღი* |
| `bonus_history[].amount` | decimal | Value of the operation on which the accrual/spending was based · *ოპერაციის ღირებულება, რომლის საფუძველზეც მოხდა დაგროვებ/გახარჯვა* |
| `bonus_history[].bonus` | decimal | Accrued/spent bonus points · *დაგროვილი/გახარჯული ბონუს ქულა* |
| `bonus_history[].coeff` | int | Accrual/spending indicator (1 - accrual, -1 - spending) · *დაგროვება/გახარჯვის მაჩვენებელი (1 დაგროვება, -1 - გახარჯვა)* |
| `bonus_history[].comment` | string | Additional comment · *დამატებითი კომენტარი* |
| `products[]` | collection | Collection of products participating in the accrual/spending operation: · *პროდუქტების კოლექცია რომელიც დაგროვება/გახარვის ოპერაციაში მონაწილებს :* |
| `products[].id` | int | Product id · *საქონლის id* |
| `products[].quantity` | double | Quantity · *რაოდენობა* |
| `products[].price` | double | Price · *ფასი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### saveLoyaltyCustomer

Save a loyalty (Cloud) card · *ლოიალობის(Cloud) ბარათის შენახვა*

Save a loyalty card (insert, update) · *ლოიალობის ბარათის შენახვა (insert, update)*

**POST** `api/operation/saveLoyaltyCustomer`

**Request body**

```json
{ 
  "id": 0, 
  "name": "ბარათის მფლობელი", 
  "code": "01001012345", 
  "tel": "+995598123456", 
  "email": "customer_email@loyalty.ge", 
  "sex": true, 
  "birth_day": "1991-10-06T10:17:40", 
  "qr_code": "777888", 
  "comment": "ბარათის კომენტარი", 
  "allow_promotions": true, 
  "loyalty_programs": [ 
    { 
      "id": 0, 
      "program_id": 63, 
      "status": true 
    }], 
  "loyalty_groups": [ 
    { 
      "id": 0, 
      "group_id": 16, 
    }] 
}
```

> [!NOTE]
> The request body example above is not valid JSON as printed in the source documentation (it contains a typo such as a stray or missing comma). The field list below is authoritative.

| Field | Type | Description |
|---|---|---|
| `id` | int | Loyalty card Id. (pass 0 to create a new one) · *ლოიალობის ბარათის Id. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `code` | string | Personal number · *პირადი ნომერი* |
| `name` | string | Name · *დასახელება* |
| `comment` | string | Comment · *კომენტარი* |
| `tel` | string | Phone number · *ტელ. ნომერი* |
| `email` | string | Email · *ელ ფოსტა* |
| `sex` | bool | Gender (true - male, false - female) · *სქესი (true - მამრობითი, false - მდედრობითი)* |
| `birth_day` | datetime | Date of birth · *დაბადების თარიღი* |
| `qr_code` | string | Unique number of the card · *ბარათის უნიკალური ნომერი* |
| `allow_promotions` | bool | Consent to marketing messages · *ნებართვა მარკეტინგულ შეტყობინებებზე* |
| `loyalty_programs[]` | collection | Collection of campaigns the card participates in: · *აქციების კოლექცია რომელშიც ბარათია ჩართული:* |
| `loyalty_programs[].id` | int | Id of the campaign record linked to the card (pass 0 when adding a new campaign to the card) · *ბარათზე მიბმული აქციის ჩანაწერის id (თუ ახალი აქცია ემატება ბარათს - გადაეცემა 0 )* |
| `loyalty_programs[].program_id` | int | Loyalty program id · *ლოიალობის პროგრამის id* |
| `loyalty_programs[].status` | bool | Status of the campaign linked to the card. (If the loyalty_programs collection is not null, the corresponding values of the campaigns passed will be applied to this card: insert/update/delete) · *ბარათზე მიბმული აქციის სტატუსი. (თუ loyalty_programs კოლექცია არ არის null, მოხდება მოცემული ბარათისთვის გადმოცემული აქციების შესაბამისი მნიშვნელობების მინიჭება insert/update/delete)* |
| `loyalty_groups[]` | collection | Collection of groups the card belongs to: · *ჯგუფების კოლექცია რომელშიც ბარათია ჩართული:* |
| `loyalty_groups[].id` | int | Id of the group record the card belongs to (pass 0 when adding the card to a new group) · *ჯგუფის ჩანაწერის id, რომელშიც ბარათია ჩართული (თუ ახალ ჯგუფში ემატება ბარათი - გადაეცემა 0 )* |
| `loyalty_groups[].group_id` | int | Group id. (If the loyalty_groups collection is not null, the corresponding values of the groups passed will be applied to this card: insert/update/delete) · *ჯგუფის id, (თუ loyalty_groups კოლექცია არ არის null, მოხდება მოცემული ბარათისთვის გადმოცემული ჯგუფების შესაბამისი მნიშვნელობების მინიჭება insert/update/delete)* |

**Response**

```json
{ 
    "id": 1, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the inserted (or updated) loyalty card · *დამატებული (ან დარედაქტირებული) ლოიალობის ბარათის Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### saveLoyaltyGroup

Save a loyalty (Cloud) group · *ლოიალობის(Cloud) ჯგუფის შენახვა*

Save a loyalty group (insert, update) · *ლოიალობის ჯგუფის შენახვა (insert, update)*

**POST** `api/operation/saveLoyaltyGroup`

**Request body**

```json
{ 
  "id": 0, 
  "name": "ჯგუფი #1", 
  "comment": "" 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Loyalty group Id. (pass 0 to create a new one) · *ლოიალობის ჯგუფისId. (თუ იქმნება ახალი, გადაეცემა 0)* |
| `name` | string | Name · *დასახელება* |
| `comment` | string | Comment · *კომენტარი* |

**Response**

```json
{ 
    "id": 1, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the inserted (or updated) loyalty group · *დამატებული (ან დარედაქტირებული) ლოიალობის ჯგუფის Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### saveLoyaltyBonusPoint

Grant / deduct loyalty (Cloud) points · *ლოიალობის(Cloud) ქულის ჩუქება / ჩამოჭრა*

Grant / deduct loyalty points (insert) · *ლოიალობის ქულის ჩუქება / ჩამოჭრა (insert)*

**POST** `api/operation/saveLoyaltyBonusPoint`

**Request body**

```json
{ 
  "id": 45, 
  "date": "2026-07-10T15:45:31", 
  "amount": 9, 
  "coeff": -1, 
  "comment": "ჩამოჭრა" 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Loyalty card Id · *ლოიალობის ბარათის Id* |
| `date` | datetime | Date the operation is carried out · *ოპერაციის განხორციელების თარიღი* |
| `amount` | decimal | Points (granted or deducted) · *ქულა (ნაჩუქარი ან ჩამოჭრილი)* |
| `coeff` | int | Operation indicator (1 - accrual, -1 - deduction) · *ოპერაციის განმსაზღვრელი (1 - დაგროვებ, -1 - ჩამოჭრა)* |
| `comment` | string | Comment · *კომენტარი* |

**Response**

```json
{ 
    "id": 1, 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Id of the created operation · *შექმნილი ოპერაციის Id* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---
