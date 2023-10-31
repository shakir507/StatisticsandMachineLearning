import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

#first we will construct the MLE for binomial distribution



#the likelihood function for an observed data, x1 in n trails, is given by

def BinFunct(p,x1,n):
    lk=sp.comb(n,x1)*(p**x1)*((1-p)**(n-x1))
    return lk

#Now we can look to find the value of the parameter 'p' for which the above likelihood function is maximum or (-likelihood is minimum):

# we can in the meanwhile plot and check the parameter value where the function might achieve its maximum:
def likelihood(x1,n):
    dp=1000
    lk=[0 for x in range(dp)]
    i=0
    max1= -10
    pmax=0
    prange=np.arange(0,1,1.0/dp)
    for p in prange:
        lk[i]=BinFunct(p,x1,n)
        if lk[i]>max1:
            max1=lk[i]
        i=i+1
    return lk,prange


if __name__=="__main__":
    #data section begins
    n=199*2
    x1=199
    #data section ends

    lk,p=likelihood(x1,n)
    ic=lk.index(max(lk))
    print(p[ic],max(lk))
    plt.plot(p,lk,'.-')
    plt.show()