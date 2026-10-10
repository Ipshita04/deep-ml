import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    m = len(data)
    n = len(data[0])

    stdarr = []
    for i in range(m):
        temp = []
        for j in range(n):
            col_mean = np.mean(data[:, j])
            col_std = np.std(data[:, j])

            if col_std == 0:
                val = 0.0
            else:
                val = (data[i][j] - col_mean) / col_std

            temp.append(round(val, 4))
        stdarr.append(temp.copy())

    mini = np.min(data, axis=0)
    maxi = np.max(data, axis=0)

    minmaxarr = []
    for i in range(m):
        temp = []
        for j in range(n):
            if maxi[j] == mini[j]:
                val = 0.0
            else:
                val = (data[i][j] - mini[j]) / (maxi[j] - mini[j])

            temp.append(round(val, 4))
        minmaxarr.append(temp.copy())

    return np.array(stdarr), np.array(minmaxarr)