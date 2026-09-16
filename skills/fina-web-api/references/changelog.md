# Version history

Which FINA release introduced each method and field. Check this before relying on anything recent: servers in the field run older builds, and a method that exists in this documentation may simply not be present on the server being integrated with.

The source table uses merged cells, so a version's changes are listed together rather than strictly paired with individual methods. The Georgian original is kept for anything ambiguous.

| Version | Methods affected | Change |
|---|---|---|
| `10.0.20260713` | `getLoyaltyBonusHistory`, `getLoyaltyCustomer`, `getLoyaltyCustomerBalance`, `getLoyaltyCustomerBalances`, `getLoyaltyCustomerGroups`, `getLoyaltyCustomerPrograms`, `getLoyaltyCustomers`, `saveLoyaltyBonusPoint`, `saveLoyaltyCustomer`, `saveLoyaltyGroup` | new methods added |
| `10.0.20260625` | `getDocAdvProduction`, `saveDocAdvProduction` | new methods added; Swagger added |
| `10.0.20260606` | — | PostgreSQL support added |
| `8.0.20260511` | `getCustomers`, `getCustomersByCode`, `getVendors`, `getVendorsByCode`, `saveCustomer`, `saveVendor` | field added: marketing_promotions |
| `8.0.20260303` | `saveDocProduction` | new method added |
| `8.0.20251107` | `getProductsRestSummary` | new method added |
| `8.0.20250926` | `getProductsRestAfter`, `getProductsRestByStoreAfter` | new methods added |
| `8.0.20250901` | `saveDocReceivedService` | new method added |
| `8.0.20250324` | `getCustomers`, `getVendors`, `saveCustomer`, `saveDocBonusCard`, `saveVendor` | fields added: person_code, person_name, person_address, person_tel; field added: birth_date |
| `8.0.20250131` | `saveDocBonusCard` | new method added |
| `8.0.20240520` | `getGiftCardInfoByCode`, `getGiftCards`, `saveDocGiftPayment` | new method added; field added: rest_amount |
| `7.0.20231128` | `getAccountValueDetails` | new method added |
| `7.0.20230904` | `getCafeOrderDetailedReport`, `getProvidedServicePrices` | new method added; field added: status_id |
| `7.0.20230630` | `getAutoServicesOutJournal`, `getContragentSubAccountFields`, `getCustomerAgreements`, `getCustomerSubAccounts`, `getDocAutoService`, `getVendorSubAccounts` | new methods added |
| `7.0.20230504` | `getTransportationMeans` | new method added |
| `7.0.20230213` | `getProductUnits` | fetching all price types added |
| `7.0.20230210` | `getDocProductOut` | field added: check_status |
| `7.0.20230111` | `getCafeOrderDetailedReport` | new method added |
| `6.0.20220930` | `getDocProductOut`, `saveDocProductOut` | fields added: sender, reciever, comment |
| `6.0.20220708` | `getProductUnits` | new method added |
| `6.0.20220616` | `getEntriesJournal`, `getProductPrices`, `getProductPricesAfter`, `saveProduct` | new method added; fields added: amount_currency, currency, debit_quantity, credit_quantity, project_id; field added: currency; field added: weight |
| `6.0.20220207` | `saveDocBonusPayment` | new method added |
| `6.0.20221401` | `getCustomerAddresses`, `getProductsInReturnReport`, `getVendorAddresses` | new methods added |
| `6.0.20211202` | `getCustomersMoneyJournal` | new method added |
| `5.0.20211025` | `getDocProduction` | field added: production_type |
| `5.0.20210212` | `saveDocCustomerOrder` | fields added: invoice_num, invoice_bank, pay_date, delivery_date, reserverd_until |
| `5.0.20210120` | `getProducts` | field added: min_quantity |
| `5.0.20210118` | `getDocProduction`, `getProductionsJournal` | new methods added |
| `5.0.20201225` | `getInventories`, `getInventoriesRest`, `getInventoriesRestAdvance`, `getInventoriesRestArray`, `getInventoriesRestByStore` | new methods added; fields added: amortization_type, service_term, liquidation_cost |
| `3.1.20201005` | `getBonusCardRestByCode`, `getBonusCoeff`, `getLoyaltyCardsByHolder`, `saveDocBonusOperation` | new methods added |
| `3.1.20200921` | `authenticate`, `getPackedProducts` | new method added; token lifetime reduced to 36 hours |
| `3.1.20200828` | `getDocProductOutSingle`, `getProductsBarcodeArray`, `getProductsRestArray`, `getStoreGroups` | new methods added; removed / replaced by getProductsRestArray |
| `3.1.20200808` | `getCharacteristicValuesArray` | new method added |
| `3.1.20200617` | `getProductPricesAdvance` | new method added |
| `3.1.20200605` | `getCharacteristicValues`, `getCharacteristics`, `getCustomersReturnJournal`, `getDocCustomerInventoryReturn`, `getDocCustomerReturn`, `getDocInventoryMove`, `getDocInventoryOut`, `getDocProductMove`, `getDocProductOut`, `getEntriesJournal`, `getInventoryGroups`, `getMovesJournal`, `getProductGroups`, `getProducts`, `getProductsAfter`, `getProductsArray`, `getProductsImageArray`, `getProvidedServiceGroups`, `getRealizesJournal`, `getReceivedServiceGroups`, `getWebProductGroups` | new methods added; fields added: web_group_id, order_id; field added: waybill_num; field added: order_id; fields separated from one another: doc_num |
| `3.1.20200520` | `getProductPrices` | fields added: discount_price, discount_start, discount_end |

---

## By method

The earliest version in which each method is mentioned. A method with no entry predates this changelog.

| Method | First mentioned in |
|---|---|
| `authenticate` | `3.1.20200921` |
| `getAccountValueDetails` | `7.0.20231128` |
| `getAutoServicesOutJournal` | `7.0.20230630` |
| `getBonusCardRestByCode` | `3.1.20201005` |
| `getBonusCoeff` | `3.1.20201005` |
| `getCafeOrderDetailedReport` | `7.0.20230111` |
| `getCharacteristicValues` | `3.1.20200605` |
| `getCharacteristicValuesArray` | `3.1.20200808` |
| `getCharacteristics` | `3.1.20200605` |
| `getContragentSubAccountFields` | `7.0.20230630` |
| `getCustomerAddresses` | `6.0.20221401` |
| `getCustomerAgreements` | `7.0.20230630` |
| `getCustomerSubAccounts` | `7.0.20230630` |
| `getCustomers` | `8.0.20250324` |
| `getCustomersByCode` | `8.0.20260511` |
| `getCustomersMoneyJournal` | `6.0.20211202` |
| `getCustomersReturnJournal` | `3.1.20200605` |
| `getDocAdvProduction` | `10.0.20260625` |
| `getDocAutoService` | `7.0.20230630` |
| `getDocCustomerInventoryReturn` | `3.1.20200605` |
| `getDocCustomerReturn` | `3.1.20200605` |
| `getDocInventoryMove` | `3.1.20200605` |
| `getDocInventoryOut` | `3.1.20200605` |
| `getDocProductMove` | `3.1.20200605` |
| `getDocProductOut` | `3.1.20200605` |
| `getDocProductOutSingle` | `3.1.20200828` |
| `getDocProduction` | `5.0.20210118` |
| `getEntriesJournal` | `3.1.20200605` |
| `getGiftCardInfoByCode` | `8.0.20240520` |
| `getGiftCards` | `8.0.20240520` |
| `getInventories` | `5.0.20201225` |
| `getInventoriesRest` | `5.0.20201225` |
| `getInventoriesRestAdvance` | `5.0.20201225` |
| `getInventoriesRestArray` | `5.0.20201225` |
| `getInventoriesRestByStore` | `5.0.20201225` |
| `getInventoryGroups` | `3.1.20200605` |
| `getLoyaltyBonusHistory` | `10.0.20260713` |
| `getLoyaltyCardsByHolder` | `3.1.20201005` |
| `getLoyaltyCustomer` | `10.0.20260713` |
| `getLoyaltyCustomerBalance` | `10.0.20260713` |
| `getLoyaltyCustomerBalances` | `10.0.20260713` |
| `getLoyaltyCustomerGroups` | `10.0.20260713` |
| `getLoyaltyCustomerPrograms` | `10.0.20260713` |
| `getLoyaltyCustomers` | `10.0.20260713` |
| `getMovesJournal` | `3.1.20200605` |
| `getPackedProducts` | `3.1.20200921` |
| `getProductGroups` | `3.1.20200605` |
| `getProductPrices` | `3.1.20200520` |
| `getProductPricesAdvance` | `3.1.20200617` |
| `getProductPricesAfter` | `6.0.20220616` |
| `getProductUnits` | `6.0.20220708` |
| `getProductionsJournal` | `5.0.20210118` |
| `getProducts` | `3.1.20200605` |
| `getProductsAfter` | `3.1.20200605` |
| `getProductsArray` | `3.1.20200605` |
| `getProductsBarcodeArray` | `3.1.20200828` |
| `getProductsImageArray` | `3.1.20200605` |
| `getProductsInReturnReport` | `6.0.20221401` |
| `getProductsRestAfter` | `8.0.20250926` |
| `getProductsRestArray` | `3.1.20200828` |
| `getProductsRestByStoreAfter` | `8.0.20250926` |
| `getProductsRestSummary` | `8.0.20251107` |
| `getProvidedServiceGroups` | `3.1.20200605` |
| `getProvidedServicePrices` | `7.0.20230904` |
| `getRealizesJournal` | `3.1.20200605` |
| `getReceivedServiceGroups` | `3.1.20200605` |
| `getStoreGroups` | `3.1.20200828` |
| `getTransportationMeans` | `7.0.20230504` |
| `getVendorAddresses` | `6.0.20221401` |
| `getVendorSubAccounts` | `7.0.20230630` |
| `getVendors` | `8.0.20250324` |
| `getVendorsByCode` | `8.0.20260511` |
| `getWebProductGroups` | `3.1.20200605` |
| `saveCustomer` | `8.0.20250324` |
| `saveDocAdvProduction` | `10.0.20260625` |
| `saveDocBonusCard` | `8.0.20250131` |
| `saveDocBonusOperation` | `3.1.20201005` |
| `saveDocBonusPayment` | `6.0.20220207` |
| `saveDocCustomerOrder` | `5.0.20210212` |
| `saveDocGiftPayment` | `8.0.20240520` |
| `saveDocProductOut` | `6.0.20220930` |
| `saveDocProduction` | `8.0.20260303` |
| `saveDocReceivedService` | `8.0.20250901` |
| `saveLoyaltyBonusPoint` | `10.0.20260713` |
| `saveLoyaltyCustomer` | `10.0.20260713` |
| `saveLoyaltyGroup` | `10.0.20260713` |
| `saveProduct` | `6.0.20220616` |
| `saveVendor` | `8.0.20250324` |
