# Sharpe Ratio Demo

This **Sharpe Ratio** demo shows how to calculate the **annualized Sharpe Ratio** for a single stock (or portfolio) using **daily returns**. We fetch historical data (using [yfinance](https://pypi.org/project/yfinance/)), compute daily returns, and then annualize both returns and volatility to get the Sharpe Ratio, with math expressions rendered in **KaTeX** style.

---

## Overview

1. **Data Download**  
   - We use `yfinance` to download historical stock data (e.g. `AAPL`).
   - By default, we take the **Adjusted Close** price to handle splits/dividends.

2. **Daily Returns**  
   - Daily returns are computed via `pct_change()`.
   - We drop the first `NaN` entry to get a clean Series of returns.

3. **Risk-Free Rate Adjustment**  
   - A default annualized risk-free rate (e.g., 2%) is converted to a **daily** rate.
   - This daily risk-free rate is subtracted from daily returns to get **excess returns**.

4. **Annualized Sharpe Ratio**  

   The standard Sharpe Ratio formula is:

   $$
   \text{Sharpe Ratio} \;=\; \frac{R_p \;-\; R_f}{\sigma_p},
   $$

   where \( R_p \) is the portfolio (or asset) return, \( R_f \) is the risk-free rate, and \( \sigma_p \) is the volatility (standard deviation of returns).

   To **annualize**, we do:

   $$
   \text{Excess Return}_{\text{annual}} \;=\; \bigl(\text{Excess Return}_{\text{daily}}\bigr) 
     \times \text{trading\_days\_per\_year},
   $$

   $$
   \sigma_{\text{annual}} \;=\; \sigma_{\text{daily}} \;\times\; 
     \sqrt{\text{trading\_days\_per\_year}}.
   $$

   Hence, the **annualized Sharpe Ratio** becomes:

   $$
   \text{Sharpe Ratio}_{\text{annual}} \;=\; 
       \frac{\text{Excess Return}_{\text{annual}}}{\sigma_{\text{annual}}}.
   $$

---


