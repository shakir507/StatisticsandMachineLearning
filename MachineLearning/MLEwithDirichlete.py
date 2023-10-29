#first we will construct the MLE for Dirichlete distribution

import numpy as np
import pandas as pd
import scipy.special as st
#data section begins
#observed data is the dengue serotype proportions,
#where only three serotypes are assumes in a year for example
observed_data=[0.1,0.5,0.4]
# observed_data=[0.1*100,0.5*100,0.4*100]

#data section ends
alpha1=[0,0,0]
#the likelihood function for an observed data with three variables, x1,x2,x3 is given by
alpha=[2,3,4]
def DirLik(alpha,observed_data):
   nrm=st.gamma(np.sum(alpha))
#    print(nrm)
   obspow=[(observed_data[i]**alpha[i])/st.gamma(alpha[i]) for i in range(len(observed_data))]
#    print(obspow)
   lk=np.prod(obspow)/nrm
   return lk


#Now we can look to find the value of the parameter 'p' for which the above likelihood function is maximum or (-likelihood is minimum):

# we can in the meanwhile plot and check the parameter value where the function might achieve its maximum:
Nmax=12
lk=np.zeros((Nmax,Nmax))
i1=0
max1=-10
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
            print(i1,j1,max1)
        j1=j1+1
    i1=i1+1
    # print("\n")
# print(lk)
print("The most likely parameters that will produce the given data from a dirichlter distribution are")
print(alpha1,max1)
# plot(seq(0,1,0.01),lk,type='b',col='red')