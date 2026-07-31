students = ["S1", "S2"]
subjects = ["Math", "Physics"]

R = [
    [0.9, 0.6],
    [0.4, 0.8]
]

for i, student in enumerate(students):
    for j, subject in enumerate(subjects):
        print(student, "interest in", subject, "=", R[i][j])