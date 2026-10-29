import pytest
import numpy as np
from cashflow_engine import CashFlowEngine


@pytest.fixture
def sample_cash_flows():
    inflows = [100.0] * 13
    outflows = [80.0] * 13
    return inflows, outflows


def test_ending_cash_calculation(sample_cash_flows):
    inflows, outflows = sample_cash_flows
    engine = CashFlowEngine(
        starting_cash=500.0,
        weekly_inflows=inflows,
        weekly_outflows=outflows,
        min_cash_threshold=-100.0
    )
    df = engine.generate_13_week_forecast()

    # Week 1: 500 + (100 - 80) = 520
    assert df.loc[0, 'Ending_Cash'] == 520.0

    # Ensure native boolean evaluation for NumPy types
    assert not df.loc[0, 'Liquidity_Breach']
