# E-Commerce Return Logistics Performance and Cost Optimization

### End-to-End Data Analytics Project | Python • MySQL • Power BI

## Project Overview

This project analyzes e-commerce orders and product returns to identify return patterns, investigate logistics-related cost indicators, and develop data-driven recommendations for improving operational efficiency.

The analysis follows an end-to-end workflow involving data preparation, exploratory data analysis, SQL-based business analysis, and interactive dashboard development.

**Project Type:** Data Analytics and Business Intelligence  
**Industry:** E-Commerce and Logistics  
**Dataset:** 34,500 synthetic e-commerce orders  
**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, MySQL, Power BI

## Business Problem

Product returns create operational challenges for e-commerce businesses, including additional shipping activities, inventory handling, and potential profitability impacts.

The project investigates the following business questions:

- What proportion of customer orders are returned?
- Which product categories show higher return volumes or rates?
- How do returns vary across customer and order characteristics?
- What patterns can be identified in recorded shipping costs?
- How can dashboards help business teams monitor return performance?

## Project Objectives

1. Clean and prepare the e-commerce dataset for analysis.
2. Calculate key order and return performance indicators.
3. Identify return patterns across product categories and other available dimensions.
4. Analyze recorded shipping costs and their relationship with return activity.
5. Build an interactive Power BI dashboard.
6. Develop actionable recommendations based on the observed findings.

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Data cleaning and exploratory data analysis |
| Pandas and NumPy | Data manipulation and numerical analysis |
| Matplotlib and Seaborn | Data visualization |
| MySQL | SQL-based analysis and business queries |
| Power BI | Interactive dashboard and KPI reporting |
| GitHub | Project documentation and portfolio presentation |

## Dataset Overview

The project uses a synthetic e-commerce dataset containing **34,500 orders**.

The dataset supports analysis of order activity, product returns, customer and product characteristics, and recorded shipping costs.

**Important:** The dataset is synthetic. Recorded shipping costs should not be interpreted as actual reverse-logistics expenses without additional supporting data and cost assumptions.

## Key Performance Indicators

| KPI | Result |
|---|---|
| Total Orders | 34,500 |
| Returned Orders | 1,903 |
| Overall Return Rate | 5.52% |

Return Rate = (Returned Orders / Total Orders) × 100

## Key Findings

### Overall Return Performance

Of the 34,500 orders analyzed, 1,903 were returned, representing an overall return rate of approximately **5.52%**.

### Product Category Analysis

The Fashion category was identified as a key area of interest in the return analysis.

Category-level findings can help businesses prioritize investigations into product information, sizing guidance, fulfillment accuracy, and customer expectations.

### Shipping Cost Analysis

Recorded shipping costs were examined to understand patterns across orders and return-related segments.

Because the dataset does not establish the complete cost of reverse logistics, these results are treated as shipping-cost indicators rather than verified return-processing costs.

## Power BI Dashboard

An interactive Power BI dashboard was developed to support the exploration of e-commerce return performance.

The dashboard provides a visual overview of important KPIs and analytical patterns to help stakeholders monitor performance and identify areas requiring attention.

**Power BI File:** `e-commerce_return_logistics_Dashboard.pbix`

To explore the dashboard, download the PBIX file and open it using Power BI Desktop.

## Business Recommendations

Based on the exploratory analysis, the following actions are proposed for further evaluation:

- **Improve product information:** Review descriptions, images, and sizing information for categories with elevated returns.
- **Monitor return performance:** Track return rates by product category and other relevant dimensions.
- **Investigate return drivers:** Combine transactional data with return reasons and customer feedback when available.
- **Improve operational visibility:** Use Power BI reporting to monitor KPIs and investigate emerging patterns.
- **Strengthen cost measurement:** Collect actual reverse-shipping, inspection, handling, and restocking costs to evaluate the financial impact of returns more accurately.

These recommendations are analytical proposals and have not been validated through operational experiments.

## Project Workflow

**Data Collection → Data Cleaning → Exploratory Data Analysis → SQL Analysis → Power BI Dashboard → Business Insights and Recommendations**

## Project Files

| File | Description |
|---|---|
| `E-commerce py.py` | Python analysis script |
| `e-commerce.py` | Python analysis script |
| `ecommerce_return_analysis.sql` | MySQL analysis queries |
| `e-commerce_return_logistics_Dashboard.pbix` | Interactive Power BI dashboard |
| `Ecommerce_Project_Report.pdf` | Detailed project report |
| `Ecommerce_Return_Logistics_Presentation.pptx` | Project presentation |
| `Kaggle_Ecommerce Data.csv` | Dataset used in the project |

## Limitations

- The analysis uses synthetic rather than real business transactions.
- Observed relationships do not establish causation.
- Recorded shipping costs do not represent the complete cost of reverse logistics.
- Proposed recommendations require further validation before implementation.

## Conclusion

This project demonstrates an end-to-end data analytics approach to understanding e-commerce returns and operational performance.

By combining Python, MySQL, and Power BI, the project translates transactional data into interpretable KPIs, visual analysis, and business-focused recommendations.

It showcases practical skills in data preparation, exploratory analysis, SQL, dashboard development, and analytical communication.
