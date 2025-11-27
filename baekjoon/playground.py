# 34071 "첫 번째 문제는 정말 쉬운 문제일까?"

import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

f = l[0]
l.sort()

if f == l[0]:
    print('ez')
elif f == l[-1]:
    print('hard')
else:
    print('?')