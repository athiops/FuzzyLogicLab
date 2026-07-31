A = [1, 2, 3]

R = []
for x in A:
    row = []
    for y in A:
        row.append(1 if x < y else 0)
    R.append(row)

for row in R:
    print(row)