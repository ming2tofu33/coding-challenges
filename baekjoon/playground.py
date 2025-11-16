# 2028 "자기복제수"

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    print('YES' if int(str(n**2)[-len(str(n)):]) == n else 'NO')