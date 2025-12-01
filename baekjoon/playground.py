# 10989 "수 정렬하기 3"

import sys

n = int(sys.stdin.readline())

cnt = [0] * 10001

for _ in range(n):
    a = int(sys.stdin.readline())
    cnt[a] += 1

for i in range(1, 10001):
    c = cnt[i]
    if c:
        sys.stdout.write((str(i) + '\n') * c)