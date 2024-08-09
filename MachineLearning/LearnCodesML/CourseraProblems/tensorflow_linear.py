import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
# Define the data
X_train = np.array([[1.0], [2.0]], dtype=np.float32)           #(size in 1000 square feet)
Y_train = np.array([[300.0], [500.0]], dtype=np.float32)       #(price in 1000s of dollars)

# Define the model
linear_layer=Dense(units=1,activation='linear',input_shape=[1])

print(linear_layer.get_weights())
print(X_train[0].reshape(1,1))
a1=linear_layer(X_train[0].reshape(1,1))
w,b=linear_layer.get_weights()
# print(f"Initial weights: {w}, Initial bias: {b}")

set_w = np.array([[200]])
set_b = np.array([100])

# set_weights takes a list of numpy arrays
linear_layer.set_weights([set_w, set_b])
# print(linear_layer.get_weights())

#compare the output of the layer with the linear equation
a1 = linear_layer(X_train[0].reshape(1,1))
# print(a1)
alin = np.dot(set_w,X_train[0].reshape(1,1)) + set_b
# print(alin)#compare the output of the layer with the linear equation. The output should be the same as the linear equation, which is 200*1+100=300

#now that we have set the weights and bias, we can use the linear layer to predict the price of the house
prediction_tf = linear_layer(X_train)
prediction_np = np.dot( X_train, set_w) + set_b
print(prediction_tf)
print(prediction_np)

plt.plot(X_train, Y_train, 'ro', label='Original data')
plt.plot(X_train, prediction_tf, label='Tensorflow prediction')
plt.plot(X_train, prediction_np, label='Numpy Prediction')

plt.legend()
plt.show()