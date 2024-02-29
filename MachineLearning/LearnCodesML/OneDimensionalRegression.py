import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from gradientdescent import gradient_descent
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#import toy data with one feature and one target

from sklearn.datasets import make_regression

# Generate toy data
X, Y = make_regression(n_samples=100, n_features=1, noise=20, random_state=4)

X,Y=fetch_california_housing(return_X_y=True)
X=X[:,0].reshape(-1,1)
#Feature scaling

scaler = StandardScaler()
X = scaler.fit_transform(X)


# Add a column of ones to the input data

ones = np.ones((X.shape[0], 1))
X = np.hstack((ones, X))

# Perform gradient descent
learning_rate = 0.01
num_iterations = 1000
theta, cost_history, theta_hisory = gradient_descent(X, Y, learning_rate, num_iterations)


# Print the results
print('Theta:', theta)

#Next we will plot the cost history to see how the cost function changes over time. Also plot the fitted line on the scatter plot of the median income and median house value.

#Creating a multiplot with the cost history and the fitted line
#Import the required libraries for multiplot


#start a new figure with a specified size and dpi multiplot

plt.figure(figsize=(10, 5), dpi=100)

#Plot the cost history

plt.subplot(3, 1, 1)
plt.plot(range(num_iterations), cost_history)
plt.xlabel('Iterations')
plt.ylabel('Cost')

#plot theta history
plt.subplot(3, 1, 2)
plt.plot(range(num_iterations), theta_hisory)
plt.xlabel('Iterations')
plt.ylabel('Theta')


#Plot the fitted line


plt.subplot(3, 1, 3)
plt.scatter(X[:, 1], Y)
plt.plot(X[:, 1], np.dot(X, theta), color='red')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.show()

