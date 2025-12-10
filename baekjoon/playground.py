# 10409 "서버"

n, T = map(int, input().split())
l = list(map(int, input().split()))
time = 0

for i, t in enumerate(l, start=1):
    time += t
    if time > T:
        i -= 1
        break

print(i)