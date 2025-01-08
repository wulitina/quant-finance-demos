import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

def linear_regression_stock_prediction(stock_ticker, start_date, end_date):
    # Fetch data
    stock_data = yf.download(stock_ticker, start=start_date, end=end_date)
    stock_data['Date'] = stock_data.index

    # Prepare features and target
    stock_data['Day'] = range(len(stock_data))
    X = stock_data[['Day']]
    y = stock_data['Close']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Visualize
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Prices')
    plt.title(f'Stock Price Prediction: {stock_ticker}')
    plt.xlabel('Days')
    plt.ylabel('Close Price')
    plt.legend()
    plt.savefig('prediction.png')
    plt.show()

    return mse, r2

if __name__ == "__main__":
    stock_ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2023-12-31"
    mse, r2 = linear_regression_stock_prediction(stock_ticker, start_date, end_date)
    print(f"Mean Squared Error: {mse}")
    print(f"R² Score: {r2}")
