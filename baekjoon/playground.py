# 1931 "회의실 배정" 

import sys
input = sys.stdin.readline

N = int(input())
times = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
cnt = final_end = 0
for start, end in times:
    if final_end <= start:
        cnt += 1
        final_end = end

print(cnt)