#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
sharpe_ratio_demo.py

Demonstration of how to compute the annualized Sharpe Ratio for a single stock
using yfinance data, ensuring we don't hit the "ambiguous Series" issue.
"""

import yfinance as yf
import pandas as pd
import numpy as np

def download_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Downloads historical stock data (Adjusted Close) from Yahoo Finance
    and returns a DataFrame with a 'Close' column.

    :param ticker: The stock ticker (e.g. 'AAPL')
    :param start_date: Start date in 'YYYY-MM-DD' format
    :param end_date: End date in 'YYYY-MM-DD' format
    :return: A DataFrame containing a 'Close' column.
    """
    df = yf.download(ticker, start=start_date, end=end_date)
    if 'Adj Close' in df.columns:
        # Use Adjusted Close if available
        df = df[['Adj Close']].rename(columns={'Adj Close': 'Close'})
    else:
        # Fallback to 'Close'
        df = df[['Close']]
    return df

def compute_daily_returns(prices: pd.Series) -> pd.Series:
    """
    Computes daily percentage returns for a single-column Series of prices.

    :param prices: A pandas Series of prices indexed by date
    :return: A pandas Series of daily returns (percentage change), indexed by date
    """
    # Ensure it's actually a Series, not a DataFrame
    if isinstance(prices, pd.DataFrame):
        # Pick the first column if needed
        prices = prices.iloc[:, 0]
    returns = prices.pct_change().dropna()
    return returns

def compute_annualized_sharpe_ratio(returns: pd.Series, annual_risk_free_rate: float = 0.02) -> float:
    """
    Computes the annualized Sharpe Ratio for daily returns.

    :param returns: A single-column Series of daily returns (e.g., 0.01 for 1%)
    :param annual_risk_free_rate: Annual risk-free rate, e.g. 0.02 for 2%
    :return: A float representing the annualized Sharpe Ratio
    """
    trading_days_per_year = 252  # Approximate number of trading days in a year

    # Convert annual risk-free rate to an approximate daily risk-free rate
    daily_rf = (1 + annual_risk_free_rate) ** (1 / trading_days_per_year) - 1

    # Calculate daily excess returns
    excess_daily_returns = returns - daily_rf

    # Mean of excess daily returns (ensure it's a float)
    avg_excess_return_daily = float(excess_daily_returns.mean())

    # Standard deviation of daily returns (ensure it's a float)
    std_daily = float(excess_daily_returns.std())

    # Annualize
    avg_excess_return_annual = avg_excess_return_daily * trading_days_per_year
    std_annual = std_daily * np.sqrt(trading_days_per_year)

    # Avoid division by zero
    if std_annual == 0:
        return 0.0

    return avg_excess_return_annual / std_annual

def main():
    """
    Main function demonstrating how to use the above routines to compute
    the Sharpe Ratio for a single stock (AAPL) over a given date range.
    """
    ticker = 'AAPL'
    start_date = '2022-01-01'
    end_date   = '2023-01-01'
    annual_risk_free_rate = 0.02  # 2% per year

    print(f"Downloading {ticker} data from {start_date} to {end_date}...")
    df = download_stock_data(ticker, start_date, end_date)

    print("Computing daily returns...")
    daily_returns = compute_daily_returns(df['Close'])

    print("Calculating annualized Sharpe Ratio...")
    sharpe_ratio = compute_annualized_sharpe_ratio(
        daily_returns,
        annual_risk_free_rate=annual_risk_free_rate
    )

    print(f"Annualized Sharpe Ratio for {ticker}: {sharpe_ratio:.4f}")

if __name__ == "__main__":
    main()
