import sys

t = int(sys.stdin.readline())

for _ in range(t):
    _ = int(sys.stdin.readline())
    n = list(map(int, sys.stdin.readline().split()))
    print(min(n), max(n))