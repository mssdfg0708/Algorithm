n = int(input())

arr = list(map(int, input().split()))

dp = [item for item in arr]

for end in range(n):
    for start in range(end):
        if arr[end] > arr[start]:
            if dp[end] >= dp[start] + arr[end]:
                continue
            dp[end] = dp[start] + arr[end]

print(max(dp))
