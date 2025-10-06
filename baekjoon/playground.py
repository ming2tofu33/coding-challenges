import sys

n = int(sys.stdin.readline())

d = {}

for _ in range(n):
    lastname = sys.stdin.readline()[0]
    if lastname in d:
        d[lastname] += 1
    else:
        d[lastname] = 1

l = []

for i in d:
    if d[i] >= 5:
        l.append(i)

l.sort()

if l:
    print(''.join([j for j in l]))
else:
    print("PREDAJA")