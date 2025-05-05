import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tensorflow.keras.models import load_model

model = load_model('results/lstm_model.h5')
predicted_stock_price = model.predict(X_test)

mse = mean_squared_error(y_test, predicted_stock_price)
mae = mean_absolute_error(y_test, predicted_stock_price)
rmse = np.sqrt(mse)

with open("results/metrics.txt", "w") as f:
    f.write(f"MAE: {mae}\nMSE: {mse}\nRMSE: {rmse}\n")

plt.plot(y_test, color='blue', label='Actual')
plt.plot(predicted_stock_price, color='red', label='Predicted')
plt.title('Stock Price Prediction')
plt.legend()
plt.savefig("results/plots/prediction.png")
plt.show()
