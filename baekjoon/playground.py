# 1927 "최소 힙"

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x:
        heappush(heap, x)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)