import numpy as np
import pandas as pd

class IndirectCashFlowEngine:
    """
    Computes 13-week projected cash flows via the indirect method:
    Adjusting Net Income for non-cash expenses and working capital deltas.
    """

    def __init__(self, net_income: pd.Series, working_capital_deltas: pd.DataFrame):
        """
        :param net_income: 13-week projected Net Income series (13,)
        :param working_capital_deltas: DataFrame with columns ['delta_ar', 'delta_ap', 'delta_inv', 'depreciation']
        """
        self.net_income = net_income
        self.wc_deltas = working_capital_deltas

    def compute_operating_cash_flow(self) -> pd.Series:
        """Sums net income with non-cash items and working capital changes."""
        # Cash inflows: increase in AP (+), decreases in AR/Inventory (+)
        # Non-cash expenses: Depreciation (+)
        total_adjustments = (
            self.wc_deltas['depreciation'] 
            - self.wc_deltas['delta_ar'] 
            + self.wc_deltas['delta_ap'] 
            - self.wc_deltas['delta_inv']
        )
        return self.net_income + total_adjustments
