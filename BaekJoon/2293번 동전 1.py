# n = 동전의 종류 수
# k = 가치의 합

n, k = map(int, input().split())
dp = [0 for _ in range(k+1)]
dp[0] = 1
coins = []

for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    for total in range(1, k+1):
        # Index 확인
        if total - coin < 0:
            continue
        dp[total] += dp[total - coin]

print(dp[-1])
