def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    n=len(x)
    mini=min(x)
    maxi=max(x)
    if(mini==maxi):
        return float([0]*(n))
    ans=[]
    for i in x:
        ans.append((i-mini)/(maxi-mini))
    return ans        
    pass