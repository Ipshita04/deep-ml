def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    # Your code here
    total=0
    fav=0
    b=False
    for i in data:
      if(i[0]==x):
        b=True
        total+=1
        if(i[1]==y):
          fav+=1
    if(b):
      return round(fav/total,4)
    return 0.0  
    pass