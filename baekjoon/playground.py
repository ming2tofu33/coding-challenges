# 18258 "큐 2"

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
out = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        q.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        out.append(str(q.popleft() if q else -1))
    elif cmd[0] == 'size':
        out.append(str(len(q)))
    elif cmd[0] == 'empty':
        out.append('0' if q else '1')
    elif cmd[0] == 'front':
        out.append(str(q[0] if q else -1))
    elif cmd[0] == 'back':
        out.append(str(q[-1] if q else -1))

sys.stdout.write("\n".join(out))