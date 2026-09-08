# Business Requirements Document — Executive Sales Analytics

## Business Context
A multi-region consumer-products company relies on fragmented regional reporting. Leadership lacks one trusted view of revenue, margin, target attainment, product performance, regional trends, channel performance and sales-team effectiveness.

## Objective
Design a governed executive analytics solution covering 24 months of synthetic sales activity using a Power BI star schema and decision-oriented report pages.

## Stakeholders
CEO / Managing Director; Sales Director; Finance Director; Regional Managers; Category Managers; Sales Managers; BI/Data Analyst.

## Core Business Questions
1. Are we meeting revenue and profitability targets?
2. Which regions and countries are driving growth or decline?
3. Which categories/SKUs create revenue but weak margin?
4. Which channels are underperforming?
5. Which salespeople consistently outperform targets?
6. Where are discounting and seasonality affecting profitability?

## Functional Requirements
- FR-01 Consolidate 24 months of sales transactions.
- FR-02 Provide executive KPI cards and time trends.
- FR-03 Filter by time, region, country, product category, channel and salesperson.
- FR-04 Calculate YoY growth and target attainment.
- FR-05 Rank products and salespeople.
- FR-06 Highlight margin leakage and target gaps.
- FR-07 Support drill-down and drill-through.
- FR-08 Allow summarized data export where permitted.

## Non-Functional Requirements
- NFR-01 Use a star schema.
- NFR-02 Define business measures centrally in DAX.
- NFR-03 Use only synthetic public-safe data.
- NFR-04 Maintain readable, accessible report design.
- NFR-05 Keep the model lightweight enough for a normal portfolio laptop.

## Acceptance Criteria
- SQL KPI checks reconcile to Power BI.
- Filters cross-filter visuals consistently.
- 2025 YoY compares correctly to 2024.
- Target Attainment % = Revenue / Target Revenue.
- Product margin and salesperson rankings respond to filters.
- Every public-facing asset clearly identifies the dataset as synthetic.
