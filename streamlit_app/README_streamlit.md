# Streamlit Decision Support App

## Overview
This Streamlit application demonstrates how demand forecasting and inventory
optimization outputs can be deployed as an interactive decision-support tool.

## Purpose
- Visualize forecasted demand
- Display inventory recommendations (EOQ, Safety Stock, ROP)
- Provide managerial interpretation of analytics outputs

## How This Fits the Project
- Power BI is used for structured managerial dashboards
- Streamlit is used as a lightweight deployment and technical demonstration

## How to Run
1. Navigate to the streamlit_app folder
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
   streamlit run app.py

## Required Files
Ensure the following files are present in the same directory:
- forecast_output.csv
- inventory_decisions.csv
