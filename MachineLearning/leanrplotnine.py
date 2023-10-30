import numpy as np
import pandas as pd
from plotnine import *
from scipy.stats import multivariate_normal

# Define the equilateral triangle's vertices
vertices = pd.DataFrame({
    'x': [0, 0.5, 1, 0],
    'y': [0, (3 ** 0.5) / 2, 0, 0]
})

# Define the mean and covariance matrix for a 2D Gaussian distribution
mean = [0.5, (3 ** 0.5) / 6]
covariance = np.array([[0.02, 0.01], [0.01, 0.03]])

# Generate a grid within the equilateral triangle
n = 100
u = np.linspace(0, 1, n)
v = np.linspace(0, 1, n)
U, V = np.meshgrid(u, v)
mask = U + V <= 1

# Apply the coordinate transformation to ensure points stay within the triangle
X = U * vertices['x'][1] + V * vertices['x'][2]
Y = U * vertices['y'][1] + V * vertices['y'][2]
U = np.ma.masked_array(X, mask=~mask)
V = np.ma.masked_array(Y, mask=~mask)

grid = pd.DataFrame({
    'x': U.flatten(),
    'y': V.flatten()
})

# Calculate the probability density of the Gaussian distribution on the grid
pdf_values = multivariate_normal.pdf(grid, mean=mean, cov=covariance)

# Create a plot
plot = (
    ggplot() +
    geom_polygon(aes(x='x', y='y'), data=vertices, fill='lightgrey', color='black') +
    geom_tile(aes(x='x', y='y', fill='pdf_values'), data=grid.assign(pdf_values=pdf_values), size=0.01) +
    geom_point(aes(x='x', y='y'), data=vertices, color='red', size=3) +  # Include vertices
    geom_path(aes(x='x', y='y'), data=vertices, color='red', size=0.5) +  # Connect the vertices
    scale_fill_gradient(low='white', high='blue') +
    theme_void() +
    labs(title='2D Gaussian Distribution on Equilateral Triangle', x='', y='') +
    theme(legend_position='none')
)

# Show the plot
print(plot)
