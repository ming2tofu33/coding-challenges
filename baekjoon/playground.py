# 11659 "구간 합 구하기 4"

import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

acc_nums = [0]

for num in nums:
    acc_nums.append(acc_nums[-1] + num)
    
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    sys.stdout.write(f"{acc_nums[j] - acc_nums[i - 1]} \n")