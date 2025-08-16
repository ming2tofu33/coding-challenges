import sys

t = int(sys.stdin.readline())

for _ in range(t):
    l = sys.stdin.readline().rstrip()
    total = 0
    score = 0
    for i in l:
        if i == 'O':
            score += 1
            total += score
        else:
            score = 0
            total += score

    print(total)