# 연산 가능한 경우의 수
# N = 5
# dp[1] = 5
# dp[2] = [55]
# dp[2] = [5*5, 5-5, int(5/5), 5+5] = [55, 25, 0, 1, 10]

# dp[3] = [555]
# dp[2] +-*/ dp[1]
# dp[1] +-*/ dp[2]

# dp[4] = [5555]
# dp[3] dp[1]
# dp[2] dp[2]
# dp[1] dp[2]
# dp[1] dp[1] dp[2] 는 dp[2] dp[2] 에 모두 포함 된다

# 초기값
# dp[i] = [dp[i-1][0] * 10 + n]

def solution(n, number):
    dp = [[]for _ in range(9)]
    dp[1] = [n]

    # 예외 처리
    if n == number:
        return 1

    for index in range(2, 9):
        dp[index] = [dp[index-1][0] * 10 + n]

        right = index - 1
        left = 1
        while right > 0:
            for item_r in dp[right]:
                for item_l in dp[left]:
                    dp[index].append(item_l + item_r)
                    dp[index].append(item_l - item_r)
                    dp[index].append(item_l * item_r)
                    if item_r > 0:
                        dp[index].append(item_l // item_r)
            # dp[index] 가 number 를 가지고 있는지 확인
            if number in dp[index]:
                return index
            # 가지고 있지 않다면 계속 진행
            right -= 1
            left += 1
    # 탐색 실패
    return -1


n = 5
number = 12
print(solution(n, number))
