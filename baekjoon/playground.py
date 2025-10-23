import sys

m = 0

for row in range(9):
    l = list(map(int, sys.stdin.readline().split()))
    tmp = max(l)
    col = l.index(tmp)
    if m <= tmp:
        m = tmp
        r, c = row + 1, col + 1
        
print(m)
print(r, c)