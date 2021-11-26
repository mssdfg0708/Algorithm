n = int(input())
dp = [987654321 for _ in range(100001)]
dp[0] = 0
dp[1] = 1

for num in range(2, n+1):
    for square_root in range(1, num):
        square = square_root * square_root
        if num - square < 0:
            break
        dp[num] = min(dp[num], dp[num - square] + 1)

print(dp[n])
