import sys

k = int(sys.stdin.readline())
stack = []

for _ in range(k):
    x = int(sys.stdin.readline())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)
        
print(sum(stack))