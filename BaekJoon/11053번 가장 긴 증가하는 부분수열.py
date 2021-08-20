import sys

n = int(input())
array = list(map(int, sys.stdin.readline().split()))
dp = [0] * n

def subSequence():
    dp[0] = 1
    for i in range(1, n):
        max_value = 0
        for j in range(i):
            if array[i] > array[j]:
                max_value = max(max_value, dp[j])
        dp[i] = max_value + 1

subSequence()
print(max(dp))
