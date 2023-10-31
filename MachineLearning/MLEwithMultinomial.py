import numpy as np
from scipy.stats import multinomial



def MultinomDist(p,observed_data):
    lk=multinomial.pmf(observed_data, n=np.sum(observed_data), p=p)
    return lk

def likelihood(observed_data):
    npoints=10
    lk=np.zeros((npoints,npoints))
    # Probabilities for each category
    i1=0
    for p1 in np.arange(0,1,1.0/npoints):
        j1=0
        for p2 in np.arange(0,1,1.0/npoints):
            p3=1-p1-p2
            if(p3>0):
                probabilities = [p1, p2, p3]
                # Calculate the likelihood using the Multinomial distribution
                likelihood = multinomial.pmf(observed_data, n=np.sum(observed_data), p=probabilities)
                lk[i1][j1]=likelihood
                # formatted_value = "{:.3f}".format(lk[i1][j1])
                # print(formatted_value,end=" ")
            j1+=1
        i1+=1
    return lk

if __name__=="__main__":
    #data section begins
    # Observed data (example data for three categories)
    observed_data = [1, 4, 7]
                
    lk=likelihood(observed_data)
    # Find the index of the maximum value in the entire matrix
    max_index = np.argmax(lk)

    # Convert the flattened index to row and column indices
    row_index, col_index = np.unravel_index(max_index, lk.shape)
    max1=max(lk.flatten())
    print("Maximum Likelihood:", max1,row_index,col_index)
    # formatted_value = "{:.3f}".format(lk)
    # print(formatted_value,end=" ")