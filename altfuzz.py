a = 0.6
b = 0.7

algebraic_product = a * b
algebraic_sum = a + b - a * b
bounded_sum = min(1, a + b)
bounded_difference = max(0, a + b - 1)

print("Algebraic product:", algebraic_product)
print("Algebraic sum:", algebraic_sum)
print("Bounded sum:", bounded_sum)
print("Bounded difference:", bounded_difference)