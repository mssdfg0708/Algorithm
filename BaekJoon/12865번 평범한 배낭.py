import sys

n, max_weight = map(int, input().split())
weight_list = [0]
value_list = [0]
dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
for item in dp:
    print(item)
for _ in range(n):
    weight, value = map(int, sys.stdin.readline().split())
    weight_list.append(weight)
    value_list.append(value)

for i in range(len(weight_list)):
    weight = weight_list[i]
    value = value_list[i]
    for j in range(1, max_weight + 1):
        if j >= weight:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][max_weight])
