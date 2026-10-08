import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    m={}
    m["mean"]=np.mean(data)
    m["median"]=np.median(data)
    values,count=np.unique(data,return_counts=True)
    m["mode"]=values[np.argmax(count)]
    m["variance"]=np.var(data)
    m["standard_deviation"]=np.std(data)
    m["25th_percentile"]=np.percentile(data,25)
    m["50th_percentile"]=np.percentile(data,50)
    m["75th_percentile"]=np.percentile(data,75)
    m["interquartile_range"]=m["75th_percentile"]-m["25th_percentile"]
    return m
    pass