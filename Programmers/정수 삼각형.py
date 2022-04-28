def solution(triangle):
    dp = []
    for row in triangle:
        length = len(row)
        dp.append([0 for _ in range(length)])

    dp[0][0] = triangle[0][0]
    for level in range(1, len(triangle)):
        for index in range(level+1):
            if index > 0:
                dp[level][index] = triangle[level][index] + dp[level-1][index-1]
            if index < level:
                dp[level][index] = max(dp[level][index], triangle[level][index] + dp[level-1][index])

    dp_length = len(dp)
    answer = max(dp[dp_length-1])

    return answer


input_triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(input_triangle))


# dp_table 을 사용한 최댓값 계산
# 7
# 10 15
# 18 16 15
# 20 25 20 19
# 24 30 27 26 24

# index 경계값 확인도 필요
