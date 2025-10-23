import sys
from collections import deque

m = int(sys.stdin.readline())
s = deque()

for _ in range(m):
    c = sys.stdin.readline()
    if c.startswith('add'):
        x = int(c.split()[1])
        if x not in s:
            s.append(x)
    elif c.startswith('remove'):
        x = int(c.split()[1])
        if x in s:
            s.remove(x)
    elif c.startswith('check'):
        x = int(c.split()[1])
        print(int(x in s))
    elif c.startswith('toggle'):
        x = int(c.split()[1])
        if x in s:
            s.remove(x)
        else:
            s.append(x)
    elif c.startswith('all'):
        s = deque(range(1, 21))
    elif c.startswith('empty'):
        s.clear()