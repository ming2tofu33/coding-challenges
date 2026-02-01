# 20920 "영단어 암기는 괴로워"

import sys
input = sys.stdin.readline

d = {}
n, m = map(int, input().split())

for _ in range(n):
    w = input().rstrip()
    if len(w) >= m:
        d[w] = d.get(w, 0) + 1

s = []
for word, cnt in d.items():
    s.append((cnt, word))

s.sort(key=lambda x: (-x[0], -len(x[1]), x[1]))

print('\n'.join([word for _, word in s]))