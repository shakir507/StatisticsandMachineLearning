import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from gradientdescent import gradient_descent
import matplotlib.pyplot as plt

california = fetch_california_housing()#This is a dataset of house prices in California based on various features such as the median income, average house age, and average number of rooms.

# Define the input and target data

X = california.data #This is the input data. columns are the features and rows are the samples. The features are the median income, average house age, average number of rooms, average number of bedrooms, population, average occupancy, latitude, and longitude.
Y = california.target

#Feature scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Add a column of ones to the input data
ones = np.ones((X.shape[0], 1))
X = np.hstack((ones, X))

# plt.scatter(X[:, 0], Y)
# plt.xlabel('Median Income')
# plt.ylabel('Median House Value')
# plt.show()

# Perform gradient descent
learning_rate = 0.01
num_iterations = 1000
theta, cost_history = gradient_descent(X, Y, learning_rate, num_iterations)


# Print the results
print('Theta:', theta)

#Next we will plot the cost history to see how the cost function changes over time. Also plot the fitted line on the scatter plot of the median income and median house value.

#Creating a multiplot with the cost history and the fitted line
#Import the required libraries for multiplot

import matplotlib.pyplot as plt

#start a new figure with a specified size and dpi multiplot

plt.figure(figsize=(10, 5), dpi=100)

#Plot the cost history

plt.subplot(1, 2, 1)
plt.plot(range(num_iterations), cost_history)
plt.xlabel('Iterations')
plt.ylabel('Cost')

#Plot the fitted line

plt.subplot(1, 2, 2)
plt.scatter(X[:, 1], Y)
plt.plot(X[:, 1], np.dot(X, theta), color='red')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.show()



# # Plot the cost history
# plt.plot(range(num_iterations), cost_history)
# plt.xlabel('Iterations')
# plt.ylabel('Cost')
# plt.show()

# # Plot the fitted line
# plt.scatter(X[:, 1], Y)
# plt.plot(X[:, 1], np.dot(X, theta), color='red')
# plt.xlabel('Median Income')
# plt.ylabel('Median House Value')
# plt.show()
# The cost function decreases over time, which is expected. The fitted line also seems to fit the data well.
# 
