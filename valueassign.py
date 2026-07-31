def tall_membership(height):
    if height <= 150:
        return 0
    elif height >= 190:
        return 1
    else:
        return (height - 150) / 40

height = 170
print("Membership in Tall:", tall_membership(height))