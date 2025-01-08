import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

def load_gdp_data():
    """
    Simulates loading GDP growth data. Replace with actual data loading logic.
    """
    data = {
        'Year': pd.date_range(start='2000', periods=24, freq='Y'),
        'GDP Growth': [3.2, 2.8, 3.5, 3.0, 3.1, 2.9, 2.8, 3.4, 3.0, 2.9,
                       3.3, 3.1, 2.7, 2.8, 3.0, 2.9, 3.1, 3.2, 2.8, 2.7,
                       2.5, 2.9, 3.3, 3.1]
    }
    df = pd.DataFrame(data)
    df.set_index('Year', inplace=True)
    return df

def visualize_data(df):
    """
    Visualizes the GDP growth data.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df, marker='o', label='GDP Growth')
    plt.title('GDP Growth Over Time')
    plt.xlabel('Year')
    plt.ylabel('GDP Growth (%)')
    plt.legend()
    plt.grid()
    plt.show()

def decompose_time_series(df):
    """
    Decomposes the time series into trend, seasonality, and residuals.
    """
    result = seasonal_decompose(df['GDP Growth'], model='additive', period=4)
    result.plot()
    plt.show()

def arima_forecasting(train, test, order=(2, 1, 2)):
    """
    Fits an ARIMA model and forecasts future values.
    """
    model = ARIMA(train, order=order)
    fitted_model = model.fit()

    print(fitted_model.summary())

    # Forecast future values
    forecast = fitted_model.forecast(steps=len(test))
    mse = mean_squared_error(test, forecast)
    print("Forecasted Values:", forecast)
    print(f"Mean Squared Error (MSE): {mse}")

    return forecast, mse

def plot_forecast(train, test, forecast):
    """
    Plots the actual vs forecasted GDP growth values.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(train, label='Training Data')
    plt.plot(test, label='Actual Test Data', marker='o')
    plt.plot(test.index, forecast, label='Forecast', marker='o')
    plt.title('GDP Growth Forecasting')
    plt.xlabel('Year')
    plt.ylabel('GDP Growth (%)')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    # Step 1: Load Data
    df = load_gdp_data()

    # Step 2: Visualize Data
    visualize_data(df)

    # Step 3: Decompose Time Series
    decompose_time_series(df)

    # Step 4: ARIMA Modeling and Forecasting
    train = df['GDP Growth'][:-4]
    test = df['GDP Growth'][-4:]
    forecast, mse = arima_forecasting(train, test)

    # Step 5: Plot Results
    plot_forecast(train, test, forecast)

if __name__ == '__main__':
    main()
