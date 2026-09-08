-- 1. Executive KPI summary
SELECT SUM(RevenueINR) TotalRevenue,
       SUM(GrossProfitINR) GrossProfit,
       SUM(GrossProfitINR)/NULLIF(SUM(RevenueINR),0) GrossMarginPct,
       SUM(RevenueINR)/NULLIF(SUM(TargetRevenueINR),0) TargetAttainmentPct,
       SUM(RevenueINR)/COUNT(DISTINCT OrderID) AverageOrderValue
FROM FactSales;

-- 2. YoY growth
WITH yearly AS (
 SELECT YEAR(OrderDate) SalesYear, SUM(RevenueINR) Revenue
 FROM FactSales GROUP BY YEAR(OrderDate)
)
SELECT cur.SalesYear,cur.Revenue,prev.Revenue PriorYearRevenue,
       (cur.Revenue-prev.Revenue)/NULLIF(prev.Revenue,0) YoYGrowthPct
FROM yearly cur LEFT JOIN yearly prev ON cur.SalesYear=prev.SalesYear+1;

-- 3. Regional contribution and target attainment
SELECT Region,SUM(RevenueINR) Revenue,
       SUM(GrossProfitINR)/NULLIF(SUM(RevenueINR),0) GrossMarginPct,
       SUM(RevenueINR)/NULLIF(SUM(TargetRevenueINR),0) TargetAttainmentPct,
       SUM(RevenueINR)/(SELECT SUM(RevenueINR) FROM FactSales) RegionalContributionPct
FROM FactSales GROUP BY Region ORDER BY Revenue DESC;

-- 4. Product margin leakage
SELECT TOP 10 p.Product,SUM(f.RevenueINR) Revenue,
       SUM(f.GrossProfitINR)/NULLIF(SUM(f.RevenueINR),0) GrossMarginPct
FROM FactSales f JOIN DimProduct p ON f.ProductID=p.ProductID
GROUP BY p.Product ORDER BY GrossMarginPct;

-- 5. Salesperson target attainment
SELECT s.Salesperson,s.PrimaryRegion,SUM(f.RevenueINR) Revenue,
       SUM(f.TargetRevenueINR) TargetRevenue,
       SUM(f.RevenueINR)/NULLIF(SUM(f.TargetRevenueINR),0) TargetAttainmentPct
FROM FactSales f JOIN DimSalesperson s ON f.SalespersonID=s.SalespersonID
GROUP BY s.Salesperson,s.PrimaryRegion ORDER BY Revenue DESC;

-- 6. Monthly seasonality
SELECT FORMAT(OrderDate,'yyyy-MM') YearMonth,SUM(RevenueINR) Revenue,
       SUM(GrossProfitINR) GrossProfit,AVG(DiscountPct) AvgDiscountPct
FROM FactSales GROUP BY FORMAT(OrderDate,'yyyy-MM') ORDER BY YearMonth;

-- 7. Channel performance
SELECT Channel,SUM(RevenueINR) Revenue,
       SUM(GrossProfitINR)/NULLIF(SUM(RevenueINR),0) GrossMarginPct,
       SUM(RevenueINR)/NULLIF(SUM(TargetRevenueINR),0) TargetAttainmentPct,
       AVG(DiscountPct) AvgDiscountPct
FROM FactSales GROUP BY Channel ORDER BY Revenue DESC;
