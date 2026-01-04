# 32068 "보물 찾기"

import sys
input = sys.stdin.readline

def time_to_reach(S, X):
    if X == S:
        return 1
    d = abs(X - S)
    if X > S:
        return 2 * d
    else: 
        return 2 * d + 1

T = int(input())
for _ in range(T):
    L, R, S = map(int, input().split())
    print(min(time_to_reach(S, L), time_to_reach(S, R)))