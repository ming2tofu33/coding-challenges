# 5656 "비교 연산자"

import sys
input = sys.stdin.readline

c = 1

while True:
    a, e, b = input().split()
    a = int(a)
    b = int(b)
    if e == '>':
        answer = 'true' if a > b else 'false'
    elif e == '<':
        answer = 'true' if a < b else 'false'
    elif e == '>=':
        answer = 'true' if a >= b else 'false'
    elif e == '<=':
        answer = 'true' if a <= b else 'false'
    elif e == '==':
        answer = 'true' if a == b else 'false'
    elif e == '!=':
        answer = 'true' if a != b else 'false'
    else:
        sys.exit()
    
    print(f"Case {c}: {answer}")
    c += 1