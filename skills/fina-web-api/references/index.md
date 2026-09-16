# Method index

All 150 methods in FINA WEB API 10.0. Find the method here, then open the reference file named in the last column for its full request/response schema.

Reading this table first is worth the tokens: the API has several near-identical methods whose differences matter (a full pull versus an incremental one, all stores versus a single store), and choosing wrong produces code that looks right and syncs the wrong data.

## Quick routing

| If you need to… | Look in |
|---|---|
| Customers, vendors and their attributes | [`contragents.md`](contragents.md) |
| Products, services, fixed assets and their catalogues | [`catalog.md`](catalog.md) |
| Prices, price types, discounts and units | [`pricing.md`](pricing.md) |
| Stock balances and cost | [`stock.md`](stock.md) |
| Stores, users, staff and other directories | [`directories.md`](directories.md) |
| Gift cards, bonus cards and loyalty | [`loyalty-and-cards.md`](loyalty-and-cards.md) |
| Bookkeeping accounts and entries | [`accounting.md`](accounting.md) |
| Reading documents — sales, orders and returns | [`documents-read-trade.md`](documents-read-trade.md) |
| Reading documents — transfers, services and production | [`documents-read-ops.md`](documents-read-ops.md) |
| Writing documents — sales, purchases, transfers and orders | [`documents-write-trade.md`](documents-write-trade.md) |
| Writing documents — money, advances and card payments | [`documents-write-money.md`](documents-write-money.md) |
| Writing documents — issuing cards and points | [`documents-write-cards.md`](documents-write-cards.md) |
| Writing documents — production | [`documents-write-production.md`](documents-write-production.md) |
| Journals and reports | [`reporting.md`](reporting.md) |
| Authentication and shared conventions | [`conventions.md`](conventions.md) |

---

## Customers, vendors and their attributes

→ [`contragents.md`](contragents.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getCustomersByCode`](contragents.md#getcustomersbycode) | GET | `api/operation/getCustomersByCode/{code}` | Customers by identification code |
| [`getVendorsByCode`](contragents.md#getvendorsbycode) | GET | `api/operation/getVendorsByCode/{code}` | Vendors by identification code |
| [`getCustomers`](contragents.md#getcustomers) | GET | `api/operation/getCustomers` | Customers |
| [`getVendors`](contragents.md#getvendors) | GET | `api/operation/getVendors` | Vendors |
| [`getCustomerAdditionalFields`](contragents.md#getcustomeradditionalfields) | GET | `api/operation/getCustomerAdditionalFields` | Description of the customer's additional fields |
| [`getVendorAdditionalFields`](contragents.md#getvendoradditionalfields) | GET | `api/operation/getVendorAdditionalFields` | Description of the vendor's additional fields |
| [`getCustomerGroups`](contragents.md#getcustomergroups) | GET | `api/operation/getCustomerGroups` | Customer groups |
| [`getVendorGroups`](contragents.md#getvendorgroups) | GET | `api/operation/getVendorGroups` | Vendor groups |
| [`getCustomerAddresses`](contragents.md#getcustomeraddresses) | GET | `api/operation/getCustomerAddresses` | Customer addresses |
| [`getVendorAddresses`](contragents.md#getvendoraddresses) | GET | `api/operation/getVendorAddresses` | Vendor addresses |
| [`getCustomerAgreements`](contragents.md#getcustomeragreements) | GET | `api/operation/getCustomerAgreements` | Customer agreements |
| [`getContragentSubAccountFields`](contragents.md#getcontragentsubaccountfields) | GET | `api/operation/getContragentSubAccountFields` | Description of contragent sub-account fields |
| [`getCustomerSubAccounts`](contragents.md#getcustomersubaccounts) | GET | `api/operation/getCustomerSubAccounts` | Customer sub-accounts |
| [`getVendorSubAccounts`](contragents.md#getvendorsubaccounts) | GET | `api/operation/getVendorSubAccounts` | Vendor sub-accounts |
| [`saveCustomer`](contragents.md#savecustomer) | POST | `api/operation/saveCustomer` | Save a customer |
| [`saveVendor`](contragents.md#savevendor) | POST | `api/operation/saveVendor` | Save a vendor |

## Products, services, fixed assets and their catalogues

→ [`catalog.md`](catalog.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getProductGroups`](catalog.md#getproductgroups) | GET | `api/operation/getProductGroups` | Product groups |
| [`getWebProductGroups`](catalog.md#getwebproductgroups) | GET | `api/operation/getWebProductGroups` | Alternative (web) product groups |
| [`getProvidedServiceGroups`](catalog.md#getprovidedservicegroups) | GET | `api/operation/getProvidedServiceGroups` | Provided service groups |
| [`getReceivedServiceGroups`](catalog.md#getreceivedservicegroups) | GET | `api/operation/getReceivedServiceGroups` | Received service groups |
| [`getInventoryGroups`](catalog.md#getinventorygroups) | GET | `api/operation/getInventoryGroups` | Fixed asset groups |
| [`getProducts`](catalog.md#getproducts) | GET | `api/operation/getProducts` | Product catalogue |
| [`getProductsArray`](catalog.md#getproductsarray) | POST | `api/operation/getProductsArray` | Selected product catalogue |
| [`getProductsAfter`](catalog.md#getproductsafter) | GET | `api/operation/getProductsAfter/{after_date}` | Product catalogue |
| [`getProvidedServices`](catalog.md#getprovidedservices) | GET | `api/operation/getProvidedServices` | Provided services catalogue |
| [`getReceivedServices`](catalog.md#getreceivedservices) | GET | `api/operation/getReceivedServices` | Received services catalogue |
| [`getInventories`](catalog.md#getinventories) | GET | `api/operation/getInventories` | Fixed assets catalogue |
| [`getProductAdditionalFields`](catalog.md#getproductadditionalfields) | GET | `api/operation/getProductAdditionalFields` | Description of the product's additional fields |
| [`getProvidedServiceAdditionalFields`](catalog.md#getprovidedserviceadditionalfields) | GET | `api/operation/getProvidedServiceAdditionalFields` | Description of the provided service's additional fields |
| [`getInventoryAdditionalFields`](catalog.md#getinventoryadditionalfields) | GET | `api/operation/getInventoryAdditionalFields` | Description of the fixed asset's additional fields |
| [`getCharacteristics`](catalog.md#getcharacteristics) | GET | `api/operation/getCharacteristics` | Description of product characteristics |
| [`getCharacteristicValues`](catalog.md#getcharacteristicvalues) | GET | `api/operation/getCharacteristicValues` | Product characteristics |
| [`getCharacteristicValuesArray`](catalog.md#getcharacteristicvaluesarray) | POST | `api/operation/getCharacteristicValuesArray` | Characteristics of selected products |
| [`getPackedProducts`](catalog.md#getpackedproducts) | GET | `api/operation/getPackedProducts` | Products grouped together |
| [`getSubCodeTypes`](catalog.md#getsubcodetypes) | GET | `api/operation/getSubCodeTypes` | Sub-code types |
| [`getProductSubCodes`](catalog.md#getproductsubcodes) | GET | `api/operation/getProductSubCodes` | Product sub-codes |
| [`getProductPlaces`](catalog.md#getproductplaces) | GET | `api/operation/getProductPlaces` | Product storage places |
| [`getProductImages`](catalog.md#getproductimages) | GET | `api/operation/getProductImages/{product}` | Product images |
| [`getProductsImageArray`](catalog.md#getproductsimagearray) | POST | `api/operation/getProductsImageArray` | Images of selected products |
| [`getProductsBarcodeArray`](catalog.md#getproductsbarcodearray) | POST | `api/operation/getProductsBarcodeArray` | Barcodes of selected products |
| [`getProductsOnWay`](catalog.md#getproductsonway) | GET | `api/operation/getProductsOnWay` | Pending product orders (goods in transit) |
| [`saveProduct`](catalog.md#saveproduct) | POST | `api/operation/saveProduct` | Save a product |
| [`saveProvidedService`](catalog.md#saveprovidedservice) | POST | `api/operation/saveProvidedService` | Save a provided service |

## Prices, price types, discounts and units

→ [`pricing.md`](pricing.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getProductPrices`](pricing.md#getproductprices) | GET | `api/operation/getProductPrices` | Product prices |
| [`getProvidedServicePrices`](pricing.md#getprovidedserviceprices) | GET | `api/operation/getProvidedServicePrices` | Provided service prices |
| [`getProductUnits`](pricing.md#getproductunits) | GET | `api/operation/getProductUnits` | Additional product units |
| [`getProductPricesAdvance`](pricing.md#getproductpricesadvance) | POST | `api/operation/getProductPricesAdvance` | Prices of specified products |
| [`getProductPricesAfter`](pricing.md#getproductpricesafter) | GET | `api/operation/getProductPricesAfter/{after_date}` | Updated product prices |
| [`getPriceTypes`](pricing.md#getpricetypes) | GET | `api/operation/getPriceTypes` | Price types |
| [`getDiscountTypes`](pricing.md#getdiscounttypes) | GET | `api/operation/getDiscountTypes` | Discount kinds |
| [`getUnits`](pricing.md#getunits) | GET | `api/operation/getUnits` | Units of measurement |

## Stock balances and cost

→ [`stock.md`](stock.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getProductsRest`](stock.md#getproductsrest) | GET | `api/operation/getProductsRest` | Current product stock balance for each store |
| [`getProductsRestAfter`](stock.md#getproductsrestafter) | GET | `api/operation/getProductsRestAfter/{after_date}` | Current stock balance for products involved in a changed operation, for each store |
| [`getProductsRestArray`](stock.md#getproductsrestarray) | POST | `api/operation/getProductsRestArray` | Current stock balance of selected products for each store |
| [`getProductsRestByStore`](stock.md#getproductsrestbystore) | GET | `api/operation/getProductsRestByStore/{store}` | Current product stock balance for a specific store |
| [`getProductsRestSummary`](stock.md#getproductsrestsummary) | POST | `api/operation/getProductsRestSummary` | Total product stock balance |
| [`getProductsRestByStoreAfter`](stock.md#getproductsrestbystoreafter) | GET | `api/operation/getProductsRestByStoreAfter/{store}/{after_date}` | Current stock balance for products involved in a changed operation, for a specific store |
| [`getProductsRestAdvance`](stock.md#getproductsrestadvance) | POST | `api/operation/getProductsRestAdvance` | Current product stock balance with price |
| [`getSubProductsRest`](stock.md#getsubproductsrest) | GET | `api/operation/getSubProductsRest` | Current stock balance of product sub-codes for each store |
| [`getInventoriesRest`](stock.md#getinventoriesrest) | GET | `api/operation/getInventoriesRest` | Current fixed asset stock balance for each store |
| [`getInventoriesRestArray`](stock.md#getinventoriesrestarray) | POST | `api/operation/getInventoriesRestArray` | Current stock balance of selected fixed assets for each store |
| [`getInventoriesRestByStore`](stock.md#getinventoriesrestbystore) | GET | `api/operation/getInventoriesRestByStore/{store}` | Current fixed asset stock balance for a specific store |
| [`getInventoriesRestAdvance`](stock.md#getinventoriesrestadvance) | POST | `api/operation/getInventoriesRestAdvance` | Current fixed asset stock balance with price |
| [`getProductsSelfCost`](stock.md#getproductsselfcost) | POST | `api/operation/getProductsSelfCost` | Product cost price |

## Stores, users, staff and other directories

→ [`directories.md`](directories.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getStoreGroups`](directories.md#getstoregroups) | GET | `api/operation/getStoreGroups` | Store groups |
| [`getStores`](directories.md#getstores) | GET | `api/operation/getStores` | Stores (warehouses) |
| [`getProjects`](directories.md#getprojects) | GET | `api/operation/getProjects` | Projects |
| [`getTerminals`](directories.md#getterminals) | GET | `api/operation/getTerminals` | POS terminals |
| [`getCashes`](directories.md#getcashes) | GET | `api/operation/getCashes` | Cash registers |
| [`getUsers`](directories.md#getusers) | GET | `api/operation/getUsers` | Users |
| [`getUserPermissions`](directories.md#getuserpermissions) | GET | `api/operation/getUserPermissions/{user}` | User permissions |
| [`getBankAccounts`](directories.md#getbankaccounts) | GET | `api/operation/getBankAccounts` | Bank accounts |
| [`getCreditBanks`](directories.md#getcreditbanks) | GET | `api/operation/getCreditBanks` | Installment banks |
| [`getStaffGroups`](directories.md#getstaffgroups) | GET | `api/operation/getStaffGroups` | Staff groups |
| [`getStaffs`](directories.md#getstaffs) | GET | `api/operation/getStaffs` | Staff members |
| [`getTransportationMeans`](directories.md#gettransportationmeans) | GET | `api/operation/getTransportationMeans` | Transportation means |
| [`getStaffAdditionalFields`](directories.md#getstaffadditionalfields) | GET | `api/operation/getStaffAdditionalFields` | Description of the staff member's additional fields |
| [`saveStaff`](directories.md#savestaff) | POST | `api/operation/saveStaff` | Save a staff member |

## Gift cards, bonus cards and loyalty

→ [`loyalty-and-cards.md`](loyalty-and-cards.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getGiftCards`](loyalty-and-cards.md#getgiftcards) | GET | `api/operation/getGiftCards` | Gift cards |
| [`getGiftCardInfoByCode`](loyalty-and-cards.md#getgiftcardinfobycode) | GET | `api/operation/getGiftCardInfoByCode/{code}` | Gift card information |
| [`getBonusCoeff`](loyalty-and-cards.md#getbonuscoeff) | GET | `api/operation/getBonusCoeff` | Bonus coefficient |
| [`getLoyaltyCardsByHolder`](loyalty-and-cards.md#getloyaltycardsbyholder) | GET | `api/operation/getLoyaltyCardsByHolder/{holder_code}` | Loyalty cards |
| [`getBonusCardRestByCode`](loyalty-and-cards.md#getbonuscardrestbycode) | GET | `api/operation/getBonusCardRestByCode/{code}` | Bonus card balance |
| [`getLoyaltyCustomers`](loyalty-and-cards.md#getloyaltycustomers) | GET | `api/operation/getLoyaltyCustomers` | Loyalty (Cloud) cards |
| [`getLoyaltyCustomer`](loyalty-and-cards.md#getloyaltycustomer) | GET | `api/operation/getLoyaltyCustomer/{id}` | Loyalty (Cloud) card |
| [`getLoyaltyCustomerPrograms`](loyalty-and-cards.md#getloyaltycustomerprograms) | GET | `api/operation/getLoyaltyCustomerPrograms` | Loyalty (Cloud) programs |
| [`getLoyaltyCustomerGroups`](loyalty-and-cards.md#getloyaltycustomergroups) | GET | `api/operation/getLoyaltyCustomerGroups` | Loyalty (Cloud) groups |
| [`getLoyaltyCustomerBalances`](loyalty-and-cards.md#getloyaltycustomerbalances) | GET | `api/operation/getLoyaltyCustomerBalances` | Loyalty (Cloud) card balances |
| [`getLoyaltyCustomerBalance`](loyalty-and-cards.md#getloyaltycustomerbalance) | GET | `api/operation/getLoyaltyCustomerBalance/{qr_code}` | Loyalty (Cloud) card balance |
| [`getLoyaltyBonusHistory`](loyalty-and-cards.md#getloyaltybonushistory) | GET | `api/operation/getLoyaltyBonusHistory/{qr_code}` | Loyalty (Cloud) card accrual/spending history |
| [`saveLoyaltyCustomer`](loyalty-and-cards.md#saveloyaltycustomer) | POST | `api/operation/saveLoyaltyCustomer` | Save a loyalty (Cloud) card |
| [`saveLoyaltyGroup`](loyalty-and-cards.md#saveloyaltygroup) | POST | `api/operation/saveLoyaltyGroup` | Save a loyalty (Cloud) group |
| [`saveLoyaltyBonusPoint`](loyalty-and-cards.md#saveloyaltybonuspoint) | POST | `api/operation/saveLoyaltyBonusPoint` | Grant / deduct loyalty (Cloud) points |

## Bookkeeping accounts and entries

→ [`accounting.md`](accounting.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getAccountValue`](accounting.md#getaccountvalue) | POST | `api/operation/getAccountValue` | Accounting account value |
| [`getAccountValueDetails`](accounting.md#getaccountvaluedetails) | POST | `api/operation/getAccountValueDetails` | Itemised accounting account values |
| [`getEntriesJournal`](accounting.md#getentriesjournal) | GET | `api/reporting/getEntriesJournal/{date_from}/{date_to}` | Journal of accounting entries |

## Reading documents — sales, orders and returns

→ [`documents-read-trade.md`](documents-read-trade.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getDocTypes`](documents-read-trade.md#getdoctypes) | GET | `api/operation/getDocTypes` | List of operations |
| [`getDocAdditionalFields`](documents-read-trade.md#getdocadditionalfields) | GET | `api/operation/getDocAdditionalFields/{type}` | Description of the document's additional fields |
| [`getDocDiscountCard`](documents-read-trade.md#getdocdiscountcard) | GET | `api/operation/getDocDiscountCard/{id}` | Issued discount card |
| [`getDocCustomerOrder`](documents-read-trade.md#getdoccustomerorder) | GET | `api/operation/getDocCustomerOrder/{id}` | Order received from a customer |
| [`getDocProductOut`](documents-read-trade.md#getdocproductout) | GET | `api/operation/getDocProductOut/{id}` | Goods sale |
| [`getDocProductOutSingle`](documents-read-trade.md#getdocproductoutsingle) | GET | `api/operation/getDocProductOutSingle/{id}` | Retail sale |
| [`getDocInventoryOut`](documents-read-trade.md#getdocinventoryout) | GET | `api/operation/getDocInventoryOut/{id}` | Fixed asset sale |
| [`getDocCustomerInventoryReturn`](documents-read-trade.md#getdoccustomerinventoryreturn) | GET | `api/operation/getDocCustomerInventoryReturn/{id}` | Return of a fixed asset from a customer |
| [`getDocCustomerReturn`](documents-read-trade.md#getdoccustomerreturn) | GET | `api/operation/getDocCustomerReturn/{id}` | Return from a customer |

## Reading documents — transfers, services and production

→ [`documents-read-ops.md`](documents-read-ops.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getDocProductMove`](documents-read-ops.md#getdocproductmove) | GET | `api/operation/getDocProductMove/{id}` | Goods transfer |
| [`getDocInventoryMove`](documents-read-ops.md#getdocinventorymove) | GET | `api/operation/getDocInventoryMove/{id}` | Fixed asset transfer |
| [`getDocProvidedService`](documents-read-ops.md#getdocprovidedservice) | GET | `api/operation/getDocProvidedService/{id}` | Provision of a service |
| [`getDocReceivedService`](documents-read-ops.md#getdocreceivedservice) | GET | `api/operation/getDocReceivedService/{id}` | Receipt of a service |
| [`getDocProduction`](documents-read-ops.md#getdocproduction) | GET | `api/operation/getDocProduction/{id}` | Production, adding goods - repair |
| [`getDocAutoService`](documents-read-ops.md#getdocautoservice) | GET | `api/operation/getDocAutoService/{id}` | Auto service request |
| [`getDocAdvProduction`](documents-read-ops.md#getdocadvproduction) | GET | `api/operation/getDocAdvProduction/{id}` | Complex production/disassembly |

## Writing documents — sales, purchases, transfers and orders

→ [`documents-write-trade.md`](documents-write-trade.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`updateRsStatus`](documents-write-trade.md#updatersstatus) | POST | `api/operation/updateRsStatus` | Update the RS status of an existing waybill |
| [`saveDocCustomerOrder`](documents-write-trade.md#savedoccustomerorder) | POST | `api/operation/saveDocCustomerOrder` | Order received from a customer |
| [`saveDocProductOut`](documents-write-trade.md#savedocproductout) | POST | `api/operation/saveDocProductOut` | Goods sale |
| [`saveDocProductMove`](documents-write-trade.md#savedocproductmove) | POST | `api/operation/saveDocProductMove` | Internal transfer |
| [`saveDocProvidedService`](documents-write-trade.md#savedocprovidedservice) | POST | `api/operation/saveDocProvidedService` | Provision of a service |
| [`saveDocReceivedService`](documents-write-trade.md#savedocreceivedservice) | POST | `api/operation/saveDocReceivedService` | Receipt of a service |
| [`saveDocCustomerReturn`](documents-write-trade.md#savedoccustomerreturn) | POST | `api/operation/saveDocCustomerReturn` | Return of goods from a customer |
| [`saveDocProductIn`](documents-write-trade.md#savedocproductin) | POST | `api/operation/saveDocProductIn` | Goods purchase |
| [`saveDocProductCancel`](documents-write-trade.md#savedocproductcancel) | POST | `api/operation/saveDocProductCancel` | Write-off of goods |
| [`saveDocCafeOrder`](documents-write-trade.md#savedoccafeorder) | POST | `api/operation/saveDocCafeOrder` | Restaurant order |

## Writing documents — money, advances and card payments

→ [`documents-write-money.md`](documents-write-money.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`saveDocCustomerMoneyIn`](documents-write-money.md#savedoccustomermoneyin) | POST | `api/operation/saveDocCustomerMoneyIn` | Receipt of money |
| [`saveDocCustomerAdvanceIn`](documents-write-money.md#savedoccustomeradvancein) | POST | `api/operation/saveDocCustomerAdvanceIn` | Receipt of an advance |
| [`saveDocCustomerMoneyReturn`](documents-write-money.md#savedoccustomermoneyreturn) | POST | `api/operation/saveDocCustomerMoneyReturn` | Return of money |
| [`saveDocBonusPayment`](documents-write-money.md#savedocbonuspayment) | POST | `api/operation/saveDocBonusPayment` | Payment with points |
| [`saveDocGiftPayment`](documents-write-money.md#savedocgiftpayment) | POST | `api/operation/saveDocGiftPayment` | Redeem a gift card |

## Writing documents — issuing cards and points

→ [`documents-write-cards.md`](documents-write-cards.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`saveDocDiscountCard`](documents-write-cards.md#savedocdiscountcard) | POST | `api/operation/saveDocDiscountCard` | Issue a discount card |
| [`saveDocBonusCard`](documents-write-cards.md#savedocbonuscard) | POST | `api/operation/saveDocBonusCard` | Issue an accrual (bonus) card |
| [`saveDocGiftCard`](documents-write-cards.md#savedocgiftcard) | POST | `api/operation/saveDocGiftCard` | Issue a gift card |
| [`saveDocBonusOperation`](documents-write-cards.md#savedocbonusoperation) | POST | `api/operation/saveDocBonusOperation` | Accrue/spend points |

## Writing documents — production

→ [`documents-write-production.md`](documents-write-production.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`saveDocProduction`](documents-write-production.md#savedocproduction) | POST | `api/operation/saveDocProduction` | Production of goods |
| [`saveDocAdvProduction`](documents-write-production.md#savedocadvproduction) | POST | `api/operation/saveDocAdvProduction` | Complex production/disassembly of goods |

## Journals and reports

→ [`reporting.md`](reporting.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`getRealizesJournal`](reporting.md#getrealizesjournal) | GET | `api/reporting/getRealizesJournal/{date_from}/{date_to}` | Sales journal |
| [`getMovesJournal`](reporting.md#getmovesjournal) | GET | `api/reporting/getMovesJournal/{date_from}/{date_to}` | Transfers journal |
| [`getDocProvidedServicesJournal`](reporting.md#getdocprovidedservicesjournal) | GET | `api/reporting/getDocProvidedServicesJournal/{date_from}/{date_to}` | Journal of provided services |
| [`getDocReceivedServicesJournal`](reporting.md#getdocreceivedservicesjournal) | GET | `api/reporting/getDocReceivedServicesJournal/{date_from}/{date_to}` | Journal of received services |
| [`getCustomersOrderJournal`](reporting.md#getcustomersorderjournal) | GET | `api/reporting/getCustomersOrderJournal/{date_from}/{date_to}` | Journal of customer orders |
| [`getCustomersReturnJournal`](reporting.md#getcustomersreturnjournal) | GET | `api/reporting/getCustomersReturnJournal/{date_from}/{date_to}` | Journal of returns from customers |
| [`getCustomersMoneyJournal`](reporting.md#getcustomersmoneyjournal) | GET | `api/reporting/getCustomersMoneyJournal/{date_from}/{date_to}` | Journal of money received from and returned to customers, and of advances |
| [`getVendorsMoneyJournal`](reporting.md#getvendorsmoneyjournal) | GET | `api/reporting/getVendorsMoneyJournal/{date_from}/{date_to}` | Journal of money issued to and returned from vendors, and of advances |
| [`getProductionsJournal`](reporting.md#getproductionsjournal) | GET | `api/reporting/getProductionsJournal/{date_from}/{date_to}` | Journal of productions |
| [`getDiscountCardsJournal`](reporting.md#getdiscountcardsjournal) | GET | `api/reporting/getDiscountCardsJournal/{date_from}/{date_to}` | Journal of discount cards |
| [`getAutoServicesOutJournal`](reporting.md#getautoservicesoutjournal) | GET | `api/reporting/getAutoServicesOutJournal/{date_from}/{date_to}` | Journal of completed requests |
| [`getCustomersCycleReport`](reporting.md#getcustomerscyclereport) | GET | `api/reporting/getCustomersCycleReport/{date_from}/{date_to}` | Customer turnover |
| [`getVendorsCycleReport`](reporting.md#getvendorscyclereport) | GET | `api/reporting/getVendorsCycleReport/{date_from}/{date_to}` | Vendor turnover |
| [`getProductsLastInReport`](reporting.md#getproductslastinreport) | GET | `api/reporting/getProductsLastInReport/{date_from}/{date_to}` | Information about the last receipt of goods |
| [`getProductsInReturnReport`](reporting.md#getproductsinreturnreport) | GET | `api/reporting/getProductsInReturnReport/{date_from}/{date_to}` | Goods receipts and returns to vendors in detail |
| [`getCafeOrderDetailedReport`](reporting.md#getcafeorderdetailedreport) | GET | `api/reporting/getCafeOrderDetailedReport/{date_from}/{date_to}` | Orders (cafe) in detail |

## Authentication and shared conventions

→ [`conventions.md`](conventions.md)

| Method | Verb | Endpoint | Purpose |
|---|---|---|---|
| [`authenticate`](conventions.md#authenticate) | POST | `api/authentication/authenticate` | Authorization |
