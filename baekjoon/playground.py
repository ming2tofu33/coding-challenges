import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, N + 1):
    adj[i].sort()

dfs_order = []
visited = [False] * (N + 1)
stack = [V]

while stack:
    node = stack.pop()
    if visited[node]:
        continue
    visited[node] = True
    dfs_order.append(node)
    for nxt in reversed(adj[node]):
        if not visited[nxt]:
            stack.append(nxt)

print(*dfs_order)

bfs_order = []
visited = [False] * (N + 1)
q = deque([V])
visited[V] = True

while q:
    node = q.popleft()
    bfs_order.append(node)
    for nxt in adj[node]:
        if not visited[nxt]:
            visited[nxt] = True 
            q.append(nxt)

print(*bfs_order)
