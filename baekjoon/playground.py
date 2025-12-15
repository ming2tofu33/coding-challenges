# 1406 "에디터"

from collections import deque
import sys
input = sys.stdin.readline

left = deque(input().rstrip())
right = deque()
n = int(input())

for _ in range(n):
    cmd = input().rstrip()
    if cmd[0] == 'P':
        left.append(cmd[2])
    elif cmd[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.popleft())
    elif cmd[0] == 'B':
        if left:
            left.pop()

print(''.join(left) + ''.join(right))