# 📊 Vendor Performance Analysis

This project is a complete end-to-end analysis of vendor performance using a combination of **SQL**, **Python**, and **Power BI**. It demonstrates how data engineering, analysis, and visualization tools work together to derive actionable insights for improving vendor relationships and optimizing procurement processes.

---

## 🚀 Project Overview

The goal of this project is to evaluate vendor performance based on key metrics such as delivery timelines, defect rates, costs, and overall reliability. The analysis helps stakeholders make data-driven decisions regarding vendor selection, negotiations, and performance improvement initiatives.

---

## 🔧 Tools & Technologies Used

* **SQL Server (SSMS / Visual Studio)** – Data extraction, transformation, and loading (ETL)
* **Python** – Data cleaning, exploratory data analysis (EDA), and preprocessing
* **Power BI** – Dashboard development and interactive visualizations
* **DAX** – Advanced calculations and performance metrics in Power BI

---

## 📁 Project Structure

```
Vendor-Performance-Analysis/
│
├── SQL/
│   └── ingestion_db.py
        exloratory_data_analysis.ipynb       # EDA, outlier handling, KPIs in Python, Data cleaning and transformation
│
├── Python/
│   ├── Vendor Performance Analysis.ipynb    # Raw data queries and joins 
│   └── preprocessing.py                     
│
├── PowerBI/
│   └── Vendor Performance Visualization.pbix     # Interactive dashboard with filters and KPIs
│
│
└── README.md                     # Project documentation
```

---

## 📌 Key Metrics Analyzed

* **On-time Delivery Rate**
* **Defect Rate / Quality Score**
* **Average Lead Time**
* **Cost per Unit**
* **Vendor Scorecard (Overall Rating)**

---

## 📊 Dashboard Highlights (Power BI)

* Vendor comparison using bar and line charts
* Filter by date range, product category, or region
* Dynamic KPIs for trend tracking
* Drill-through reports for vendor-specific performance

![Dashboard Screenshot](<img width="1407" height="790" alt="image" src="https://github.com/user-attachments/assets/edd24550-9de0-41d8-923a-3cbccc59f0f2" />)

---

## 🧪 SQL and Python Insights

* Joined multiple normalized tables to consolidate vendor, product, delivery, and inspection data
* Performed EDA to detect:

  * Late deliveries
  * High defect suppliers
  * Cost inconsistencies
* Created summary tables for Power BI using Python and SQL views

---

## 📈 DAX Measures in Power BI

* `BrandPerformance = SUMMARIZE(vendor_sale_summary,vendor_sale_summary[Description],"TotalSales", SUM(vendor_sale_summary[TotalSalesDollars]),"AvgProfitMargin", AVERAGE(vendor_sale_summary[ProfitMargin]))`
* `TargetBrand = IF([TotalSales] <= PERCENTILEX.INC(BrandPerformance, BrandPerformance[TotalSales], 0.15) && [AvgProfitMargin] >= PERCENTILEX.INC(BrandPerformance, BrandPerformance[AvgProfitMargin], 0.85),"Yes","No")`
* `LowTurnoverVendor = VAR FilterData = FILTER(vendor_sale_summary, vendor_sale_summary[StockTurnover] < 1)   RETURN SUMMARIZE(FilterData,vendor_sale_summary[VendorName], "avgStockTurnOver", AVERAGE(vendor_sale_summary[StockTurnover]))`
* `PurchaseCountribution = SUMMARIZE(vendor_sale_summary, vendor_sale_summary[VendorName], "TotalPurchaseDollars",SUM(vendor_sale_summary[TotalPurchaseDollars]))`
* `PurchaseContribution% = ROUND(PurchaseCountribution[TotalPurchaseDollars]/SUM(PurchaseCountribution[TotalPurchaseDollars])*100,2)`

---

## 📬 Insights & Recommendations

* Identify underperforming vendors and initiate improvement plans
* Reward high-performing vendors with preferred supplier status
* Negotiate better terms with consistent vendors based on historical data
* Reduce overall procurement risks through data-driven decisions

---

## 📦 Future Improvements

* Integrate machine learning for vendor score prediction
* Schedule data refreshes using Power BI Service
* Automate alerts for delivery or quality breaches

---

## 🧠 Learnings

* Practical integration of SQL, Python, and BI tools in real-world analysis
* Hands-on experience with ETL, DAX, and performance visualization
* Translating data into strategic procurement decisions


