# 25206 "너의 평점은"

import sys

lines = sys.stdin.read().splitlines()

subject_grades = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0, "P": None}
div = 0
total = 0

for line in lines:
    _, grade, subject_avg = line.split()
    if subject_avg == "P":
        pass
    else:
        total += float(grade) * subject_grades[subject_avg]
        div += float(grade) 

print(total / div)
