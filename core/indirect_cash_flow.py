import numpy as np
import pandas as pd

class IndirectCashFlowEngine:
    """
    Computes 13-week projected cash flows using the indirect method:
    Starting from Net Income, adjusting for non-cash items and working capital deltas.
    """

    def __init__(self, net_income_forecast: pd.Series, adjustments: pd.DataFrame):
        self.net_income = net_income_forecast
        self.adjustments = adjustments  # e.g., Depreciation, D&A, Change in AR, AP, Inventory

    def compute_operating_cash_flow(self) -> pd.Series:
        """Sums net income with all non-cash and working capital adjustments."""
        total_adjustments = self.adjustments.sum(axis=1)
        ocf = self.net_income + total_adjustments
        return ocf

    def project_13_week_liquidity(self, opening_cash: float, financing_flows: pd.Series) -> pd.DataFrame:
        """Builds the rolling 13-week cash balance forecast."""
        ocf = self.compute_operating_cash_flow()
        net_cash_flow = ocf + financing_flows
        
        cash_balance = opening_cash + net_cash_flow.cumsum()
        
        forecast_df = pd.DataFrame({
            'Net_Income': self.net_income,
            'Operating_Cash_Flow': ocf,
            'Financing_Flows': financing_flows,
            'Net_Cash_Change': net_cash_flow,
            'Ending_Cash_Balance': cash_balance
        })
        return forecast_df
