def hot(temp):
    if temp <= 25:
        return 0
    elif temp >= 35:
        return 1
    else:
        return (temp - 25) / 10


def fan_speed_from_hot(hot_value):
    return hot_value * 100


if __name__ == "__main__":
    temperature = 32
    hot_value = hot(temperature)
    fan_speed = fan_speed_from_hot(hot_value)

    print("Hot membership:", hot_value)
    print("Fan speed:", fan_speed)
