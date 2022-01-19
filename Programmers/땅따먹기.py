# dp 활용
def solution(land):
    dp = [[] for _ in range(len(land))]
    dp[0] = land[0]

    for row in range(1, len(dp)):
        for land_col in range(4):
            # 각 col 에 올수 있는 가장 큰 값 저장
            temp = []
            for dp_col in range(4):
                if dp_col != land_col:
                    temp.append(dp[row-1][dp_col] + land[row][land_col])
            dp[row].append(max(temp))

    answer = max(dp[-1])
    return answer


land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
print(solution(land))
