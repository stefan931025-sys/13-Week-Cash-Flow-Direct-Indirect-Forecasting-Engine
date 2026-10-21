# 13-Week Cash Flow & Liquidity Forecasting Engine

A short-term liquidity projection engine designed for trade operations, treasury management, and working capital monitoring to prevent settlement friction and cash shortfalls.

## Key Features
* Rolling Cash Flow Projections: Simulates 13-week direct and indirect cash flows incorporating recurring customer receipts and operational disbursements.
* Liquidity Warning Triggers: Automatically flags weeks where ending cash drops below predefined operational threshold reserves.
* Variance Auditing: Tracks baseline projections against simulated actual settlements to maintain clean audit trails.

## Tech Stack
* Language: Python
* Libraries: Pandas, NumPy

## Quick Start
git clone https://github.com/yourusername/liquidity-cashflow-engine.git
cd liquidity-cashflow-engine
python cashflow_forecast.py
