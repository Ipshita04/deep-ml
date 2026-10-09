import numpy as np

def learning_curve(X_train, y_train, X_val, y_val, train_sizes,
                   degree, bias_threshold=0.5, variance_threshold=0.5):

    train_errors = []
    val_errors = []

    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_val = np.array(X_val)
    y_val = np.array(y_val)

    for n in train_sizes:
        x = X_train[:n, 0]
        X = np.column_stack([x**i for i in range(degree + 1)])

        w = np.linalg.pinv(X) @ y_train[:n]

        train_pred = X @ w
        train_mse = np.mean((y_train[:n] - train_pred)**2)
        train_errors.append(float(train_mse))

        xv = X_val[:, 0]
        Xv = np.column_stack([xv**i for i in range(degree + 1)])

        val_pred = Xv @ w
        val_mse = np.mean((y_val - val_pred)**2)
        val_errors.append(float(val_mse))

    final_train_error = train_errors[-1]
    final_val_error = val_errors[-1]

    if final_train_error > bias_threshold:
        diagnosis = "high_bias"
    elif final_val_error - final_train_error > variance_threshold:
        diagnosis = "high_variance"
    else:
        diagnosis = "good_fit"

    return {
        "train_errors": train_errors,
        "val_errors": val_errors,
        "diagnosis": diagnosis
    }