import numpy as np
import pandas as pd


def gradient_descent(X, Y, learning_rate, num_iterations):
    """
    Perform gradient descent to minimize the cost function.

    :param X: np.array, input data
    :param Y: np.array, target data
    :param learning_rate: float, learning rate
    :param num_iterations: int, number of iterations
    :return: tuple, (theta, cost_history)
    """
    # Initialize the parameters
    m = X.shape[0]
    n = X.shape[1]
    print(m,n)
    theta = np.zeros(n)
    cost_history = np.zeros(num_iterations)
    theta_history = np.zeros((num_iterations, n))

    # Perform gradient descent
    for i in range(num_iterations):
        # Calculate the predicted values
        predicted = np.dot(X, theta)

        # Calculate the error
        error = predicted - Y

        # Calculate the cost function
        cost = (1 / (2 * m)) * np.sum(error ** 2)
        cost_history[i] = cost

        # Calculate the gradient
        gradient = (1 / m) * np.dot(X.T, error)

        # Update the parameters
        theta -= learning_rate * gradient
        theta_history[i, :] = theta
        # if i % 2 == 0:  # Print debug information every 100 iterations
        #     print(f"Iteration {i}, Cost: {cost}, Theta: {theta}")

        # if np.isnan(cost) or np.isinf(cost):
        #     print("Encountered NaN or Inf cost. Stopping early.")
        #     break

    return theta, cost_history, theta_history

