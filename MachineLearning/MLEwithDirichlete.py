#first we will construct the MLE for Dirichlete distribution

import numpy as np
import pandas as pd
import scipy.special as st
#data section begins
#observed data is the dengue serotype proportions,
#where only three serotypes are assumes in a year for example
observed_data=[0.1,0.5,0.4]
#data section ends
alpha1=[0,0,0]
#the likelihood function for an observed data with three variables, x1,x2,x3 is given by
alpha=[2,3,4]
def DirLik(alpha, observed_data):
    """
    Calculate the likelihood of a Dirichlet distribution.

    Parameters:
    - alpha: A list of shape parameters for the Dirichlet distribution.
    - observed_data: A list of observed proportions.

    Returns:
    - likelihood: The likelihood of the Dirichlet distribution.
    """
    nrm = st.gamma(np.sum(alpha))
    obspow = [(observed_data[i] ** alpha[i]) / st.gamma(alpha[i]) for i in range(len(observed_data))]
    likelihood = np.prod(obspow) / nrm
    return likelihood


#Now we can look to find the value of the parameter 'p' for which the above likelihood function is maximum or (-likelihood is minimum):

# we can in the meanwhile plot and check the parameter value where the function might achieve its maximum:
Nmax=15
lk=np.zeros((Nmax,Nmax))
i1=0
max1=-10000
pmax=[0,0,0]

for p1 in range(1,Nmax+1):
    j1=0
    for p2 in range(1,Nmax+1):
        p3=1+Nmax+Nmax-p1-p2
        alpha=[p1,p2,p3]
        # print(i1,j1)

        lk[i1][j1]=DirLik(alpha,observed_data)
        # print(" my value is ",lk[i1][j1],max1)
        if lk[i1][j1]>max1:
            # print("check max\n")
            max1=lk[i1][j1] 
            alpha1=alpha
            # print(i1,j1,max1)
        j1=j1+1
    i1=i1+1
    # print("\n")
# print(lk)
print("The most likely parameters that will produce the given data from a dirichlter distribution are")
print(alpha1,max1)
# plot(seq(0,1,0.01),lk,type='b',col='red')
# print(lk)