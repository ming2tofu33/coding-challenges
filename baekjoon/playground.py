import sys

n = int(sys.stdin.readline())
pts = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
pts.sort()

sys.stdout.write('\n'.join(f'{x} {y}' for x, y in pts))