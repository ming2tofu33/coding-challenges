# 28279 "덱 2"

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque()
out = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == '1':
        d.appendleft(int(cmd[1]))
    elif cmd[0] == '2':
        d.append(int(cmd[1]))
    elif cmd[0] == '3':
        out.append(str(d.popleft() if d else -1))
    elif cmd[0] == '4':
        out.append(str(d.pop() if d else -1))
    elif cmd[0] == '5':
        out.append(str(len(d)))
    elif cmd[0] == '6':
        out.append('0' if d else '1')
    elif cmd[0] == '7':
        out.append(str(d[0] if d else -1))
    elif cmd[0] == '8':
        out.append(str(d[-1] if d else -1))
        
sys.stdout.write("\n".join(out))