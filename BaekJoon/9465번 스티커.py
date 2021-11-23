# dp[0][2] = max(dp[0][0], dp[1][0], dp[1][1]) + stickers[0][2] / dp[0][1] 제외
# dp[1][2] = max(dp[0][0], dp[1][0], dp[0][1]) + stickers[1][2] / dp[1][1] 제외
# x 값이 같고 y 값이 -1 인 경우 제외

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0 for _ in range(n)], [0 for _ in range(n)]]
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))

    # 예외 처리
    if n == 1:
        num0 = stickers[0][0]
        num1 = stickers[1][0]
        print(max(num0, num1))
        continue

    dp[0][0] = (stickers[0][0])
    dp[1][0] = (stickers[1][0])

    dp[0][1] = (stickers[1][0] + stickers[0][1])
    dp[1][1] = (stickers[0][0] + stickers[1][1])

    for y in range(2, n):
        dp[0][y] = max(dp[0][y-2], dp[1][y-2], dp[1][y-1]) + stickers[0][y]
        dp[1][y] = max(dp[0][y-2], dp[1][y-2], dp[0][y-1]) + stickers[1][y]

    print(max(dp[0][n-1], dp[1][n-1]))
