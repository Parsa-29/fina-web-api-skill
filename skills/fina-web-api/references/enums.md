# Coded values (enums)

Every coded value in the API, collected from the field descriptions where the source documentation buries them.

These matter more than they look. The codes are bare integers with no symbolic names, several fields reuse the same numbers for different meanings (`pay_type` 1 is cashless, but `w_type` 1 does not exist and `t_payer` 1 is the buyer), and a wrong number posts a valid-looking document with the wrong semantics. Check the field name, not just the number.

## `amortization_type`

| Value | Meaning |
|---|---|
| `0` | Declining balance · *ნარჩენი ღირებულება* |
| `1` | Straight line · *წრფივი* |

Used by: [`getInventories`](catalog.md#getinventories)

## `fiscal_print`

| Value | Meaning |
|---|---|
| `0` | Do not print · *არ დაიბეჭდოს* |
| `1` | Detailed · *დეტალური* |
| `2` | Total · *ჯამური* |

Used by: [`getUserPermissions`](directories.md#getuserpermissions)

## `is_company`

| Value | Meaning |
|---|---|
| `true` | Legal entity · *იურიდიული პირი* |
| `false` | Natural person · *ფიზიკური პირი* |

Used by: [`getCustomersByCode`](contragents.md#getcustomersbycode), [`getVendorsByCode`](contragents.md#getvendorsbycode), [`getCustomers`](contragents.md#getcustomers), [`getVendors`](contragents.md#getvendors), [`saveCustomer`](contragents.md#savecustomer), [`saveVendor`](contragents.md#savevendor)

## `is_resident`

| Value | Meaning |
|---|---|
| `true` | Local · *ადგილობრივი* |
| `false` | Foreign citizen · *უცხო ქვეყნის მოქალაქე* |

Used by: [`getCustomersByCode`](contragents.md#getcustomersbycode), [`getVendorsByCode`](contragents.md#getvendorsbycode), [`getCustomers`](contragents.md#getcustomers), [`getVendors`](contragents.md#getvendors), [`saveCustomer`](contragents.md#savecustomer), [`saveVendor`](contragents.md#savevendor)

## `order_status`

| Value | Meaning |
|---|---|
| `1` | Active · *აქტიური* |
| `2` | Received · *მიღებული* |
| `3` | Cancelled · *გაუქმებული* |

Used by: [`getDocCustomerOrder`](documents-read-trade.md#getdoccustomerorder), [`getCustomersOrderJournal`](reporting.md#getcustomersorderjournal)

## `overlap_type`

| Value | Meaning |
|---|---|
| `0` | Offset neither · *არ გადაიხუროს არც ერთი* |
| `1` | Offset the advance · *ავანსი გადაიხუროს* |
| `2` | Offset the advance · *ავანსი გადაიხუროს* |
| `3` | Offset the advance · *ავანსი გადაიხუროს* |

Used by: [`getDocProductOut`](documents-read-trade.md#getdocproductout), [`getDocProvidedService`](documents-read-ops.md#getdocprovidedservice), [`getDocReceivedService`](documents-read-ops.md#getdocreceivedservice), [`getDocAutoService`](documents-read-ops.md#getdocautoservice), [`saveDocProductOut`](documents-write-trade.md#savedocproductout), [`saveDocProvidedService`](documents-write-trade.md#savedocprovidedservice), [`saveDocReceivedService`](documents-write-trade.md#savedocreceivedservice)

## `overlap_type`

| Value | Meaning |
|---|---|
| `0` | Do not separate · *არ გამოეყოს* |
| `1` | Partially · *ნაწილობრივ* |
| `2` | Fully · *სრულად* |

Used by: [`saveDocCustomerAdvanceIn`](documents-write-money.md#savedoccustomeradvancein)

## `pay_type`

| Value | Meaning |
|---|---|
| `0` | Cash · *ნაღდი* |
| `1` | Cashless (bank transfer) · *უნაღდო* |
| `2` | Consignment · *კონსიგნაცია* |
| `3` | Installment · *განვადება* |
| `4` | Cash/cashless · *ნაღდი/უნაღდო* |
| `5` | Free of charge · *უსასყიდლო* |
| `6` | Other · *სხვა* |

Used by: [`getDocCustomerOrder`](documents-read-trade.md#getdoccustomerorder), [`getDocProductOut`](documents-read-trade.md#getdocproductout), [`getDocInventoryOut`](documents-read-trade.md#getdocinventoryout), [`getDocCustomerInventoryReturn`](documents-read-trade.md#getdoccustomerinventoryreturn), [`getDocProvidedService`](documents-read-ops.md#getdocprovidedservice), [`getDocReceivedService`](documents-read-ops.md#getdocreceivedservice), [`getDocCustomerReturn`](documents-read-trade.md#getdoccustomerreturn), [`getDocAutoService`](documents-read-ops.md#getdocautoservice) and 11 more

## `pay_type`

| Value | Meaning |
|---|---|
| `1` | Cash · *ნაღდი* |
| `2` | POS terminal · *ტერმინალი* |
| `3` | Bank transfer · *საბანკო გადარიცხვა* |
| `4` | Installment bank · *განვადების ბანკი* |

Used by: [`saveDocCustomerMoneyIn`](documents-write-money.md#savedoccustomermoneyin), [`saveDocCustomerAdvanceIn`](documents-write-money.md#savedoccustomeradvancein), [`saveDocCustomerMoneyReturn`](documents-write-money.md#savedoccustomermoneyreturn), [`getCustomersMoneyJournal`](reporting.md#getcustomersmoneyjournal), [`getVendorsMoneyJournal`](reporting.md#getvendorsmoneyjournal)

## `pay_type`

| Value | Meaning |
|---|---|
| `0` | Cash · *ნაღდი* |
| `1` | Cashless (bank transfer) · *უნაღდო* |
| `6` | Other · *სხვა* |

Used by: [`getDocProductOutSingle`](documents-read-trade.md#getdocproductoutsingle)

## `price_types`

| Value | Meaning |
|---|---|
| `1` | Purchase price · *მიღების ფასი* |
| `2` | Cost price · *თვითღირებულება* |

Used by: [`getUserPermissions`](directories.md#getuserpermissions)

## `production_type`

| Value | Meaning |
|---|---|
| `0` | Production · *წარმოება* |
| `2` | Adding a part · *ნაწილის დამატება* |

Used by: [`getDocProduction`](documents-read-ops.md#getdocproduction)

## `program_type`

| Value | Meaning |
|---|---|
| `1` | Discount · *ფასდაკლება* |
| `2` | Accrual · *დაგროვება* |
| `3` | Campaign · *აქცია* |
| `4` | Price type · *ფასის ტიპი* |

Used by: [`getLoyaltyCustomerPrograms`](loyalty-and-cards.md#getloyaltycustomerprograms)

## `sex`

| Value | Meaning |
|---|---|
| `true` | Male · *მამრობითი* |
| `false` | Female · *მდედრობითი* |

Used by: [`getLoyaltyCustomers`](loyalty-and-cards.md#getloyaltycustomers), [`getLoyaltyCustomer`](loyalty-and-cards.md#getloyaltycustomer), [`saveLoyaltyCustomer`](loyalty-and-cards.md#saveloyaltycustomer)

## `status`

| Value | Meaning |
|---|---|
| `true` | Active · *აქტიური* |
| `false` | Inactive · *არააქტიური* |

Used by: [`getLoyaltyCustomer`](loyalty-and-cards.md#getloyaltycustomer), [`getLoyaltyCustomerPrograms`](loyalty-and-cards.md#getloyaltycustomerprograms)

## `status_id`

| Value | Meaning |
|---|---|
| `1` | Active · *აქტიური* |
| `2` | Closed · *დახურული* |
| `3` | Cancelled · *გაუქმებული* |

Used by: [`getCafeOrderDetailedReport`](reporting.md#getcafeorderdetailedreport)

## `t_payer`

| Value | Meaning |
|---|---|
| `1` | Buyer · *მყიდველი* |
| `2` | Seller · *გამყიდველი* |

Used by: [`getDocProductOut`](documents-read-trade.md#getdocproductout), [`getDocInventoryOut`](documents-read-trade.md#getdocinventoryout), [`getDocProductMove`](documents-read-ops.md#getdocproductmove), [`getDocInventoryMove`](documents-read-ops.md#getdocinventorymove), [`getDocCustomerInventoryReturn`](documents-read-trade.md#getdoccustomerinventoryreturn), [`getDocCustomerReturn`](documents-read-trade.md#getdoccustomerreturn), [`getDocAutoService`](documents-read-ops.md#getdocautoservice), [`saveDocProductOut`](documents-write-trade.md#savedocproductout) and 2 more

## `t_type`

| Value | Meaning |
|---|---|
| `1` | Road · *საავტომობილო* |
| `2` | Rail · *სარკინიგზო* |
| `3` | Air · *საავიაციო* |
| `4` | Other · *სხვა* |
| `6` | Foreign road · *საავტომობილო უცხო ქვეყნის* |
| `7` | Carrier road · *გადამზიდავი საავტომობილო* |

Used by: [`getDocProductOut`](documents-read-trade.md#getdocproductout), [`getDocInventoryOut`](documents-read-trade.md#getdocinventoryout), [`getDocProductMove`](documents-read-ops.md#getdocproductmove), [`getDocInventoryMove`](documents-read-ops.md#getdocinventorymove), [`getDocCustomerInventoryReturn`](documents-read-trade.md#getdoccustomerinventoryreturn), [`getDocCustomerReturn`](documents-read-trade.md#getdoccustomerreturn), [`getDocAutoService`](documents-read-ops.md#getdocautoservice), [`saveDocProductOut`](documents-write-trade.md#savedocproductout) and 2 more

## `type`

| Value | Meaning |
|---|---|
| `0` | Text · *ტექსტური* |
| `1` | List · *სია* |

Used by: [`getCharacteristics`](catalog.md#getcharacteristics)

## `type`

| Value | Meaning |
|---|---|
| `1` | Administrator · *ადმინისტრატორი* |
| `2` | Operator · *ოპერატორი* |
| `3` | Cashier operator · *მოლარე ოპერატორი* |

Used by: [`getUsers`](directories.md#getusers)

## `type`

| Value | Meaning |
|---|---|
| `0` | Provided services · *გაწეული მომსახურებები* |
| `1` | Salaries · *ხელფასები* |
| `2` | Depreciation · *ცვეთები* |

Used by: [`getDocProduction`](documents-read-ops.md#getdocproduction)

## `type`

| Value | Meaning |
|---|---|
| `0` | production; 1 - disassembly; 2 - adding a part · *წარმოება; 1 - დაშლა; 2 - ნაწილის დამატება* |
| `3` | Separating a part · *ნაწილის გამოყოფა* |

Used by: [`saveDocProduction`](documents-write-production.md#savedocproduction)

## `type_id`

| Value | Meaning |
|---|---|
| `1` | Accrual · *დაგროვება* |
| `2` | Discount · *ფასდაკლება* |
| `5` | Price type · *ფასის ტიპი* |
| `7` | Cashback · *cashback* |

Used by: [`getLoyaltyCardsByHolder`](loyalty-and-cards.md#getloyaltycardsbyholder)

## `usage_type`

| Value | Meaning |
|---|---|
| `0` | On the selected card · *არჩეულ ბარათზე* |
| `1` | On all cards · *ყველა ბარათზე* |
| `2` | Without a card · *ბარათის გარეშე* |

Used by: [`getLoyaltyCustomerPrograms`](loyalty-and-cards.md#getloyaltycustomerprograms)

## `vat`

| Value | Meaning |
|---|---|
| `1` | Taxable · *იბეგრება* |
| `2` | Zero-rated · *ნულოვანი* |
| `3` | Non-taxable · *დაუბეგრავი* |

Used by: [`getProducts`](catalog.md#getproducts), [`getProvidedServices`](catalog.md#getprovidedservices), [`getReceivedServices`](catalog.md#getreceivedservices), [`saveProduct`](catalog.md#saveproduct), [`saveProvidedService`](catalog.md#saveprovidedservice)

## `vat_type`

| Value | Meaning |
|---|---|
| `0` | Not a VAT payer · *არ არის დღგ-ს გადამხდელი* |
| `1` | VAT payer · *დღგ-ს გადამხდელი* |
| `2` | Exempt with the right of deduction · *განთავისუფლებული ჩათვლის უფლებით* |
| `3` | Exempt without the right of deduction · *განთავისუფლებული ჩათვლის უფლების გარეშე* |

Used by: [`getCustomersByCode`](contragents.md#getcustomersbycode), [`getVendorsByCode`](contragents.md#getvendorsbycode), [`getCustomers`](contragents.md#getcustomers), [`getVendors`](contragents.md#getvendors), [`saveCustomer`](contragents.md#savecustomer), [`saveVendor`](contragents.md#savevendor)

## `w_type`

| Value | Meaning |
|---|---|
| `2` | With transportation · *ტრანსპორტირებით* |
| `3` | Without transportation · *ტრანსპორტირების გარეშე* |

Used by: [`getDocProductOut`](documents-read-trade.md#getdocproductout), [`getDocInventoryOut`](documents-read-trade.md#getdocinventoryout), [`getDocAutoService`](documents-read-ops.md#getdocautoservice), [`saveDocProductOut`](documents-write-trade.md#savedocproductout)
