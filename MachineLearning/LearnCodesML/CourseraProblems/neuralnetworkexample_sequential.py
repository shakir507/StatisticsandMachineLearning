from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import tensorflow as tf

tf.random.set_seed(1234)  # applied to achieve consistent results


x = np.array([[200.0,17.0],[120,5],[425,20],[212,18],[214,20],[210,19],[390,20],[400,20]])
y = np.array([1,0,0,1,1,1,0,0])  # binary labels

model = Sequential([
    Dense(3, activation='sigmoid'),
    Dense(1, activation='sigmoid')  # sigmoid activation for binary classification
])

model.compile(optimizer='sgd', loss='binary_crossentropy')  # binary cross-entropy for binary classification

model.fit(x, y, epochs=1000)

x_new = np.array([[200.0,19.0]])
y_pred = model.predict(x_new)

print('The predicted probability is', y_pred[0][0])

yhat = 1 if y_pred > 0.5 else 0
print('The predicted class is', yhat)