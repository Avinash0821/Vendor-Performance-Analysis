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
│   └── data_extraction.sql       # Raw data queries and joins
│
├── Python/
│   ├── vendor_analysis.ipynb     # EDA, outlier handling, KPIs in Python
│   └── preprocessing.py          # Data cleaning and transformation
│
├── PowerBI/
│   └── vendor_dashboard.pbix     # Interactive dashboard with filters and KPIs
│
├── images/
│   └── dashboard_screenshot.png  # Dashboard preview
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

![Dashboard Screenshot](images/dashboard_screenshot.png)

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

* `OnTimeDeliveryRate = DIVIDE(OnTimeDeliveries, TotalDeliveries)`
* `DefectRate = DIVIDE(DefectiveItems, TotalItemsReceived)`
* `VendorRating = AVERAGE(VendorScore)`
* `AverageLeadTime = AVERAGEX(Deliveries, DeliveryDate - OrderDate)`

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


