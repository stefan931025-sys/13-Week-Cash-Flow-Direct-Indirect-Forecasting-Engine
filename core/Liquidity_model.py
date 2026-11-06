import pandas as pd

class LiquidityModel:
    """
    Combines direct/indirect cash flows to maintain a rolling 13-week forecast
    and flag liquidity buffer breaches.
    """

    def __init__(self, starting_cash: float, min_cash_buffer: float = 50000.0):
        self.starting_cash = starting_cash
        self.min_cash_buffer = min_cash_buffer

    def generate_schedule(self, operating_cf: pd.Series, financing_cf: pd.Series) -> pd.DataFrame:
        """Builds 13-week liquidity waterfall and evaluates minimum balance breaches."""
        net_cf = operating_cf + financing_cf
        ending_cash = self.starting_cash + net_cf.cumsum()
        
        buffer_breach = ending_cash < self.min_cash_buffer

        return pd.DataFrame({
            'Operating_CF': operating_cf,
            'Financing_CF': financing_cf,
            'Net_Cash_Flow': net_cf,
            'Ending_Cash': ending_cash,
            'Buffer_Breach': buffer_breach
        })
