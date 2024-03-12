import matplotlib.pyplot as plt
from pmdarima import auto_arima
import pandas as pd

data = pd.read_csv("QuantRocket.csv")

step_fit = auto_arima(data['FIBBG000B9XRY4'], trace=True, suppress_warnings=True)
print(step_fit.summary())

# Split data into train and test
train = data.iloc[:-50]
test = data.iloc[-50:]

# Forecast using auto ARIMA model
forecast = step_fit.predict(n_periods=len(test))

# Plot forecast and test data
plt.figure(figsize=(10, 6))
plt.plot(train['FIBBG000B9XRY4'], label='Training data')
plt.plot(test['FIBBG000B9XRY4'], label='Test data')
plt.plot(forecast, label='Forecast', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Auto ARIMA Forecast vs Actual')
plt.legend()
plt.show()
