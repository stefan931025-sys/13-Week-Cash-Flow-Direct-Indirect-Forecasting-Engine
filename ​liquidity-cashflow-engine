import numpy as np
import pandas as pd

def generate_13_week_cash_flow(
    beginning_cash: float,
    min_cash_threshold: float,
    weeks: int = 13
):
    """
    Simulates a 13-week rolling cash flow forecast with inflows, outflows,
    net cash change, and liquidity warning flags.
    """
    np.random.seed(42)  # Seed for reproducible mock data
    
    week_list = [f"Week {i+1}" for i in range(weeks)]
    
    # Simulate recurring customer receipts (inflows) and operating disbursements (outflows)
    customer_receipts = np.random.normal(loc=450_000, scale=40_000, size=weeks)
    other_inflows = np.random.normal(loc=25_000, scale=5_000, size=weeks)
    total_inflows = customer_receipts + other_inflows
    
    payroll_outflows = np.full(weeks, 220_000) # Fixed weekly payroll mock
    vendor_payments = np.random.normal(loc=180_000, scale=20_000, size=weeks)
    debt_service = np.full(weeks, 30_000)      # Weekly loan servicing/interest
    total_outflows = payroll_outflows + vendor_payments + debt_service
    
    # Calculate cash flow trajectory
    cash_flow_data = []
    current_cash = beginning_cash
    
    for i in range(weeks):
        net_cash = total_inflows[i] - total_outflows[i]
        ending_cash = current_cash + net_cash
        deficit_flag = ending_cash < min_cash_threshold
        
        cash_flow_data.append({
            "Week": week_list[i],
            "Beginning Cash": current_cash,
            "Total Inflows": total_inflows[i],
            "Total Outflows": total_outflows[i],
            "Net Cash Flow": net_cash,
            "Ending Cash": ending_cash,
            "Below Minimum Threshold?": deficit_flag
        })
        
        current_cash = ending_cash # Roll ending cash forward
        
    df = pd.DataFrame(cash_flow_data)
    return df

# --- EXECUTION ---
if __name__ == "__main__":
    print("--- 13-WEEK LIQUIDITY & CASH FLOW FORECAST ---")
    forecast_df = generate_13_week_cash_flow(
        beginning_cash=1_200_000,
        min_cash_threshold=500_000
    )
    
    # Format currency columns for display
    pd.options.display.float_format = '${:,.2f}'.format
    print(forecast_df.to_string(index=False))
