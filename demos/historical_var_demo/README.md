# Value at Risk (VaR) - Historical Simulation in Python

This repository demonstrates a **Historical Simulation** approach to calculate **Value at Risk (VaR)** for a given stock (or portfolio). We use [yfinance](https://github.com/ranaroussi/yfinance) to download historical data, compute daily returns, and then estimate VaR at a specified confidence level.

## How It Works

1. **Download Historical Data**
   By default, we fetch data for a chosen stock ticker (e.g., AAPL) from Yahoo Finance for a particular date range.

2. **Compute Daily Returns**
   We calculate daily percentage returns based on adjusted closing prices:
   \[
     R_t = \frac{P_t - P_{t-1}}{P_{t-1}}
   \]

3. **Historical Simulation Method**
   - Sort the daily returns in ascending order (worst to best).
   - Identify the cutoff for the chosen confidence level \(\alpha\).
   - The VaR is the (1-\(\alpha\)) quantile of the distribution of returns, interpreted as a potential loss (thus taken as a positive value when returns are negative).


