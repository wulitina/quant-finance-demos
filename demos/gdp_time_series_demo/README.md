# GDP Growth Time Series Analysis

This project demonstrates the use of Python for time series analysis, focusing on GDP growth data. The analysis includes visualizing GDP growth trends, decomposing time series data into components, and applying ARIMA modeling for forecasting future growth rates.

## Features

1. **Time Series Visualization**:
   - Plot GDP growth over time to identify general trends.

2. **Statistical Modeling**:
   - Decompose time series into trend, seasonality, and residuals using seasonal decomposition.

3. **ARIMA Modeling**:
   - Fit an ARIMA model to GDP growth data.
   - Forecast future GDP growth and evaluate the model using Mean Squared Error (MSE).

4. **Forecasting Trends**:
   - Compare actual vs predicted values using visualizations.

---

## Key Concepts

### 1. Statistical Modeling
Statistical modeling applies mathematical methods to understand the structure of data. In this project:
- **Seasonal Decomposition**: 
  - Splits the time series into three components:
    - **Trend**: Overall movement in the data (e.g., increasing GDP growth).
    - **Seasonality**: Regular, repeating patterns in the data.
    - **Residuals**: Irregular variations or noise after removing trend and seasonality.

# ARIMA Modeling and Forecasting Trends

This document explains the concepts, implementation, and applications of **ARIMA Modeling** and **Forecasting Trends** in time series analysis.

---

## 1. ARIMA Modeling

### What is ARIMA?

**ARIMA (Autoregressive Integrated Moving Average)** is a statistical model used for analyzing and forecasting time series data. It combines three components:
- **AR (Autoregressive)**: Models the relationship between an observation and its previous values.
- **I (Integrated)**: Differencing the series to make it stationary (removing trends).
- **MA (Moving Average)**: Models the dependency between an observation and residual errors from previous steps.

### Parameters
ARIMA is defined by three parameters:
- **p**: The number of lag observations included in the model (AR component).
- **d**: The number of times data needs to be differenced to remove trends (Integration).
- **q**: The size of the moving average window (MA component).

Example ARIMA configuration: `(p, d, q)` = `(2, 1, 2)`.

---

### How ARIMA Works
1. **Stationarize the Data**:
   - Time series data should be stationary (constant mean and variance over time).
   - Differencing is used to remove trends and achieve stationarity.

2. **Fit the Model**:
   - Use the AR, I, and MA components to fit the model on the training data.

3. **Forecast**:
   - Generate predictions for future time steps based on the fitted model.

---

### Example Code for ARIMA Modeling

```python
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import pandas as pd

# Sample GDP growth data
data = {
    'Year': pd.date_range(start='2000', periods=24, freq='Y'),
    'GDP Growth': [3.2, 2.8, 3.5, 3.0, 3.1, 2.9, 2.8, 3.4, 3.0, 2.9,
                   3.3, 3.1, 2.7, 2.8, 3.0, 2.9, 3.1, 3.2, 2.8, 2.7,
                   2.5, 2.9, 3.3, 3.1]
}
df = pd.DataFrame(data).set_index('Year')

# Split data into training and testing sets
train = df['GDP Growth'][:-4]
test = df['GDP Growth'][-4:]

# Fit ARIMA model
model = ARIMA(train, order=(2, 1, 2))
fitted_model = model.fit()

# Print model summary
print(fitted_model.summary())

# Forecast future values
forecast = fitted_model.forecast(steps=4)
print("Forecasted Values:", forecast)

# Evaluate using Mean Squared Error
mse = mean_squared_error(test, forecast)
print(f"Mean Squared Error (MSE): {mse}")
```
# Forecasting Trends

Forecasting trends is a critical step in time series analysis, used to predict future values based on historical data. In this project, we focus on forecasting GDP growth trends using ARIMA modeling.

---

## What is Forecasting?

Forecasting is the process of using historical data to make predictions about future outcomes. It is widely used in economics, finance, supply chain management, and other fields where understanding future behavior is essential for decision-making.

In this project, forecasting uses the ARIMA model to predict GDP growth for upcoming periods.

---

## Key Components of Forecasting

### 1. Data Preparation
- Time series data must be preprocessed to ensure:
  - **Stationarity**: The data's mean and variance are constant over time.
  - **No missing values**: Missing data can distort predictions.

### 2. Model Fitting
- Train the ARIMA model on historical data.
- Validate the model using test data to ensure accuracy.

### 3. Evaluation Metrics
To measure the accuracy of predictions, we use:
- **Mean Squared Error (MSE)**: Quantifies the average squared difference between actual and predicted values.

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
$$

- **Mean Absolute Error (MAE)**: Measures the average absolute difference between actual and predicted values.

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|
$$

---

## Example Code for Forecasting

```python
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# Simulated train and test data (replace with actual GDP growth data)
train = [3.2, 3.5, 3.0, 3.1, 3.4, 3.3, 3.1, 2.8, 2.9, 3.0]
test = [3.2, 2.9, 3.1, 3.3]
forecast = [3.1, 2.8, 3.0, 3.2]  # Example forecast values

# Evaluate accuracy
mse = mean_squared_error(test, forecast)
print(f"Mean Squared Error (MSE): {mse}")

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(range(len(train)), train, label='Training Data')
plt.plot(range(len(train), len(train) + len(test)), test, label='Actual Test Data', marker='o')
plt.plot(range(len(train), len(train) + len(test)), forecast, label='Forecast', marker='o')
plt.title('GDP Growth Forecasting')
plt.xlabel('Time')
plt.ylabel('GDP Growth (%)')
plt.legend()
plt.grid()
plt.show()
