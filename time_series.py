
import numpy as np

def get_train(values, window_size):
    X, y = [], []
    len_values = len(values)
    for i in range(window_size, len_values):
        X.append(values[i-window_size:i])
        y.append(values[i])
    # 将X，y转换成矩阵
    X, y = np.asarray(X), np.asarray(y)
    # 将X转换成一个三维数组
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    print(f"X {X.shape}, y {y.shape}")
    return X, y

def get_val(values, window_size):
    X = []
    len_values = len(values)
    for i in range(window_size, len_values):
        X.append(values[i-window_size:i])
    X = np.asarray(X)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    y = values[-X.shape[0]:]
    print(f"X {X.shape}, y {y.shape}")
    return X, y