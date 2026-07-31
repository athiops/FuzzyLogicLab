A = [0.3, 0.8]
B = [0.7, 0.4]

lhs = [1 - max(a, b) for a, b in zip(A, B)]
rhs = [min(1 - a, 1 - b) for a, b in zip(A, B)]

print("LHS:", lhs)
print("RHS:", rhs)
print("De Morgan law satisfied:", lhs == rhs)