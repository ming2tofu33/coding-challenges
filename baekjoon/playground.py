import sys

n = int(sys.stdin.readline())
age_name = [sys.stdin.readline().split() for _ in range(n)]

age_name.sort(key=lambda x: (int(x[0])))

sys.stdout.write('\n'.join(f'{x} {y}' for x, y in age_name))