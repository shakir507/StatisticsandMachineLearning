import numpy as np
import pandas as pd
import scipy.stats as st
import scipy.special as sp
from MLEwithMultinomial import *
import matplotlib.pyplot as plt

#data section begins
observed_data = [1, 4, 7]
#data section ends

#likelihood function begins
lk,p=likelihood(observed_data)
max_index = np.argmax(lk)

# Convert the flattened index to row and column indices
row_index, col_index = np.unravel_index(max_index, lk.shape)
maxlk=max(lk.flatten())
print("Maximum Likelihood:", maxlk,row_index,col_index)
lk1=np.zeros((len(lk),len(lk)))
for i in range(len(lk)):
    lk1[i,:]=[lk[i,j]*1/maxlk for j in range(len(lk))]

#likelihood function ends

#prior distribution begins
prior_a=1#uniform prior
prior_b=1#uniform prior

# prior0=st.gamma.pdf(p,prior_a,1.0/prior_b)
prior0=st.beta.pdf(p,prior_a,prior_b)/sp.beta(prior_a,prior_b)
#prior distribution ends

print(len(prior0))

plt.plot(p,lk1,'.-') #plot likelihood
# plt.plot(p,prior0,'.-') #plot likelihood

for up in range(10):#updating the beilef ten times each time using the posterior as the prior

    posterior=np.zeros((len(lk),len(lk)))
    for i in range(len(lk)):
        posterior[i,:]=[lk[i,j]*prior0[i,j] for j in range(len(lk))]
    prior0=posterior
    maxp=max(posterior)
    max_index = np.argmax(posterior)

    # Convert the flattened index to row and column indices
    row_index, col_index = np.unravel_index(max_index, posterior.shape)
    maxlp=max(posterior.flatten())
    for i in range(len(lk)):
        posterior[i,:]=[posterior[i,j]*1/maxp for j in range(len(posterior))]

    plt.plot(p,posterior,'.-') #posterior

plt.show()