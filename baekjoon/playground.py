import sys

n = int(sys.stdin.readline())
s1 = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
s2 = set(l)

dif = s2 - s1

print('\n'.join(['0' if i in dif else '1' for i in l]))