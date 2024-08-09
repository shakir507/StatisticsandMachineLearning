#In this example we will explore forward propagation in a neural network
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

tf.random.set_seed(1234)  # applied to achieve consistent results

x=np.array([[200.0,17.0],[120,5],[425,20],[212,18]])
x_new=np.array([[200.0,20.0]])
y=np.array([1,0,0,1])
layer_1=Dense(3,activation='sigmoid')
layer_2=Dense(1,activation='sigmoid')
a_1=layer_1(x_new)
a_2=layer_2(a_1)
print(a_2)
# model=Sequential([layer_1,layer_2])
# model.compile(optimizer='sgd',loss='mean_squared_error')
# model.fit(x,y,epochs=1000)
# a_2=model.predict(x_new)
# Print the result
if a_2>0.5:
    yhat=1
else:
    yhat=0
print('The result is',yhat)
