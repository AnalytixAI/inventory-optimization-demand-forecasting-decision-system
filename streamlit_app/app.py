import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from inventory_logic import load_inventory_decisions

st.set_page_config(
    page_title="Inventory Optimization Decision System",
    layout="wide"
)

# -------------------------
# Title & Introduction
# -------------------------
st.title("📦 Inventory Optimization & Demand Forecasting")
st.write(
    "This application demonstrates how forecasting and inventory optimization "
    "outputs can be converted into a decision-support tool for managers."
)

# -------------------------
# Load Data
# -------------------------
try:
    forecast_df = pd.read_csv("forecasted_demand_(NoteBook2).csv")
    inventory_df = pd.read_csv("inventory_decision_output_(NoteBook3).csv")
except FileNotFoundError:
    st.error("Required CSV files not found. Please place them in the app folder.")
    st.stop()

# -------------------------
# Forecast Visualization
# -------------------------
st.subheader("📈 Forecasted Demand")

forecast_df['Month'] = pd.to_datetime(forecast_df['Month'])

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(
    forecast_df['Month'],
    forecast_df['Forecasted_Demand'],
    marker='o',
    linestyle='-'
)
ax.set_xlabel("Month")
ax.set_ylabel("Forecasted Demand")
ax.set_title("Forecasted Monthly Demand")

st.pyplot(fig)

# -------------------------
# Inventory Decisions
# -------------------------
st.subheader("📊 Inventory Recommendations")

inventory_metrics = load_inventory_decisions(inventory_df)

col1, col2, col3 = st.columns(3)

col1.metric("Economic Order Quantity (EOQ)", round(inventory_metrics["EOQ"], 2))
col2.metric("Safety Stock", round(inventory_metrics["Safety_Stock"], 2))
col3.metric("Reorder Point (ROP)", round(inventory_metrics["Reorder_Point"], 2))

# -------------------------
# Managerial Insights
# -------------------------
st.subheader("🧠 Managerial Insights")

st.write("""
- Forecast-driven inventory planning improves service levels and reduces uncertainty.
- EOQ balances ordering and holding costs effectively.
- Safety stock ensures demand variability is managed at a 95% service level.
- Reorder Point enables timely replenishment and prevents stockouts.
""")

st.info(
    "Note: This Streamlit app is a deployment demonstration. "
    "Power BI is used as the primary managerial dashboard."
)