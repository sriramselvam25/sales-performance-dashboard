# Data Model

`FactSales` is the central transaction fact table.

## Relationships
All relationships are **one-to-many (1:*)**, single direction from dimension to fact:

- `DimDate[Date]` → `FactSales[OrderDate]`
- `DimCustomer[CustomerID]` → `FactSales[CustomerID]`
- `DimGeography[GeographyID]` → `FactSales[GeographyID]`
- `DimProduct[ProductID]` → `FactSales[ProductID]`
- `DimChannel[ChannelID]` → `FactSales[ChannelID]`
- `DimSalesperson[SalespersonID]` → `FactSales[SalespersonID]`

Mark `DimDate` as the model Date table. Disable automatic date/time. Keep descriptive attributes in dimensions and additive transaction metrics in `FactSales`.

## Grain
One row in `FactSales` represents one synthetic sales order transaction.

## Why a Star Schema?
The model separates business dimensions from transaction metrics, keeps DAX easier to reason about, improves report performance, and demonstrates an enterprise-style semantic modelling approach rather than a flat spreadsheet model.
