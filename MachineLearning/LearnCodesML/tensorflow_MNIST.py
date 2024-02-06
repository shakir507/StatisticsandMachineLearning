import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import tensorflow as tf
from sklearn.model_selection import train_test_split

#load data from mnist dataset
mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()
dataX=np.concatenate((x_train,x_test))
dataY=np.concatenate((y_train,y_test))
train_size=0.8
test_size=0.2
#split data into train and test
xtest,xtrain,ytest,ytrain=train_test_split(dataX,dataY,test_size=test_size,train_size=train_size)
#reshape data
print(dataX.shape,dataY.shape,x_train.shape,y_train.shape,x_test.shape,y_test.shape)