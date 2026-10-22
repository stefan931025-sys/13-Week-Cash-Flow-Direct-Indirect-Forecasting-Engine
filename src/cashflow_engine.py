"""
13-Week Rolling Cash Flow & Liquidity Forecasting Engine.
Models operational direct cash flows, accounts receivable collections, 
accounts payable disbursements, and flags minimum liquidity covenant breaches.
"""

from typing import List
import pandas as pd


class CashFlowEngine:
    """Institutional Treasury & Working Capital Liquidity Model."""

    def __init__(
        self,
        starting_cash: float,
        weekly_inflows: List[float],
        weekly_outflows: List[float],
        min_cash_threshold: float = 10_000_000.0,
    ):
        self.starting_cash = starting_cash
        self.inflows = weekly_inflows
        self.outflows = weekly_outflows
        self.threshold = min_cash_threshold

        if len(self.inflows) != 13 or len(self.outflows) != 13:
            raise ValueError("Inflows and outflows vectors must span exactly 13 weeks.")

    def generate_13_week_forecast(self) -> pd.DataFrame:
        """Generates a rolling 13-week cash position schedule with breach flags."""
        schedule = []
        current_cash = self.starting_cash

        for week in range(1, 14):
            inflow = self.inflows[week - 1]
            outflow = self.outflows[week - 1]
            net_flow = inflow - outflow
            ending_cash = current_cash + net_flow

            breach_flag = ending_cash < self.threshold

            schedule.append(
                {
                    "Week": f"Week {week}",
                    "Beginning_Cash": round(current_cash, 2),
                    "Cash_Inflows": round(inflow, 2),
                    "Cash_Outflows": round(outflow, 2),
                    "Net_Cash_Flow": round(net_flow, 2),
                    "Ending_Cash": round(ending_cash, 2),
                    "Liquidity_Breach": bool(breach_flag),
                }
            )
            current_cash = ending_cash

        return pd.DataFrame(schedule)
