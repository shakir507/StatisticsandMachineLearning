from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the data

X=np.array([[1,1],[2,1],[3,2],[-1,-1],[-2,-1],[-3,-2]])

#compute principal components

pca_1=PCA(n_components=2)
pca_1.fit(X)

print(pca_1.explained_variance_ratio_)

X_trans_1=pca_1.transform(X)

X_reduced_1=pca_1.inverse_transform(X_trans_1)

print(X_reduced_1)
print(X_trans_1)

#plot the data

plt.scatter(X[:,0],X[:,1],color='r')
plt.scatter(X_reduced_1[:,0],X_reduced_1[:,1],color='b')
plt.show()