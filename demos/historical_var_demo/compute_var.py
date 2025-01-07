#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
compute_var.py

Example: Calculate Value at Risk (VaR) using the Historical Simulation method.
"""

import pandas as pd
import numpy as np
import yfinance as yf  # For downloading stock data (optional)

def download_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Downloads historical stock data from Yahoo Finance and returns a pandas DataFrame.
    :param ticker: Stock ticker, e.g. 'AAPL' for Apple Inc.
    :param start_date: Start date in 'YYYY-MM-DD' format.
    :param end_date: End date in 'YYYY-MM-DD' format.
    :return: A DataFrame containing date and adjusted closing price.
    """
    df = yf.download(ticker, start=start_date, end=end_date)
    if 'Adj Close' in df.columns:
        # Use adjusted close for returns calculation
        df = df[['Adj Close']]
        df.rename(columns={'Adj Close': 'Close'}, inplace=True)
    else:
        # Fallback to 'Close' if 'Adj Close' is not available
        df = df[['Close']]
    return df


def calculate_daily_returns(df: pd.DataFrame) -> pd.Series:
    """
    Computes daily returns for a stock.
    :param df: A DataFrame containing the 'Close' column.
    :return: A pandas Series indexed by date with daily returns.
    """
    df['Return'] = df['Close'].pct_change()
    returns = df['Return'].dropna()
    return returns


def historical_simulation_var(returns: pd.Series, alpha: float = 0.95) -> float:
    """
    Calculates Value at Risk (VaR) using the Historical Simulation method.
    :param returns: A Series of historical daily returns.
    :param alpha: Confidence level (default: 0.95 for 95%).
    :return: The VaR (a positive number representing potential loss).
    """
    # Sort returns from smallest (worst) to largest (best)
    sorted_returns = np.sort(returns.values)

    # At confidence level alpha, the critical quantile is (1 - alpha)
    # e.g., alpha=0.95 corresponds to the worst 5%
    index = int((1 - alpha) * len(sorted_returns))

    # VaR is taken as a positive value indicating potential loss
    # If returns are negative, use the negative sign to represent the loss
    var = -sorted_returns[index]
    return var


def main():
    """
    Example main function:
    - Download Apple's (AAPL) historical data for approximately 1 year
    - Compute daily returns
    - Calculate VaR at the 95% confidence level (1-day VaR)
    """
    ticker = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2023-01-01'
    alpha = 0.95

    print(f"Downloading stock data for {ticker} from {start_date} to {end_date}...")
    df = download_stock_data(ticker, start_date, end_date)

    print("Calculating daily returns...")
    returns = calculate_daily_returns(df)

    print(f"Calculating VaR at {int(alpha*100)}% confidence level using Historical Simulation...")
    var_value = historical_simulation_var(returns, alpha=alpha)

    # If you want to display as a percentage, multiply by 100
    print(f"Value at Risk (VaR) = {var_value:.4%} (daily)")
    # Example output: 2.0100% means a 2.01% potential loss for 1 day

if __name__ == '__main__':
    main()
