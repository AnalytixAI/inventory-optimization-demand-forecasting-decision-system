# 📦 Inventory Optimization & Demand Forecasting Decision System

### A Data-Driven Predictive & Prescriptive Analytics Framework for Retail Inventory Management

---

## 🔹 Project Overview

Retail and distribution organizations constantly face a dual operational risk:

* **Overstocking** → Excess holding cost, capital blockage, and product obsolescence
* **Stockouts** → Lost sales, poor service levels, and customer churn

Traditional inventory planning relies heavily on historical averages and managerial intuition. These approaches fail under demand volatility, seasonality, lead-time uncertainty, and increasing customer service expectations.

This project develops a **structured decision optimization system** integrating:

* 📈 Predictive Analytics (Demand Forecasting)
* 📊 Prescriptive Analytics (Inventory Optimization)
* 📉 Service-Level Scenario Analysis
* 📊 Power BI Decision Dashboard
* 🚀 Streamlit Deployment Application

The objective is to convert forecasts into **actionable inventory policies** aligned with measurable business KPIs.

---

## 🏗 Project Architecture (4-Layer Framework)

### 🔹 Layer 1 — Business Context & KPI Foundation

* Defined inventory risk trade-offs
* Established measurable KPIs:

  * Forecast Accuracy (MAPE / RMSE)
  * Service Level (%)
  * Holding Cost vs Stockout Cost
  * Inventory Turnover
  * Stockout Risk Indicator

This layer anchors all downstream analytical decisions.

---

### 🔹 Layer 2 — Demand Forecasting (Predictive Analytics)

* Monthly aggregation of Global Superstore dataset
* SKU consolidation into `ALL_SKUS`
* Time-series decomposition:

  * Trend
  * Seasonality
  * Residual component
* Forecasting Models:

  * Baseline (Naïve / Moving Average)
  * ARIMA (Selected model)
* Evaluation Metrics:

  * Mean Absolute Percentage Error (MAPE)
  * Root Mean Squared Error (RMSE)

**Output:** Forecasted future demand feeding the inventory optimization layer.

---

### 🔹 Layer 3 — Inventory Optimization (Prescriptive Analytics)

Inventory decisions are derived directly from forecast outputs.

Applied models:

* **Economic Order Quantity (EOQ)**
  [ EOQ = √(2DS / H) ]

* **Safety Stock**
  Buffer against demand variability and service-level uncertainty.

* **Reorder Point (ROP)**
  [ ROP = (Demand × Lead Time) + Safety Stock ]

Service-level scenarios evaluated:

| Service Level | Risk Exposure | Cost Impact |
| ------------- | ------------- | ----------- |
| 90%           | Moderate      | Lowest      |
| 95%           | Low           | Balanced    |
| 99%           | Very Low      | Highest     |

This layer converts predictive insights into operational inventory policies.

---

### 🔹 Layer 4 — Decision Dashboard & Deployment

#### 📊 Power BI Dashboard

Includes:

* Forecasted demand trend (future periods)
* Safety Stock by service level
* Reorder Point comparison
* Incremental cost analysis
* Stockout risk classification
* Inventory policy summary table

Power BI serves as the **primary managerial decision interface**.

#### 🚀 Streamlit Application

Demonstrates deployment of:

* Forecast visualization
* EOQ, Safety Stock, and ROP metrics
* Structured managerial insight summary

---

## 🎯 Final Managerial Recommendation

At a **95% service level**, the system achieves an optimal balance between inventory holding cost and stockout risk.

Increasing service level to 99% further reduces stockout probability but significantly increases safety stock and incremental cost, resulting in diminishing marginal benefit.

> Therefore, a **95% service level is operationally efficient and cost-optimal** under current demand volatility assumptions.

---

## 🛠 Technologies Used

* Python
* Pandas
* Statsmodels (ARIMA)
* Matplotlib
* Power BI
* Streamlit

---

## 📂 Repository Structure

```
notebooks/              → Predictive & prescriptive modeling
notebook_outputs/       → Model output CSV files
data/                   → Cleaned datasets
streamlit_app/          → Deployment application
dashboards/             → Power BI dashboard
reports/                → Structured project report
images/                 → Dashboard & deployment screenshots
```

---

## 🚀 Business Impact

This decision system enables:

* Reduced overstocking
* Controlled stockout risk
* Improved capital efficiency
* Structured service-level optimization
* KPI-driven inventory policy design

---

## 🔮 Future Enhancements

* Multi-SKU segmentation
* Multi-echelon inventory modeling
* Real-time demand integration
* Dynamic service-level optimization
* Automated model retraining pipeline

---

## 👤 Author
AnalytixAI
