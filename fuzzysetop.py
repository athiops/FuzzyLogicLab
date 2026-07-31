A = [0.2, 0.7, 1.0]
B = [0.6, 0.4, 0.8]

union = [max(a, b) for a, b in zip(A, B)]
intersection = [min(a, b) for a, b in zip(A, B)]
complement_A = [1 - a for a in A]
difference = [min(a, 1 - b) for a, b in zip(A, B)]

print("Union:", union)
print("Intersection:", intersection)
print("Complement of A:", complement_A)
print("A - B:", difference)
