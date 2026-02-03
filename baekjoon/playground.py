import sys
import heapq
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    for x in map(int, input().split()):
        if len(hq) < n:
            heapq.heappush(hq, x)
        else:
            # 현재 힙의 최소값보다 큰 수만 교체
            if x > hq[0]:
                heapq.heapreplace(hq, x)

print(hq[0])