# Market Risk Monitor Dashboard

## Overview
This project analyzes macroeconomic indicators and equity market performance to monitor periods of increased market risk and financial stress.

The goal is to demonstrate an end-to-end analytics workflow:
data ingestion → aggregation → risk metrics → visualization → insights.

The dashboard focuses on how inflation, unemployment, and interest rate policy interact with equity markets over time.

---

## Tools & Technologies
- Python (ETL, data ingestion)
- PostgreSQL (analytical tables and views)
- SQL (schema design, aggregations)
- Docker & Docker Compose
- Power BI
- FRED (Federal Reserve Economic Data) API

---

## Key Analyses
- S&P 500 index performance over time
- Market stress and caution thresholds based on drawdown levels
- Inflation (CPI) trends and monetary tightening
- Unemployment rate dynamics
- Federal Funds Rate and 10Y Treasury Yield behavior
- Historical event overlays (2008 Financial Crisis, 2020 COVID shock)

---

## Key Insights
- Rising inflation combined with tightening monetary policy has historically preceded periods of increased market volatility.
- Elevated interest rates often coincide with slower equity market growth and higher downside risk.
- Unemployment spikes tend to align with major economic shocks and equity drawdowns.

---

## Dashboard Preview
https://github.com/dvnguyin/Market-Risk-Monitor/blob/main/dashboard/screenshots/Market%20Risk%20Monitor%20Dashboard.png

---

## How to Run
1. Create a `.env` file using `.env.example` and add your FRED API key
2. Start PostgreSQL using Docker:
   ```bash
   docker compose up -d

