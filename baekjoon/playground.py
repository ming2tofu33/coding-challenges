import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
box = []

for i in range(N):
    box.append(list(map(int, input().split())))

ripe = deque()
days = 0
dr = [-1, -1, 0, 0]
dc = [0, 0, -1, 1]

def valid(x, y):
    v = 0
    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]
        if nr < 0 or nr >= M or nc < 0 or nc >= N or box[nc][nr] == -1:
            v += 1
    if v != 4:
        return True
    return False
        
def ripen(l):
    pass
    
for row in range(N):
    for col in range(M):
        if not valid(col, row):
            days = -1
            break
        if box[col][row] == 1:
            ripe.append((col, row))
        

# while ripe:



#########

print(box)