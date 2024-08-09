# UNQ_C1
# GRADED FUNCTION: find_closest_centroids

def find_closest_centroids(X, centroids):
    """
    Computes the centroid memberships for every example
    
    Args:
        X (ndarray): (m, n) Input values      
        centroids (ndarray): (K, n) centroids
    
    Returns:
        idx (array_like): (m,) closest centroids
    
    """

    # Set K
    K = centroids.shape[0]

    # You need to return the following variables correctly
    idx = np.zeros(X.shape[0], dtype=int)

    ### START CODE HERE ###
    
    for i in range(X.shape[0]):
        dist=[]
        for j in range(K):
            norm_ij=np.linalg.norm(X[i,:],centroids[j,:])
            dist.append(norm_ij)
        idx[i]=np.argmin(dist)
        
            
            
        
     ### END CODE HERE ###
    
    return idx