let
    Source = Csv.Document(File.Contents(ParameterFactSalesPath),[Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source,[PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Headers,{
        {"OrderID",type text},{"OrderDate",type date},{"CustomerID",type text},{"GeographyID",type text},
        {"ProductID",type text},{"ChannelID",type text},{"SalespersonID",type text},{"Units",Int64.Type},
        {"UnitPriceINR",Currency.Type},{"DiscountPct",Percentage.Type},{"RevenueINR",Currency.Type},
        {"CostINR",Currency.Type},{"GrossProfitINR",Currency.Type},{"TargetRevenueINR",Currency.Type}
    }),
    Margin = Table.AddColumn(Typed,"GrossMarginPct",each if [RevenueINR]=0 then null else [GrossProfitINR]/[RevenueINR],Percentage.Type),
    Variance = Table.AddColumn(Margin,"RevenueVarianceINR",each [RevenueINR]-[TargetRevenueINR],Currency.Type),
    Attainment = Table.AddColumn(Variance,"TargetAttainmentPct",each if [TargetRevenueINR]=0 then null else [RevenueINR]/[TargetRevenueINR],Percentage.Type)
in
    Attainment
