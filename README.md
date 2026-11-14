# 13-Week Cash Flow & Liquidity Forecasting Engine

![CI Workflow](https://github.com/stefan931025-sys/13-Week-Cash-Flow-Direct-Indirect-Forecasting-Engine/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A short-term treasury liquidity projection engine designed for trade operations, cash management, and working capital monitoring to prevent settlement friction and funding shortfalls[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span).

## 🚀 Core Features

* **Rolling Cash Flow Projections:** Simulates 13-week direct and indirect cash flows incorporating recurring customer receipts, vendor disbursements, payroll, and debt service obligations[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span).
* **Liquidity Warning Triggers:** Automatically flags weeks where ending cash balances drop below predefined operational threshold reserves[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span).
* **Variance & Scenario Auditing:** Tracks baseline projections against simulated actual settlements to maintain clean audit trails and stress-test cash conversion cycles[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span).

---

## 📊 Treasury & Liquidity Mathematics

### 1. Direct & Indirect Cash Flow Roll-Forward

$$\text{Ending Cash}_t = \text{Beginning Cash}_t + \text{Operating Receipts}_t - \text{Cash Disbursements}_t + \text{Financing Net}_t$$

### 2. Working Capital Burn Rate & Runway

$$\text{Runway (Weeks)} = \frac{\text{Current Liquid Reserves}}{\text{Average Weekly Net Cash Burn}}$$

---

## 📁 Repository Structure

```text
13-Week-Cash-Flow-Direct-Indirect-Forecasting-Engine/
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions automated test workflow
├── core/
│   └── scenario_engine.py # Cash flow simulation & scenario modules
├── tests/
│   └── test_cashflow.py   # Automated pytest suite
├── main.py                # Main execution pipeline script
├── repo_auditor.py        # Static AST analysis governance tool
├── requirements.txt       # Python dependencies
└── README.md              # System documentation
