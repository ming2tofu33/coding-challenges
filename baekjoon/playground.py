# 11286 "절댓값 힙"

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x:
        heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)