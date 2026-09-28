import numpy as np

def gaussian_mle(data: np.ndarray) -> tuple:
    """
    Compute Maximum Likelihood Estimates for Gaussian distribution parameters.
    
    Args:
        data: 1D numpy array of observations
        
    Returns:
        Tuple of (mean_mle, variance_mle)
    """
    # Your code here
    n=len(data)
    t=[]
    sum=0
    diff=0
    for i in range(n):
        sum+=data[i]
    mean=sum/n    
    t.append(mean)
    for i in range(n):
        diff+=(data[i]-mean)**(2)
    var=diff/n
    t.append(var)
    return tuple(t)    
    pass