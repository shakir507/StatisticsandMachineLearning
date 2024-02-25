import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.regularizers import l2
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Load the data
file_path = '../../Data/HillsCases_deaths_hospitals_March1_2020_Aug18_2023.csv'
df = pd.read_csv(file_path, parse_dates=['date'])
df = df[df['date'] <= '2021-07-31']  # Filter data up to July 2021

data = df['total cases'].values.reshape(-1, 1)

# Smooth the data using a 7-day moving average and drop NaN values
data_smoothed = pd.Series(data.flatten()).rolling(window=7).mean().dropna().values.reshape(-1, 1)

# Scale the data to be between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data_smoothed)

# Create the training and testing data
look_back = 7  # Use the last 7 days to predict the next day
X, Y = [], []
for i in range(len(data_scaled) - look_back):
    X.append(data_scaled[i:(i + look_back), 0])
    Y.append(data_scaled[i + look_back, 0])

X = np.array(X)
Y = np.array(Y)

X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Split the data into training and testing sets
train_size = int(len(X) * 0.9)
X_train, X_test = X[:train_size], X[train_size:]
Y_train, Y_test = Y[:train_size], Y[train_size:]

# Define the LSTM model
def build_model():
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(look_back, 1),
                   dropout=0.2, recurrent_dropout=0.2))  # Add dropout and recurrent dropout
    model.add(LSTM(units=50, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(units=1, kernel_regularizer=l2(0.01)))  # Add L2 regularization to the Dense layer
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model
# Define the prediction function outside the loop
def make_predictions(model, X_test):
    predictions = model.predict(X_test)
    return scaler.inverse_transform(predictions)

# Bootstrap predictions
n_bootstraps = 100
bootstrap_predictions = []

for i in range(n_bootstraps):
    # Resample the training data with replacement
    indices = np.random.choice(range(len(X_train)), size=len(X_train), replace=True)
    X_train_resampled = X_train[indices]
    Y_train_resampled = Y_train[indices]

    # Build and train the model
    model = build_model()
    model.fit(X_train_resampled, Y_train_resampled, epochs=50, batch_size=32, verbose=0)

    # Make predictions using the defined function
    predictions = make_predictions(model, X_test)
    bootstrap_predictions.append(predictions.flatten())
    
# Calculate the median and confidence intervals
bootstrap_predictions = np.array(bootstrap_predictions)
median_predictions = np.median(bootstrap_predictions, axis=0)
lower_bound = np.percentile(bootstrap_predictions, 2.5, axis=0)
upper_bound = np.percentile(bootstrap_predictions, 97.5, axis=0)

# Plotting
plt.figure(figsize=(12, 6))
date_range = df['date'][6:]  # Adjust for the dropped NaN values

# Plot training data
plt.plot(date_range[:train_size+look_back], data_smoothed[:train_size+look_back], label='Training Data')

# Plot testing data
test_dates = date_range[train_size+look_back:]
plt.plot(test_dates, data_smoothed[train_size+look_back:], label='Testing Data', color='orange')

# Plot median predictions and confidence bands
plt.plot(test_dates, median_predictions, label='Median Predictions', color='red')
plt.fill_between(test_dates, lower_bound, upper_bound, color='red', alpha=0.3, label='95% Confidence Interval')

plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('COVID-19 Total Cases Prediction with Confidence Bands')
plt.legend()
plt.show()
