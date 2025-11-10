# 11399 "ATM"

n = int(input())
p = list(map(int, input().split()))

p.sort()
t = [0]

for i in p:
    t.append(t[-1] + i)

print(sum(t[1:]))