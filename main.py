from src.cashflow_engine import CashFlowEngine
from src.scenario_engine import LiquidityStressTester

if __name__ == "__main__":
    print("--- INITIATING 13-WEEK LIQUIDITY & CASH FLOW ENGINE ---")

    # Baseline weekly treasury projections ($ Millions)
    starting_cash = 18_000_000.0
    weekly_inflows = [4.5, 4.2, 5.0, 3.8, 4.1, 4.6, 4.9, 3.5, 4.0, 4.2, 4.8, 5.1, 4.3]
    weekly_outflows = [3.9, 4.0, 4.2, 4.1, 3.8, 4.5, 4.3, 4.0, 3.9, 4.2, 4.1, 4.0, 4.4]

    # 1. Run Base Case 13-Week Forecast
    treasury_engine = CashFlowEngine(
        starting_cash=starting_cash,
        weekly_inflows=weekly_inflows,
        weekly_outflows=weekly_outflows,
        min_cash_threshold=12_000_000.0,  # $12M minimum liquidity covenant
    )

    base_forecast_df = treasury_engine.generate_13_week_forecast()
    print("\n[Base Case 13-Week Liquidity Schedule Preview (First 4 Weeks)]")
    print(base_forecast_df[["Week", "Beginning_Cash", "Net_Cash_Flow", "Ending_Cash", "Liquidity_Breach"]].head(4))

    # 2. Run Stress Scenario (25% Collection Delay & 15% Cost Spike)
    stress_tester = LiquidityStressTester(weekly_inflows, weekly_outflows)
    shocked_inflows = stress_tester.apply_collection_delay_shock(0.25)
    shocked_outflows = stress_tester.apply_expense_spike_shock(0.15)

    stressed_engine = CashFlowEngine(
        starting_cash=starting_cash,
        weekly_inflows=shocked_inflows,
        weekly_outflows=shocked_outflows,
        min_cash_threshold=12_000_000.0,
    )

    stressed_df = stressed_engine.generate_13_week_forecast()
    breach_weeks = stressed_df[stressed_df["Liquidity_Breach"] == True]

    print(f"\n[Stress Test Results]")
    print(f"Total Weeks Flagged for Liquidity Covenant Breach: {len(breach_weeks)}")
    if not breach_weeks.empty:
        print(breach_weeks[["Week", "Ending_Cash", "Liquidity_Breach"]])
