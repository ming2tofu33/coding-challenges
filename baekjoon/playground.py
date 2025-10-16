# 11659 "구간 합 구하기 4"

import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
s = []

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    s.append(sum(l[i-1:j]))
    
sys.stdout.write("\n".join([str(i) for i in s]))