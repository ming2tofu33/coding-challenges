# 10989 "수 정렬하기 3"

import sys

input = sys.stdin.readline
write = sys.stdout.write

n = int(input())

cnt = [0] * 10001

for _ in range(n):
    a = int(input())
    cnt[a] += 1

for i in range(1, 10001):
    c = cnt[i]
    for _ in range(c):
        write(f"{i}\n")