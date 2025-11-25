# 10816 "숫자 카드 2"

from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
hold = list(map(int, input().split()))

cnt = Counter(cards)

for i in hold:
    print(cnt.get(i, 0), end=' ')