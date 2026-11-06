import pandas as pd
import numpy as np
from core.indirect_cash_flow import IndirectCashFlowEngine
from core.liquidity_model import LiquidityModel

def run_pipeline():
    weeks = [f"Week_{i+1}" for i in range(13)]
    
    # Mock 13-week net income project stream
    net_income = pd.Series(np.linspace(15000, 25000, 13), index=weeks)
    
    wc_deltas = pd.DataFrame({
        'depreciation': 2000,
        'delta_ar': np.random.normal(1000, 500, 13),
        'delta_ap': np.random.normal(800, 300, 13),
        'delta_inv': np.random.normal(500, 200, 13)
    }, index=weeks)

    engine = IndirectCashFlowEngine(net_income, wc_deltas)
    operating_cf = engine.compute_operating_cash_flow()

    financing_cf = pd.Series(0.0, index=weeks)
    
    liquidity = LiquidityModel(starting_cash=100000.0, min_cash_buffer=60000.0)
    schedule = liquidity.generate_schedule(operating_cf, financing_cf)

    print("--- 13-Week Rolling Cash Flow Forecast ---")
    print(schedule.round(2))

if __name__ == "__main__":
    run_pipeline()
