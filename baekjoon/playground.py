# 11651 "좌표 정렬하기"

import sys

n = int(sys.stdin.readline())
pairs = [tuple(reversed(tuple(map(int, sys.stdin.readline().split())))) for _ in range(n)]  # (y,x)
pairs.sort()

sys.stdout.write('\n'.join(f'{x} {y}' for y, x in pairs))