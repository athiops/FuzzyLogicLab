theta = 0.0
eta = 0.1

x_data = [1, 2, 3]
y_data = [2, 4, 6]

for epoch in range(20):
    for x, y in zip(x_data, y_data):
        y_pred = theta * x
        error = y - y_pred
        theta = theta + eta * error * x

print("Estimated theta:", theta)