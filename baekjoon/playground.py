import sys

lines = sys.stdin.read().splitlines()

m = 0

for line in lines:
    tmp = max(map(int, (line.split())))
    col = lines.index(tmp)
    if m < tmp:
        m = tmp
        r, c = lines.index(line) + 1, col + 1
        
print(m)
print(r, c)