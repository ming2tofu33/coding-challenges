# 1764 "듣보잡"

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

heard = set(input().rstrip() for _ in range(n))
both = []

for _ in range(m):
    name = input().rstrip()
    if name in heard:
        both.append(name)

both.sort()

print(len(both))
print('\n'.join(both))