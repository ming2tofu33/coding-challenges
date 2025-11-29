# 9946 "단어 퍼즐"

from collections import Counter
import sys
input = sys.stdin.readline

def game(before, after):
    before_count = Counter(before)
    after_count = Counter(after)
    
    if before_count == after_count:
        return "same"
    else:
        return "different"

num = 1

while True:
    before = input().strip()
    after = input().strip()
    
    if before == "END" and after == "END":
        break
    
    print(f'Case {num}: {game(before, after)}')
    num += 1