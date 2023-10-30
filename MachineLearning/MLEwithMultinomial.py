import numpy as np
from scipy.stats import multinomial

# Observed data (example data for three categories)
observed_data = [1, 4, 7]
max1=-1000
lk=np.zeros((10,10))
# Probabilities for each category
i1=0
im=0
jm=0
for p1 in np.arange(0,1,0.1):
    j1=0
    for p2 in np.arange(0,1,0.1):
        p3=1-p1-p2
        if(p3>0):
            probabilities = [p1, p2, p3]
            # Calculate the likelihood using the Multinomial distribution
            likelihood = multinomial.pmf(observed_data, n=np.sum(observed_data), p=probabilities)
            lk[i1][j1]=likelihood
            if(likelihood>max1):
                max1=likelihood
                im=p1
                jm=p2
            formatted_value = "{:.3f}".format(lk[i1][j1])
            print(formatted_value,end=" ")
        j1+=1
    print("\n")
    i1+=1

# print("Maximum Likelihood:",likelihood, max1,im,jm,1-im-jm)
# print(lk)