# 1 / 1
# 2 / 1+1 2
# 3 / 1+1+1 1+2 2+1 3
# 4 / 1+1+1+1 2+1+1 1+2+1 1+1+2 3+1 1+3 2+2

# dp 테이블 입력
t = int(input())
dp = [0, 1, 2, 4]
for i in range(4, 11):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

# 결과 출력
for _ in range(t):
    n = int(input())
    print(dp[n])
