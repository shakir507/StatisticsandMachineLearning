import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import multinomial

# Observed data (example data for three categories)
observed_data = [1, 4, 7]

# Initialize variables and grid
n = 10
lk = np.zeros((n, n))
x = np.linspace(0, 1, n)
y = np.linspace(0, 1, n)
X, Y = np.meshgrid(x, y)

# Create a grid on the 2D simplex (equilateral triangle)
n = 10
x = np.linspace(0, 1, n)
y = np.linspace(0, 1, n)
X, Y = np.meshgrid(x, y)

# Ensure that x + y <= 1 (points inside the simplex)
mask = X + Y <= 1
X = np.ma.masked_array(X, mask=~mask)
Y = np.ma.masked_array(Y, mask=~mask)

max1=-1000
# Calculate likelihood values for the grid
for i in range(n):
    for j in range(n):
        p1, p2 = X[i, j], Y[i, j]
        p3 = 1 - p1 - p2
        if p3 > 0:
            probabilities = [p1, p2, p3]
            # Calculate the likelihood using the Multinomial distribution
            likelihood = multinomial.pmf(observed_data, n=np.sum(observed_data), p=probabilities)
            lk[i, j] = likelihood
            if(likelihood>max1):
                max1=likelihood
                im=p1
                jm=p2

print("Maximum likelihood",max1,im,jm)
# Plot the likelihood values on the 2D simplex
plt.figure()
contour = plt.contourf(X, Y, lk, levels=100, cmap='viridis')
plt.colorbar(contour)
plt.title('Likelihood on the 2D Simplex (Equilateral Triangle)')
plt.xlabel('p1')
plt.ylabel('p2')
plt.show()
