# Portfolio Analysis with Streamlit

This project aims to analyze portfolio data using Streamlit, a popular Python library for building interactive web applications. It provides insights into the portfolio value, optimal buy indices, and transition distribution based on the given dataset.

## Problem Statement

Investors often seek tools to analyze their portfolio performance and make informed decisions. This project addresses this need by providing a user-friendly interface to analyze portfolio data and understand market trends.

## Code Flow for analysis.py

1. **Data Preparation**: The dataset is read and processed to extract relevant information such as closing prices.

2. **Calculations**: Returns are calculated based on the closing prices, and the state of the market (Bull, Flat, or Bear) is determined.

3. **Portfolio Analysis**: Portfolio value is calculated based on predefined rules (e.g., buying during Bull markets and selling during Bear markets). Optimal buy indices are identified.

4. **Transition Distribution**: The distribution of state transitions (e.g., from Bull to Flat, Flat to Bear) is computed to understand market behavior.

5. **Streamlit Integration**: The results are displayed using Streamlit, providing an interactive and user-friendly interface for portfolio analysis.

## Code Flow for plot_analysis.py

1. **Data**: The dataset contains historical time series data.

2. **Auto ARIMA Model**: The auto_arima function from the pmdarima library is used to automatically select the optimal ARIMA parameters for the time series forecasting.

3. **Training and Testing**: The dataset is split into training and testing sets. The last 50 data points are used for testing, and the remaining data is used for training.

4. **Forecasting**: The Auto ARIMA model is trained on the training data, and then used to forecast future values for the test period.

5. **Visualization**: The forecasted values are plotted along with the actual test data to visualize the performance of the model.


## Use of Streamlit

Streamlit is a powerful tool for building interactive web applications with minimal effort. In this project, Streamlit is used to create a user interface for portfolio analysis, allowing users to:

- View portfolio value over time
- Identify optimal buy indices
- Explore transition distribution of market states

## Images

### Interface Preview

![image](https://github.com/barath-sk17/sigma_hackathon/assets/127032804/f8d71a1b-bd34-4da9-a5b2-2bf36333eb37)


![image](https://github.com/barath-sk17/sigma_hackathon/assets/127032804/cda842b2-0302-4d1d-bf2c-36ea8cdfcd04)



