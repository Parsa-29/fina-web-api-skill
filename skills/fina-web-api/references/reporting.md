# Journals and reports

16 methods. Generated from *FINA WEB API 10.0* — do not edit by hand; see `scripts/render_references.py`.

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getRealizesJournal`](#getrealizesjournal) | GET | `api/reporting/getRealizesJournal/{date_from}/{date_to}` | Sales journal |
| [`getMovesJournal`](#getmovesjournal) | GET | `api/reporting/getMovesJournal/{date_from}/{date_to}` | Transfers journal |
| [`getDocProvidedServicesJournal`](#getdocprovidedservicesjournal) | GET | `api/reporting/getDocProvidedServicesJournal/{date_from}/{date_to}` | Journal of provided services |
| [`getDocReceivedServicesJournal`](#getdocreceivedservicesjournal) | GET | `api/reporting/getDocReceivedServicesJournal/{date_from}/{date_to}` | Journal of received services |
| [`getCustomersOrderJournal`](#getcustomersorderjournal) | GET | `api/reporting/getCustomersOrderJournal/{date_from}/{date_to}` | Journal of customer orders |
| [`getCustomersReturnJournal`](#getcustomersreturnjournal) | GET | `api/reporting/getCustomersReturnJournal/{date_from}/{date_to}` | Journal of returns from customers |
| [`getCustomersMoneyJournal`](#getcustomersmoneyjournal) | GET | `api/reporting/getCustomersMoneyJournal/{date_from}/{date_to}` | Journal of money received from and returned to customers, and of advances |
| [`getVendorsMoneyJournal`](#getvendorsmoneyjournal) | GET | `api/reporting/getVendorsMoneyJournal/{date_from}/{date_to}` | Journal of money issued to and returned from vendors, and of advances |
| [`getProductionsJournal`](#getproductionsjournal) | GET | `api/reporting/getProductionsJournal/{date_from}/{date_to}` | Journal of productions |
| [`getDiscountCardsJournal`](#getdiscountcardsjournal) | GET | `api/reporting/getDiscountCardsJournal/{date_from}/{date_to}` | Journal of discount cards |
| [`getAutoServicesOutJournal`](#getautoservicesoutjournal) | GET | `api/reporting/getAutoServicesOutJournal/{date_from}/{date_to}` | Journal of completed requests |
| [`getCustomersCycleReport`](#getcustomerscyclereport) | GET | `api/reporting/getCustomersCycleReport/{date_from}/{date_to}` | Customer turnover |
| [`getVendorsCycleReport`](#getvendorscyclereport) | GET | `api/reporting/getVendorsCycleReport/{date_from}/{date_to}` | Vendor turnover |
| [`getProductsLastInReport`](#getproductslastinreport) | GET | `api/reporting/getProductsLastInReport/{date_from}/{date_to}` | Information about the last receipt of goods |
| [`getProductsInReturnReport`](#getproductsinreturnreport) | GET | `api/reporting/getProductsInReturnReport/{date_from}/{date_to}` | Goods receipts and returns to vendors in detail |
| [`getCafeOrderDetailedReport`](#getcafeorderdetailedreport) | GET | `api/reporting/getCafeOrderDetailedReport/{date_from}/{date_to}` | Orders (cafe) in detail |

---

### getRealizesJournal

Sales journal · *გაყიდვების ჟურნალი*

Sales journal (sale of goods / fixed assets, retail sale) · *გაყიდვების ჟურნალი (საქონლის / ძირ. საშუალების რეალიზაცია, საცალო გაყიდვა)*

**GET** `api/reporting/getRealizesJournal/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "journals": [{ 
        "id": 5280, 
        "version": "AAAAAAAB3TM=", 
        "date": "2018-12-27 18:10:48", 
        "doc_num": "36", 
        "waybill_num": null, 
        "doc_type": 21, 
        "purpose": "საქონლის რეალიზაცია ნაღდზე", 
        "amount": 4.28, 
        "staff_id": 3, 
        "currency": "GEL", 
        "customer_id": 8, 
        "store_id": 1, 
        "pay_type": 0 
    }, { 
        "id": 5282, 
        "version": "AAAAAAAB3Tg=", 
        "date": "2018-12-27 18:36:25", 
        "doc_num": "49", 
        "waybill_num": "0431440360", 
        "doc_type": 23, 
        "purpose": "საცალო გაყიდვა № 49", 
        "amount": 4.50, 
        "staff_id": 0, 
        "currency": "GEL", 
        "customer_id": 0, 
        "store_id": 1, 
        "pay_type": 0 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `journal[]` | collection | Collection of the sales journal consisting of: · *გაყიდვების ჟურნალის კოლექციაა რომელიც შედგება:* |
| `journal[].id` | int | Operation id · *ოპერაციის id* |
| `journal[].version` | string | Record version in the database (base64 of byte[]) · *ჩანაწერის ვერსია ბაზაში (base64 of byte[])* |
| `journal[].date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `journal[].doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `journal[].waybill_num` | string | Waybill number (RS - Revenue Service) · *ზედნადების ნომერი (RS)* |
| `journal[].doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `journal[].purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `journal[].amount` | decimal | Operation amount · *ოპერაციის თანხა* |
| `journal[].staff_id` | int | Staff member id · *თანამშრომლის id* |
| `journal[].currency` | string | Currency · *ვალუტა* |
| `journal[].customer_id` | int | Customer id · *მყიდველის id* |
| `journal[].store_id` | int | Id of the store the sale was made from · *საწყობის id რომლიდანაც მოხდა რეალიზაცია* |
| `journal[].pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `journals` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `journal` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getMovesJournal

Transfers journal · *გადატანების ჟურნალი*

Journal of internal transfers (transfer of goods / fixed assets) · *შიდა გადატანების ჟურნალი (საქონლის / ძირ. საშუალების გადატანა)*

**GET** `api/reporting/getMovesJournal/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "journals": [{ 
        "id": 14830, 
        "version": "AAAAAAAG/RM=", 
        "date": "2020-03-18 10:24:13", 
        "doc_num": "11", 
        "waybill_num": "0514054983", 
        "doc_type": 20, 
        "purpose": "საქონლის გადატანა № 11", 
        "amount": 18.70, 
        "staff_id": 2, 
        "store_from_id": 1, 
        "store_to_id": 2 
    }, { 
        "id": 14831, 
        "version": "AAAAAAAG/RQ=", 
        "date": "2020-03-18 10:25:25", 
        "doc_num": "12", 
        "waybill_num": null, 
        "doc_type": 12, 
        "purpose": "ძირითადი საშუალების გადაადგილება № 12", 
        "amount": 5.70, 
        "staff_id": 2, 
        "store_from_id": 1, 
        "store_to_id": 6 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `journal[]` | collection | Collection of the transfers journal consisting of: · *გადატანების ჟურნალის კოლექციაა რომელიც შედგება:* |
| `journal[].id` | int | Operation id · *ოპერაციის id* |
| `journal[].version` | string | Record version in the database (base64 of byte[]) · *ჩანაწერის ვერსია ბაზაში (base64 of byte[])* |
| `journal[].date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `journal[].doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `journal[].waybill_num` | string | Waybill number (RS - Revenue Service) · *ზედნადების ნომერი (RS)* |
| `journal[].doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `journal[].purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `journal[].amount` | decimal | Operation amount · *ოპერაციის თანხა* |
| `journal[].staff_id` | int | Staff member id · *თანამშრომლის id* |
| `journal[].store_from_id` | int | Store id (sender) · *საწყობის id (გამგზავნი)* |
| `journal[].store_to_id` | int | Store id (recipient) · *საწყობის id (მიმღები)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `journals` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `journal` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getDocProvidedServicesJournal

Journal of provided services · *გაწეული მომსახურებების ჟურნალი*

Journal of provided services · *გაწეული მომსახურებების ჟურნალი*

**GET** `api/reporting/getDocProvidedServicesJournal/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "journals": [{ 
        "id": 6400, 
        "version": "AAAAAAACWbw=", 
        "date": "2019-02-15 13:00:00", 
        "doc_num": "7", 
        "doc_type": 29, 
        "purpose": "მომსახურების გაწევა", 
        "amount": 2.00, 
        "staff_id": 2, 
        "currency": "GEL", 
        "customer_id": 8, 
        "f_status": false, 
        "pay_type": 0 
    }, { 
        "id": 6478, 
        "version": "AAAAAAAC5rk=", 
        "date": "2019-03-15 12:32:18", 
        "doc_num": "8", 
        "doc_type": 29, 
        "purpose": "მომსახურების გაწევა № 8", 
        "amount": 118.00, 
        "staff_id": 0, 
        "currency": "GEL", 
        "customer_id": 1, 
        "f_status": false, 
        "pay_type": 1 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `journal[]` | collection | Collection of the provided services journal consisting of: · *გაწეული მომსახურებების ჟურნალის კოლექციაა რომელიც შედგება:* |
| `journal[].id` | int | Operation id · *ოპერაციის id* |
| `journal[].version` | string | Record version in the database (base64 of byte[]) · *ჩანაწერის ვერსია ბაზაში (base64 of byte[])* |
| `journal[].date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `journal[].doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `journal[].doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `journal[].purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `journal[].amount` | decimal | Operation amount · *ოპერაციის თანხა* |
| `journal[].staff_id` | int | Staff member id · *თანამშრომლის id* |
| `journal[].currency` | string | Currency · *ვალუტა* |
| `journal[].customer_id` | int | Customer id · *მყიდველის id* |
| `journal[].f_status` | bool | Whether an invoice/declaration has been issued · *გამოწერილია თუ არა ა/ფ დეკლარაცია* |
| `journal[].pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `journals` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `journal` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getDocReceivedServicesJournal

Journal of received services · *მიღებული მომსახურებების ჟურნალი*

Journal of received services · *მიღებული მომსახურებების ჟურნალი*

**GET** `api/reporting/getDocReceivedServicesJournal/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "journals": [{ 
        "id": 6562, 
        "version": "AAAAAAAEPh0=", 
        "date": "2019-05-16 11:36:11", 
        "doc_num": "4", 
        "doc_type": 28, 
        "purpose": "მომსახურების მიღება № 4", 
        "amount": 1000.00, 
        "staff_id": 0, 
        "currency": "GEL", 
        "vendor_id": 3, 
        "pay_type": 1 
    }, { 
        "id": 10756, 
        "version": "AAAAAAAGAy0=", 
        "date": "2019-12-09 16:22:04", 
        "doc_num": "5", 
        "doc_type": 28, 
        "purpose": "მომსახურების მიღება № 5", 
        "amount": 1000.00, 
        "staff_id": 0, 
        "currency": "GEL", 
        "vendor_id": 24, 
        "pay_type": 2 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `journal[]` | collection | Collection of the provided services journal consisting of: · *გაწეული მომსახურებების ჟურნალის კოლექციაა რომელიც შედგება:* |
| `journal[].id` | int | Operation id · *ოპერაციის id* |
| `journal[].version` | string | Record version in the database (base64 of byte[]) · *ჩანაწერის ვერსია ბაზაში (base64 of byte[])* |
| `journal[].date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `journal[].doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `journal[].doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `journal[].purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `journal[].amount` | decimal | Operation amount · *ოპერაციის თანხა* |
| `journal[].staff_id` | int | Staff member id · *თანამშრომლის id* |
| `journal[].currency` | string | Currency · *ვალუტა* |
| `journal[].vendor_id` | int | Vendor id · *მომწოდებლის id* |
| `journal[].pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `journals` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `journal` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getCustomersOrderJournal

Journal of customer orders · *მყიდველების შეკვეთების ჟურნალი*

Journal of orders received from customers · *მყიდველებისგან მიღებული შეკვეთების ჟურნალი*

**GET** `api/reporting/getCustomersOrderJournal/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "journals": [{ 
        "id": 3121, 
        "version": "AAAAAAABf5A=", 
        "date": "2018-10-19 16:03:21", 
        "doc_num": "5", 
        "doc_type": 8, 
        "purpose": "შეკვეთა მყიდველისგან № 5", 
        "amount": 49.00, 
        "staff_id": 4, 
        "currency": "GEL", 
        "customer_id": 8, 
        "store_id": 1, 
        "order_status": 1, 
        "pay_type": 0 
    }, { 
        "id": 4131, 
        "version": "AAAAAAACOlY=", 
        "date": "2018-11-07 11:30:28", 
        "doc_num": "6", 
        "doc_type": 8, 
        "purpose": "შეკვეთა მყიდველისგან № 6", 
        "amount": 33.75, 
        "staff_id": 0, 
        "currency": "GEL", 
        "customer_id": 8, 
        "store_id": 1, 
        "order_status": 3, 
        "pay_type": 5 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `journal[]` | collection | Collection of the customer orders journal consisting of: · *მყიდველების შკვეთების ჟურნალის კოლექციაა რომელიც შედგება:* |
| `journal[].id` | int | Operation id · *ოპერაციის id* |
| `journal[].version` | string | Record version in the database (base64 of byte[]) · *ჩანაწერის ვერსია ბაზაში (base64 of byte[])* |
| `journal[].date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `journal[].doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `journal[].doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `journal[].purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `journal[].amount` | decimal | Operation amount · *ოპერაციის თანხა* |
| `journal[].staff_id` | int | Staff member id · *თანამშრომლის id* |
| `journal[].currency` | string | Currency · *ვალუტა* |
| `journal[].customer_id` | int | Customer id · *მყიდველის id* |
| `journal[].store_id` | int | Id of the store the goods were ordered in · *საწყობის id რომლშიც მოხდა საქონლის შეკვეთა* |
| `journal[].order_status` | byte | Order status (1 - active, 2 - received, 3 - cancelled) · *შეკვეთის სტატუსი (1 - აქტიური, 2 - მიღებული, 3 - გაუქმებული)* |
| `journal[].pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `journals` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `journal` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getCustomersReturnJournal

Journal of returns from customers · *მყიდველებისგან დაბრუნებების ჟურნალი*

Journal of goods and fixed assets returned from customers · *მყიდველებისგან დაბრუნებული საქონლის, ძირ. საშუალებების ჟურნალი*

**GET** `api/reporting/getCustomersReturnJournal/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "journals": [{ 
        "id": 6352, 
        "version": "AAAAAAACSlg=", 
        "date": "2019-02-11 12:56:45", 
        "doc_num": "1", 
        "waybill_num": null, 
        "doc_type": 9, 
        "purpose": "დაბრუნება მყიდველისგან № 0", 
        "amount": 7.25, 
        "staff_id": 0, 
        "currency": "GEL", 
        "customer_id": 8, 
        "store_id": 1, 
        "pay_type": 1 
    }, { 
        "id": 6401, 
        "version": "AAAAAAACaUU=", 
        "date": "2019-02-15 13:00:00", 
        "doc_num": "5", 
        "waybill_num": null, 
        "doc_type": 9, 
        "purpose": "dabruneba", 
        "amount": 65.7, 
        "staff_id": 0, 
        "currency": "GEL", 
        "customer_id": 8, 
        "store_id": 1, 
        "pay_type": 2 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Operation id · *ოპერაციის id* |
| `version` | string | Record version in the database (base64 of byte[]) · *ჩანაწერის ვერსია ბაზაში (base64 of byte[])* |
| `date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `waybill_num` | string | Waybill number (RS - Revenue Service) · *ზედნადების ნომერი (RS)* |
| `doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `amount` | decimal | Operation amount · *ოპერაციის თანხა* |
| `staff_id` | int | Staff member id · *თანამშრომლის id* |
| `currency` | string | Currency · *ვალუტა* |
| `customer_id` | int | Customer id · *მყიდველის id* |
| `store_id` | int | Store (warehouse) id · *საწყობის id* |
| `pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `journals` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---

### getCustomersMoneyJournal

Journal of money received from and returned to customers, and of advances · *მყიდველებისგან მიღებული, დაბრუნებული თანხების და ავანსების ჟურნალი*

Journal of money received from and returned to customers, and of advances · *მყიდველებისგან მიღებული, დაბრუნებული თანხების და ავანსების ჟურნალი*

**GET** `api/reporting/getCustomersMoneyJournal/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "journals": [{ 
        "id": 3122, 
        "version": "AAAAAAACOnw=", 
        "date": "2018-10-19 16:05:04", 
        "doc_num": "5", 
        "doc_type": 49, 
        "purpose": "ავანსის მიღება მყიდველისგან - რონალდ რეიგანი", 
        "amount": 12.00, 
        "staff_id": 4, 
        "currency": "USD", 
        "customer_id": 8, 
        "pay_type": 4, 
        "pay_type_id": 11 
    }, { 
        "id": 3123, 
        "version": "AAAAAAABf5I=", 
        "date": "2018-10-19 16:08:48", 
        "doc_num": "5", 
        "doc_type": 38, 
        "purpose": "თანხის მიღება მყიდველისგან - რონალდ რეიგანი", 
        "amount": 10.00, 
        "staff_id": 0, 
        "currency": "GEL", 
        "customer_id": 8, 
        "pay_type": 1, 
        "pay_type_id": 1 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Operation id · *ოპერაციის id* |
| `version` | string | Record version in the database (base64 of byte[]) · *ჩანაწერის ვერსია ბაზაში (base64 of byte[])* |
| `date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `amount` | decimal | Operation amount · *ოპერაციის თანხა* |
| `staff_id` | int | Staff member id · *თანამშრომლის id* |
| `currency` | string | Currency · *ვალუტა* |
| `customer_id` | int | Customer id · *მყიდველის id* |
| `pay_type` | byte | Payment method (1 - cash, 2 - POS terminal, 3 - bank transfer, 4 - installment bank) · *გადახდის სახეობა (1 - ნაღდი, 2 - ტერმინალი, 3 - საბანკო გადარიცხვა, 4 - განვადების ბანკი) * |
| `pay_type_id` | int | Id of the cash register, POS terminal, bank account or installment bank in the FINA database (depending on pay_type) · *სალაროს, ტერმინალის, საბანკო ანგარიშის ან განვადების ბანკის Id არსებული FINA -ს ბაზაში (იმისდა მიხედვით თუ რა არის pay_type)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `journals` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---

### getVendorsMoneyJournal

Journal of money issued to and returned from vendors, and of advances · *მომწოდებლებზე გაცემული, დაბრუნებული თანხების და ავანსების ჟურნალი*

Journal of money issued to and returned from vendors, and of advances · *მომწოდებლებზე გაცემული, დაბრუნებული თანხების და ავანსების ჟურნალი*

**GET** `api/reporting/getVendorsMoneyJournal/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "journals": [{ 
        "id": 4122, 
        "version": "AAAAAAACOnw=", 
        "date": "2018-10-19 16:05:04", 
        "doc_num": "5", 
        "doc_type": 50, 
        "purpose": "ავანსის გაცემა მომწოდებელზე - (მომწოდებელი)", 
        "amount": 12.00, 
        "staff_id": 4, 
        "currency": "USD", 
        "vendor_id": 18, 
        "pay_type": 4, 
        "pay_type_id": 11 
    }, { 
        "id": 3165, 
        "version": "AAAAAAABf5I=", 
        "date": "2018-10-19 16:08:48", 
        "doc_num": "5", 
        "doc_type": 39, 
        "purpose": "თანხის გაცემა მომწოდებელზე - xyz", 
        "amount": 10.00, 
        "staff_id": 0, 
        "currency": "GEL", 
        "vendor_id": 68, 
        "pay_type": 1, 
        "pay_type_id": 1 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `id` | int | Operation id · *ოპერაციის id* |
| `version` | string | Record version in the database (base64 of byte[]) · *ჩანაწერის ვერსია ბაზაში (base64 of byte[])* |
| `date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `amount` | decimal | Operation amount · *ოპერაციის თანხა* |
| `staff_id` | int | Staff member id · *თანამშრომლის id* |
| `currency` | string | Currency · *ვალუტა* |
| `customer_id` | int | Vendor id · *მომწოდებლის id* |
| `pay_type` | byte | Payment method (1 - cash, 2 - POS terminal, 3 - bank transfer, 4 - installment bank) · *გადახდის სახეობა (1 - ნაღდი, 2 - ტერმინალი, 3 - საბანკო გადარიცხვა, 4 - განვადების ბანკი) * |
| `pay_type_id` | int | Id of the cash register, POS terminal, bank account or installment bank in the FINA database (depending on pay_type) · *სალაროს, ტერმინალის, საბანკო ანგარიშის ან განვადების ბანკის Id არსებული FINA -ს ბაზაში (იმისდა მიხედვით თუ რა არის pay_type)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `journals`, `vendor_id` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `customer_id` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getProductionsJournal

Journal of productions · *წარმოებების ჟურნალი*

Journal of productions · *წარმოებების ჟურნალი*

**GET** `api/reporting/getProductionsJournal/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "journals": [{ 
        "id": 17059, 
        "version": "AAAAAAAQY1Q=", 
        "date": "2021-01-14 16:12:00", 
        "doc_num": "2", 
        "doc_type": 18, 
        "purpose": "წარმოება № 2", 
        "amount": 0.00, 
        "store_id": 1, 
        "production_type": 1 
    }, { 
        "id": 17060, 
        "version": "AAAAAAAQgpI=", 
        "date": "2021-01-14 18:44:57", 
        "doc_num": "3", 
        "doc_type": 18, 
        "purpose": "წარმოება № 3", 
        "amount": 5.92, 
        "store_id": 1, 
        "production_type": 0 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `journal[]` | collection | Collection of the productions journal consisting of: · *წარმოებების ჟურნალის კოლექციაა რომელიც შედგება:* |
| `journal[].id` | int | Operation id · *ოპერაციის id* |
| `journal[].version` | string | Record version in the database (base64 of byte[]) · *ჩანაწერის ვერსია ბაზაში (base64 of byte[])* |
| `journal[].date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `journal[].doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `journal[].doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `journal[].purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `journal[].amount` | decimal | Operation amount · *ოპერაციის თანხა* |
| `journal[].store_id` | int | Store (warehouse) id · *საწყობის id* |
| `journal[].production_type` | byte | Production kind (0 - production; 1 - disassembly; 2 - adding a part, repair; 3 - separating a part) · *წარმოების სახეობა (0 - წარმოება; 1 - დაშლა; 2 - ნაწილის დამატება, რემონტი; 3 - ნაწილის გამოყოფა)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `journals` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `journal` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getDiscountCardsJournal

Journal of discount cards · *ფასდაკლების ბარათების ჟურნალი*

Journal of issued discount cards · *გაცემული ფასდაკლების ბარათების ჟურნალი*

**GET** `api/reporting/getDiscountCardsJournal/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "journals": [{ 
        "id": 8728, 
        "version": "AAAAAAAFKHk=", 
        "date": "2019-11-08 18:00:00", 
        "doc_num": "14", 
        "doc_type": 118, 
        "purpose": "ფასდაკლების ბარათის გაცემა", 
        "amount": 823.44, 
        "staff_id": 0, 
        "customer": 31, 
        "store_id": 1, 
        "card_code": "231", 
        "discount_id": 1, 
        "status": true 
    }, { 
        "id": 8733, 
        "version": "AAAAAAAFKHg=", 
        "date": "2019-11-08 18:00:00", 
        "doc_num": "15", 
        "doc_type": 118, 
        "purpose": "ფასდაკლების ბარათის გაცემა", 
        "amount": 823.44, 
        "staff_id": 0, 
        "customer": 31, 
        "store_id": 1, 
        "card_code": "2311", 
        "discount_id": 2, 
        "status": true 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `journal[]` | collection | Collection of the discount cards journal consisting of: · *ფასდაკლების ბარათების ჟურნალის კოლექციაა რომელიც შედგება:* |
| `journal[].id` | int | Operation (card) id · *ოპერაციის (ბარათის) id* |
| `journal[].version` | string | Record version in the database (base64 of byte[]) · *ჩანაწერის ვერსია ბაზაში (base64 of byte[])* |
| `journal[].date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `journal[].doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `journal[].doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `journal[].purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `journal[].amount` | decimal | Amount accumulated by the customer (sum of the transactions in which this card participated) · *მყიდველის მიერ დაგროვილი თანხა (ტრანსაზციების თანხის ჯამი, რომელშიც აღნიშნული ბარათი მონაწილეობდა)* |
| `journal[].staff_id` | int | Staff member id · *თანამშრომლის id* |
| `journal[].customer_id` | int | Customer id · *მყიდველის id* |
| `journal[].store_id` | int | Id of the store from which the card was issued · *საწყობის id რომლიდანაც მოხდა ბარათის გაცემა* |
| `journal[].card_code` | string | Card code · *ბარათის კოდი* |
| `journal[].discount_id` | int | Discount id · *ფასდაკლების id* |
| `journal[].status` | bool | Card status (whether it is active) · *ბარათის სტატუსი (აქტიურია თუ არა)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `customer`, `journals` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `customer_id`, `journal` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getAutoServicesOutJournal

Journal of completed requests · *გასული განაცხადების ჟურნალი*

Journal of requests completed at the auto service · *ავტოსერვისიდან გასული განაცხადების ჟურნალი*

**GET** `api/reporting/getAutoServicesOutJournal/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "journals": [{ 
        "id": 5280, 
        "version": "AAAAAAAB3TM=", 
        "date": "2022-12-27 18:10:48", 
        "in_date": "2022-12-29 12:00:00", 
        "doc_num": "36", 
        "waybill_num": null, 
        "doc_type": 107, 
        "purpose": "განაცხადი № 2", 
        "amount": 150, 
        "staff_id": 3, 
        "customer_id": 8, 
        "pay_type": 0 
    }, { 
        "id": 5282, 
        "version": "AAAAAAAB3Tg=", 
        "date": "2022-12-27 18:36:25", 
        "in_date": "2022-12-29 14:30:00", 
        "doc_num": "49", 
        "waybill_num": "0431440360", 
        "doc_type": 107, 
        "purpose": "განაცხადი № 22", 
        "amount": 400.50, 
        "staff_id": 10, 
        "customer_id": 21, 
        "pay_type": 0 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `journal[]` | collection | Collection of completed auto service requests consisting of: · *ავტოსერვისის გასული განაცხადების კოლექციაა რომელიც შედგება:* |
| `journal[].id` | int | Operation id · *ოპერაციის id* |
| `journal[].version` | string | Record version in the database (base64 of byte[]) · *ჩანაწერის ვერსია ბაზაში (base64 of byte[])* |
| `journal[].date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `journal[].in_date` | datetime | Receipt (incoming) date · *შემოსვლის თარიღი* |
| `journal[].doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `journal[].waybill_num` | string | Waybill number (RS - Revenue Service) · *ზედნადების ნომერი (RS)* |
| `journal[].doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `journal[].purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `journal[].amount` | decimal | Operation amount · *ოპერაციის თანხა* |
| `journal[].staff_id` | int | Staff member id · *თანამშრომლის id* |
| `journal[].customer_id` | int | Customer id · *მყიდველის id* |
| `journal[].pay_type` | byte | Payment type (0 - cash, 1 - cashless, 2 - consignment, 3 - installment, 4 - cash/cashless, 5 - free of charge, 6 - other) · *გადახდის ტიპი (0 - ნაღდი, 1 - უნაღდო, 2 - კონსიგნაცია, 3 - განვადება, 4 - ნაღდი/უნაღდო, 5 - უსასყიდლო, 6 - სხვა)* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `journals` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.
> `journal` are described in the field list but do not appear in the JSON example. Verify against a live response before relying on them.

---

### getCustomersCycleReport

Customer turnover · *მყიდველების ბრუნვა*

Customer turnover report · *მყიდელების ბრუნვის რეპორტი*

**GET** `api/reporting/getCustomersCycleReport/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "reports": [{ 
        "id": 1, 
        "start_val": 2000.54, 
        "in_val": 640.00, 
        "out_val": 0.00, 
        "end_val": 2640.54 
    }, { 
        "id": 6, 
        "start_val": 1080.00, 
        "in_val": 0.00, 
        "out_val": 0.00, 
        "end_val": 1080.00 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `reports[]` | collection | Collection of the customer turnover report consisting of: · *მყიდველების ბრუნვის რეპორტის კოლექციაა რომელიც შედგება:* |
| `reports[].id` | int | Customer id · *მყიდველის id* |
| `reports[].start_val` | decimal | Balance at the start of the period · *ნაშთი პერიოდის დასაწყისში* |
| `reports[].in_val` | decimal | Delivered · *მიწოდებული* |
| `reports[].out_val` | decimal | Paid · *გადახდილი* |
| `reports[].end_val` | decimal | Balance at the end of the period · *ნაშთი პერიოდის ბოლოს* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getVendorsCycleReport

Vendor turnover · *მომწოდებლების ბრუნვა*

Vendor turnover report · *მომწოდებლების ბრუნვის რეპორტი*

**GET** `api/reporting/getVendorsCycleReport/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "reports": [{ 
        "id": 2, 
        "start_val": 2887.27, 
        "in_val": 2275.70, 
        "out_val": 3136.00, 
        "end_val": 2026.97 
    }, { 
        "id": 3, 
        "start_val": 4584.28, 
        "in_val": 620.00, 
        "out_val": 323.27, 
        "end_val": 4881.01 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `reports[]` | collection | Collection of the vendor turnover report consisting of: · *მომწოდებლების ბრუნვის რეპორტის კოლექციაა რომელიც შედგება:* |
| `reports[].id` | int | Vendor id · *მომწოდებლის id* |
| `reports[].start_val` | decimal | Balance at the start of the period · *ნაშთი პერიოდის დასაწყისში* |
| `reports[].in_val` | decimal | Received · *მიღებული* |
| `reports[].out_val` | decimal | Paid · *გადახდილი* |
| `reports[].end_val` | decimal | Balance at the end of the period · *ნაშთი პერიოდის ბოლოს* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProductsLastInReport

Information about the last receipt of goods · *საქონლის ბოლო მიღების ინფორმაცია*

Information about the last receipt of goods · *საქონლის ბოლო მიღების ინფორმაცია*

**GET** `api/reporting/getProductsLastInReport/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "reports": [{ 
        "id": 1, 
        "quantity": 2.00, 
        "price": 118.00, 
        "vendor_id": 25, 
        "currency": "GEL", 
        "rate": 1.00, 
        "waybill_date": "2019-04-01T16:12:00", 
        "waybill_num": "", 
        "purpose": "საქონლის მიღება № 10" 
    }, { 
        "id": 2, 
        "quantity": 1.00, 
        "price": 35.70, 
        "vendor_id": 2, 
        "currency": "GEL", 
        "rate": 1.00, 
        "waybill_date": "2019-02-18T13:00:00", 
        "waybill_num": "", 
        "purpose": "shesyidva" 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `reports[]` | collection | Collection of the report on the last receipt of goods consisting of: · *საქონლის ბოლო მიღების ინფორმაციის რეპორტის კოლექციაა რომელიც შედგება:* |
| `reports[].id` | int | Product id · *საქონლის id* |
| `reports[].quantity` | decimal | Quantity · *რაოდენობა* |
| `reports[].price` | decimal | Price · *ფასი* |
| `reports[].vendor_id` | int | Vendor id · *მომწოდებლის id* |
| `reports[].currency` | string | Currency · *ვალუტა* |
| `reports[].rate` | decimal | Currency rate · *ვალუტის კურსი* |
| `reports[].waybill_date` | string | Waybill date · *ზედნადების თარიღი* |
| `reports[].waybill_num` | string | RS number of the waybill · *ზედნადების RS ნომერი* |
| `reports[].purpose` | string | Operation content · *ოპერაციის შინაარსი* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

---

### getProductsInReturnReport

Goods receipts and returns to vendors in detail · *საქონლის მიღება, დაბრუნებები მომწოდებლებზე დეტალურად*

Detailed report of goods receipts and returns to vendors · *საქონლის მიღება, დაბრუნებები მომწოდებლებზე დეტალური რეპორტი*

**GET** `api/reporting/getProductsInReturnReport/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "reports": [{ 
      "date": "2020-08-21T13:01:28.913", 
      "doc_num": "10", 
      "doc_type": 16, 
      "vendor_id": 24, 
      "store_id": 1, 
      "product_id": 1, 
      "unit_id": 1, 
      "quantity": 20, 
      "amount": 2000, 
      "vat": 0 
    }, { 
      "date": "2020-09-22T08:21:27", 
      "doc_num": "0548560688", 
      "doc_type": 32, 
      "vendor_id": 5, 
      "store_id": 1, 
      "product_id": 58, 
      "unit_id": 1, 
      "quantity": 1, 
      "amount": 3, 
      "vat": 0.457627 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `date` | datetime | Operation date · *ოპერაციის თარიღი* |
| `doc_num` | string | Operation number (combination of the number prefix and the number) · *ოპერაციის ნომერი (ოპერაციის ნომრის პრეფიქსისა და ნომრის კომბინაცია)* |
| `doc_type` | int | Document (operation) type · *დოკუმენტის (ოპერაციის) ტიპი* |
| `vendor_id` | int | Vendor id · *მომწოდებლის id* |
| `store_id` | int | Store (warehouse) id · *საწყობის id* |
| `product_id` | int | Product id · *პროდუქტის id* |
| `unit_id` | int | Product unit id · *საქონლის ერთეულის id* |
| `quantity` | decimal | Quantity · *რაოდენობა* |
| `amount` | decimal | Value (cost) · *ღირებულება* |
| `vat` | decimal | VAT amount · *დ.ღ.გ - ს თანხა* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `reports` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---

### getCafeOrderDetailedReport

Orders (cafe) in detail · *შეკვეთები (კაფეს) დეტალურად*

Detailed report of cafe orders · *კაფეს შეკვეთების დეტალური რეპორტი*

**GET** `api/reporting/getCafeOrderDetailedReport/{date_from}/{date_to}`

**Path parameters**

| Field | Type | Description |
|---|---|---|
| `date_from` | datetime | Period start date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საწყისი თარიღი (yyyy-MM-ddTHH:mm:ss)* |
| `date_to` | datetime | Period end date (yyyy-MM-ddTHH:mm:ss) · *პერიოდის საბოლოო თარიღი (yyyy-MM-ddTHH:mm:ss)* |

**Response**

```json
{ 
    "reports": [{ 
      "date": "2020-08-21T13:01:28.913", 
      "doc_num": "20190228100000", 
      "store_id": 1, 
      "status_id": 1, 
      "product_id": 1, 
      "group_id": 1, 
      "unit_id": 1, 
      "quantity": 1, 
      "amount": 2.5 
    }, { 
      "date": "2020-09-22T08:21:27", 
      "doc_num": "0548560688", 
      "store_id": 1, 
      "status_id": 1, 
      "product_id": 58, 
      "group_id": 1, 
      "unit_id": 1, 
      "quantity": 1, 
      "amount": 3 
    }], 
    "ex": null 
}
```

| Field | Type | Description |
|---|---|---|
| `date` | datetime | Order (closing) date · *შეკვეთის (დახურვის) თარიღი* |
| `doc_num` | string | Order number · *შეკვეთის ნომერი* |
| `store_id` | int | Store (warehouse) id · *საწყობის id* |
| `status_id` | int | Order status id (1 - active, 2 - closed, 3 - cancelled) · *შეკვეთის სტატუსის id (1 - აქტიური , 2 - დახურული, 3 - გაუქმებული)* |
| `product_id` | int | Product id · *პროდუქტის id* |
| `group_id` | int | Product group id · *პროდუქტის ჯგუფის id* |
| `unit_id` | int | Product unit id · *საქონლის ერთეულის id* |
| `quantity` | decimal | Quantity · *რაოდენობა* |
| `amount` | decimal | Value (cost) · *ღირებულება* |
| `ex` | string | Error information (if any) · *ინფორმაცია შეცდომის შესახებ (ასეთის არსებობის შემთხვევაში)* |

> [!WARNING]
> **The source documentation is inconsistent here.**
> `reports` appear in the JSON example but are never described in the field list. They are real — the example is what the API returns.

---
