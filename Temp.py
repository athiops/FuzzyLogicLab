def hot_temperature(temp):
    if temp <= 20:
        return 0.0
    elif temp >= 35:
        return 1.0
    else:
        return (temp - 20) / (35 - 20)

temperature = 30
membership = hot_temperature(temperature)

print("Temperature:", temperature)
print("Degree of hotness:", membership)