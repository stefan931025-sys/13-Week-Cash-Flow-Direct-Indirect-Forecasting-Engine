# 13-Week Cash Flow & Liquidity Forecasting Engine

[![Liquidity Cash Flow CI](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/stefan931025-sys/13-Week-Cash-Flow-Direct-Indirect-Forecasting-Engine)
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A short-term treasury liquidity projection engine designed for trade operations, cash management, and working capital monitoring to prevent settlement friction and funding shortfalls.

---

## Core Features

* **Rolling Cash Flow Projections:** Simulates 13-week direct and indirect cash flows incorporating recurring customer receipts, vendor disbursements, payroll, and debt service obligations.
* **Liquidity Warning Triggers:** Automatically flags weeks where ending cash balances drop below predefined operational threshold reserves.
* **Variance & Scenario Auditing:** Tracks baseline projections against simulated actual settlements to maintain clean audit trails and stress-test cash conversion cycles.

---

## Treasury & Liquidity Mathematics

### 1. Direct & Indirect Cash Flow Roll-Forward
$$\text{Ending Cash}_t = \text{Beginning Cash}_t + \text{Operating Receipts}_t - \text{Cash Disbursements}_t + \text{Financing Net Flows}_t$$

### 2. Working Capital Burn Rate & Runway
$$\text{Runway (Weeks)} = \frac{\text{Current Liquid Reserves}}{\text{Average Weekly Net Cash Burn}}$$

---

## System Architecture & Data Flow

