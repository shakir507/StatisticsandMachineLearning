import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the data
file_path = '../../Data/HillsCases_deaths_hospitals_March1_2020_Aug18_2023.csv'
df = pd.read_csv(file_path, parse_dates=['date'])
data = df['total cases'].values.reshape(-1, 1)

# Scale the data to be between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data)

# Create the training and testing data
look_back = 7  # Use the last 7 days to predict the next day
X, Y = [], []
for i in range(len(data_scaled) - look_back):
    X.append(data_scaled[i:(i + look_back), 0])
    Y.append(data_scaled[i + look_back, 0])

X = np.array(X)
Y = np.array(Y)

X = np.reshape(X, (X.shape[0], X.shape[1], 1))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Build the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(look_back, 1)))
model.add(LSTM(units=50))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, Y_train, epochs=100, batch_size=32)

# Make predictions
predictions = model.predict(X_test)

# Inverse transform the predictions to get the actual values
predictions = scaler.inverse_transform(predictions)
Y_test = scaler.inverse_transform(Y_test.reshape(-1, 1))

# Plotting
plt.figure(figsize=(12, 6))
train_size = len(X_train)
test_size = len(X_test)

# Plot training data
plt.plot(df['date'][:train_size+look_back], data[:train_size+look_back], label='Training Data')

# Plot testing data
plt.plot(df['date'][train_size+look_back:train_size+test_size+look_back], data[train_size+look_back:train_size+test_size+look_back], label='Testing Data')

# Plot predictions
prediction_dates = df['date'][train_size+look_back:train_size+test_size+look_back]
plt.plot(prediction_dates, predictions, label='Predictions', color='red')

plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('COVID-19 Total Cases Prediction')
plt.legend()
plt.show()
