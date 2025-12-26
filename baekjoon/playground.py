# 10820 "문자열 분석"

import sys

lines = sys.stdin.read().splitlines()

for line in lines:
    lowercase = 0
    uppercase = 0
    numeric = 0
    space = 0
    for ch in line:
        if ch.islower():
            lowercase +=1
        elif ch.isupper():
            uppercase += 1
        elif ch.isnumeric():
            numeric += 1
        elif ch == ' ':
            space += 1
    print(lowercase, uppercase, numeric, space)