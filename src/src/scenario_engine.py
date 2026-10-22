"""
Liquidity Stress-Testing & Scenario Engine.
Applies operational stress (e.g., collection delays, sales downturns, unexpected expenses) 
to evaluate cash runway and treasury resilience.
"""

from typing import List


class LiquidityStressTester:
    """Evaluates treasury resilience under adverse operational shocks."""

    def __init__(self, base_inflows: List[float], base_outflows: List[float]):
        self.inflows = base_inflows
        self.outflows = base_outflows

    def apply_collection_delay_shock(self, delay_penalty_pct: float = 0.20) -> List[float]:
        """Reduces weekly cash inflows due to delayed customer receivable collections."""
        shocked_inflows = [inf * (1.0 - delay_penalty_pct) for inf in self.inflows]
        return shocked_inflows

    def apply_expense_spike_shock(self, expense_spike_pct: float = 0.15) -> List[float]:
        """Increases weekly operational expense outflows unexpectedly."""
        shocked_outflows = [out * (1.0 + expense_spike_pct) for out in self.outflows]
        return shocked_outflows
