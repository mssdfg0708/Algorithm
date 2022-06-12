import sys

nums = list(map(int, sys.stdin.readline().rstrip()))
zero = 0
one = 0

for i in range(1, len(nums)):
    if nums[i] - nums[i - 1] == 1:
        one += 1
    elif nums[i] - nums[i - 1] == -1:
        zero += 1

if one > zero:
    print(one)
else:
    print(zero)
