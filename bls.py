import numpy as np

X = np.array([[1], [2], [3]])
Y = np.array([[2], [4], [6]])

theta = np.linalg.inv(X.T @ X) @ X.T @ Y

print("Estimated parameter:", theta)