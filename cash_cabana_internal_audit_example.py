# =================================================
# Cash Cabana Bank Audit Code Example
# =================================================
# Internal Audit Example: Self-Documenting vs Traditonal Code
# -------------------------------------------------
# Traditional Logic Showing Unclear Calculation
# -------------------------------------------------
def calc (a, b, c):
  
  return (a - b) / c # ratio
  
# -------------------------------------------------
# Self-Documenting Internal Audit Ready Calculation
# -------------------------------------------------
def calculate_cash_cabana_liquidity_ratio(total_liquid_assets, short_term_liabilities, adjustment_factor):
    """
    Calculates the liquidity ratio for Cash Cabana Bank.
    
    Liquidity Ration = (Total Liquid Assets - Adjustments) / Short-Term Liabilities
    This function is designed for internal audit clarity and regulatory validation.
    """
    adjusted_assets = total_liquid_assets - adjustment_factor
    liquidity_ratio = adjusted_assets / short_term_liabilities
    return liquidity_ratio

print(calculate_cash_cabana_liquidity_ratio(100000, 50000, 5000))                                          
                                          
