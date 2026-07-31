import numpy as np

# Data
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2, 4, 6, 8, 10])

# Initial values
theta = np.array([[0.0]])
P = np.array([[1000.0]])
lam = 1.0

for x, y in zip(x_data, y_data):
    phi = np.array([[x]])
    y_pred = phi.T @ theta
    error = y - y_pred[0, 0]
    
    K = (P @ phi) / (lam + phi.T @ P @ phi)
    theta = theta + K * error
    P = (1 / lam) * (P - K @ phi.T @ P)

print("Estimated theta:", theta)