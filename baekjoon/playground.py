import sys

lines = sys.stdin.read().splitlines()
for line in lines:
    a, b = map(int, line.split())
    print(a + b)