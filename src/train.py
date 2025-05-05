import numpy as np
from src.model import build_model
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.optimizers import Adam

# Assume X_train and y_train are prepared
model = build_model((X_train.shape[1], 1))
model.compile(optimizer=Adam(), loss='mean_squared_error')
model.fit(X_train, y_train, epochs=20, batch_size=32)
model.save('results/lstm_model.h5')
