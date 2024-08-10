import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import SparseCategoricalCrossentropy

def norm_l():
    norm_l = tf.keras.layers.Normalization(axis=-1)
    return norm_l
#importing mnist dataset
mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()
#normalizing the data
norm_l=norm_l()
# x_train,x_test=norm_l(x_train),norm_l(x_test)
x_train, x_test = x_train / 255.0, x_test / 255.0
# Reshape the data to fit the model input
x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)

#creating the model
# model=Sequential([Dense(25,activation='relu'),Dense(15,activation='relu'),Dense(10,activation='softmax')])

model=Sequential([Dense(25,activation='relu'),Dense(15,activation='relu'),Dense(10,activation='linear')])

#compiling the model

model.compile(loss=SparseCategoricalCrossentropy(from_logits=True),optimizer='adam')


#model fitting
model.fit(x_train,y_train,epochs=100)
softmaxit = model(x_train)
#model prediction
fx=tf.nn.softmax(softmaxit)

#print category of the images based on the highest probability
# Make predictions on the test data
predictions = model.predict(x_test)
softmaxit = model(x_test)
fx=tf.nn.softmax(softmaxit)

# # Convert the predictions to class labels
# predicted_labels = np.argmax(predictions, axis=1)

# # Print the first 10 predicted labels
# print(predicted_labels[:10])
#First calculate index of the highest probability
category=np.argmax(fx,axis=1)

print(category)
# print(fx[-1,:])  # Fix: Replace "fx[end,:]" with "fx[-1,:]"
# print(fx.shape)

#plotting the model
# tf.keras.utils.plot_model(model, to_file='model.png')
import matplotlib.pyplot as plt

# Choose a sample index to visualize
sample_index = x_test[-1]  # You can change this to any valid index

# Reshape the image back to 28x28 for visualization
image = x_test[-1].reshape(28, 28)

# # Plot the image
# plt.imshow(image, cmap='gray')
# plt.title(f'Predicted Category: {category[-1]}')
# plt.show()

#Use the model to make predictions on images taken with your phone

# Load the image
from tensorflow.keras.preprocessing import image
# Load the image
image_path = '../../../Data/mymnist/Six.jpg'
img = image.load_img(image_path, target_size=(28, 28), color_mode="grayscale")
# Resize and invert the image
img_array = image.img_to_array(img)
# Normalize and reshape the image
img_array = img_array / 255.0
img_array = img_array.reshape((1, 28*28))

prediction_iphone = model.predict(img_array)
predicted_class = np.argmax(prediction_iphone, axis=1)
print(f"The model predicts this is a: {predicted_class[0]}")