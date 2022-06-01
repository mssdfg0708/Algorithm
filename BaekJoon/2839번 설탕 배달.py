target = int(input())
INF = 9999

dp = [INF for _ in range(target+1)]
if target >= 3:
    dp[3] = 1
if target >= 5:
    dp[5] = 1
for weight in range(6, target+1):
    dp[weight] = min(dp[weight], dp[weight-3] + 1, dp[weight-5] + 1)

answer = -1
if dp[target] != INF:
    answer = dp[target]
print(answer)
