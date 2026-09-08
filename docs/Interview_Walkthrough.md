# 90-Second Interview Walkthrough

> “I built an Executive Sales Analytics solution using a fully synthetic 55,000-row, 24-month sales dataset. I started with the business requirement: leadership needed one view of revenue, margin, growth, target attainment, regional contribution, product performance and sales-team effectiveness.
>
> I designed a star schema with FactSales and six dimensions, created SQL validation queries, prepared Power Query transformations, and centralized the business logic in DAX. The dashboard is designed as four pages: Executive Overview, Regional & Product Performance, Sales Team Performance, and Trends & Drivers.
>
> I deliberately engineered realistic patterns into the synthetic data, including Q4 seasonality, regional performance differences, channel discount behavior and low-margin products. That lets the dashboard demonstrate actual analytical thinking rather than random charts. I then translate those findings into recommendations around target gaps, margin leakage, channel performance and seasonality.”

## Interview Follow-ups to Prepare For
- Why did you choose a star schema rather than a flat table?
- How did you validate Power BI KPIs against SQL?
- Why are measures preferred over calculated columns for these KPIs?
- How would you implement row-level security by region?
- What would you change if the model grew from 55K to 500M rows?
- How would you move this solution to Microsoft Fabric or Snowflake?
