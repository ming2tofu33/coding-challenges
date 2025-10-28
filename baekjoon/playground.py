import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

q = deque()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            q.append((r, c))

while q:
    r, c = q.popleft()
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0:
            box[nr][nc] = box[r][c] + 1
            q.append((nr, nc))

ans = 0
for r in range(N):
    for c in range(M):
        if box[r][c] == 0:
            print(-1)
            sys.exit(0)
        ans = max(ans, box[r][c])

print(ans - 1)