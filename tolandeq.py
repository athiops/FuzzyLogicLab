R = [
    [1, 0.5, 0.3],
    [0.5, 1, 0.4],
    [0.3, 0.4, 1]
]

def is_reflexive(R):
    for i in range(len(R)):
        if R[i][i] != 1:
            return False
    return True

def is_symmetric(R):
    n = len(R)
    for i in range(n):
        for j in range(n):
            if R[i][j] != R[j][i]:
                return False
    return True

print("Reflexive:", is_reflexive(R))
print("Symmetric:", is_symmetric(R))
print("Tolerance relation:", is_reflexive(R) and is_symmetric(R))