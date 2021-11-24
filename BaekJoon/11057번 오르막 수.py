# n = 1 / dp[0] = 1 dp[1] = 1 ... dp[9] = 1

# n = 2 / dp[0] = dp[0]
#           dp[1] = dp[0] + dp[1]
#           dp[9] = dp[0] + ... dp[9]

# n = 3 / dp[0] = dp[0]
#           dp[1] = dp[0] + dp[1]
#           dp[9] = dp[0] + ... dp[9]

n = int(input())
dp = []
for _ in range(10):
    dp.append(1)

for num in range(2, n+1):
    sub_dp = [0 for _ in range(10)]
    for threshold in range(len(dp)):
        sub_sum = 0
        for index in range(threshold+1):
            sub_sum += dp[index]
        sub_dp[threshold] = sub_sum

    for index in range(len(sub_dp)):
        dp[index] = sub_dp[index]

result = 0
for item in dp:
    result += item

print(result % 10007)
