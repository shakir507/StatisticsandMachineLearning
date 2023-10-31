import numpy as np
import pandas as pd
import scipy.stats as st
import scipy.special as sp
from MLEWithDist import *
import matplotlib.pyplot as plt

#data section begins
n=199*2
x1=200
#data section ends

#likelihood function begins
lk,p=likelihood(x1,n)
maxlk=max(lk)

lk1=[lk[i]*1/maxlk for i in range(len(lk))]

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

    posterior=[lk[i]*prior0[i] for i in range(len(lk))]
    prior0=posterior
    maxp=max(posterior)
    maxlk=max(lk)

    posterior=[posterior[i]*1/maxp for i in range(len(posterior))]

    plt.plot(p,posterior,'.-') #posterior

plt.show()