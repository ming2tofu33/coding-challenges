import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
s = []

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    s.append(sum(l[i - 1: j ]))

print('\n'.join([str(k) for k in s]))