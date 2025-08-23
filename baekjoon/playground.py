# 11047 "동전 0"

import sys

n, k = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]

i = n - 1
while i >= 0 and a[i] > k:
    i -= 1

c = 0
while k > 0 and i >= 0:
    if a[i] <= k:
        c += k // a[i]
        k %= a[i]
    i -= 1

print(c)
