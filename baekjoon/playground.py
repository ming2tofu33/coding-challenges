import sys

n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.read().split()))
l.sort()

s = set(l)

c = set()

for i in s:
    tmp = l.count(i)
    if tmp > 1:
        c = {i}
    elif tmp == max(c):
        c.add(i)

cnt = sorted(list(c))

print(n, l, '==del==')

print(round(sum(l) / n))
print(l[len(l) // 2] if len(l) % 2 else (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2)
print(cnt[-2] if len(c) > 1 else cnt[0])
print(max(l) - min(l))