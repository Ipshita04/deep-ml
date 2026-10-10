import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    col_mean=[]
    col_std=[]
    for i in range(len(X_train[0])):
        col_mean.append(X_train[:,i].mean())
        col_std.append(X_train[:,i].std())
        if(col_std[i]==0):
            col_std[i]=1
    ans=[]
    for i in range(len(X_test)):
        temp=[]
        for j in range(len(X_test[0])):
            temp.append((X_test[i][j]-col_mean[j])/col_std[j])
        ans.append(temp.copy())
    return np.array(ans)        
    pass
