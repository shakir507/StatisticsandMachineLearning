import numpy as np
import pandas as pd
import scipy.stats as st
import scipy.special as sp
from MLEWithDist import *
import matplotlib.pyplot as plt

#data section begins
n=199*2
x1=100
#data section ends

lk,p=likelihood(x1,n)
#prior distribution begins
prior_a=50#uniform prior
prior_b=50#uniform prior

prior=st.beta.pdf(p,prior_a,prior_b)/sp.beta(prior_a,prior_b)
print(len(prior))
#prior distribution ends
posterior=[lk[i]*prior[i] for i in range(len(lk))]
maxp=max(posterior)
maxlk=max(lk)
lk=[lk[i]*1/maxlk for i in range(len(lk))]
posterior=[posterior[i]*1/maxp for i in range(len(posterior))]
ic=lk.index(max(lk))
ipc=posterior.index(max(posterior))

print(p[ic],posterior[ipc],ic,ipc,max(lk))

plt.plot(p,lk,'.-') #likelihood
plt.plot(p,posterior,'.-') #posterior
plt.show()