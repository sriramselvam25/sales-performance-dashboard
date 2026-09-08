# Data Dictionary

## FactSales
| Column | Type | Description |
|---|---|---|
| OrderID | Text | Unique synthetic transaction identifier |
| OrderDate | Date | Transaction date |
| CustomerID | Text | Customer dimension key |
| GeographyID | Text | Geography dimension key |
| ProductID | Text | Product dimension key |
| ChannelID | Text | Channel dimension key |
| SalespersonID | Text | Salesperson dimension key |
| Units | Integer | Units sold |
| UnitPriceINR | Decimal | Unit selling price normalized to INR |
| DiscountPct | Decimal | Transaction discount percentage |
| RevenueINR | Decimal | Net revenue in INR |
| CostINR | Decimal | Synthetic product cost in INR |
| GrossProfitINR | Decimal | Revenue minus cost |
| TargetRevenueINR | Decimal | Synthetic revenue target |

## DimProduct
ProductID, ProductCategory, Product, BaseUnitPriceINR, BaseUnitCostINR.

## DimCustomer
CustomerID, CustomerName, CustomerSegment, GeographyID, Country, Region.

## DimGeography
GeographyID, Region, Country, Currency, FX_to_INR.

## DimChannel
ChannelID, Channel, PriceMultiplier, TypicalDiscount.

## DimSalesperson
SalespersonID, Salesperson, PrimaryRegion, Manager.

## DimDate
Date, Year, Quarter, MonthNumber, Month, YearMonth, Weekday, IsWeekend.
