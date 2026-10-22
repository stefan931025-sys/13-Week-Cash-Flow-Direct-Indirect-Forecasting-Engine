"""Automated Unit Tests for 13-Week Cash Flow Forecasting Engine."""

import pytest
from src.cashflow_engine import CashFlowEngine
from src.scenario_engine import LiquidityStressTester


@pytest.fixture
def sample_cash_flows():
    inflows = [100.0] * 13
    outflows = [80.0] * 13
    return inflows, outflows


def test_cash_flow_length_validation():
    """Ensures incomplete weekly data arrays raise ValueError."""
    with pytest.raises(ValueError):
        CashFlowEngine(
            starting_cash=1000.0,
            weekly_inflows=[100.0] * 10,  # Invalid length
            weekly_outflows=[80.0] * 13,
        )


def test_ending_cash_calculation(sample_cash_flows):
    inflows, outflows = sample_cash_flows
    engine = CashFlowEngine(
        starting_cash=500.0,
        weekly_inflows=inflows,
        weekly_outflows=outflows,
        min_cash_threshold=100.0,
    )
    df = engine.generate_13_week_forecast()

    # Week 1: 500 + (100 - 80) = 520
    assert df.loc[0, "Ending_Cash"] == 520.0
    assert df.loc[0, "Liquidity_Breach"] is False


def test_stress_tester_shocks(sample_cash_flows):
    inflows, outflows = sample_cash_flows
    tester = LiquidityStressTester(inflows, outflows)
    shocked_in = tester.apply_collection_delay_shock(0.50)
    
    assert shocked_in[0] == 50.0
