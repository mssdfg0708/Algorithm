def solution(prices):
    answer = [None for _ in range(len(prices))]

    # 가격이 떨어지지 않은 기간 확인
    stack = []
    for index in range(len(prices)):
        while stack and stack[-1][0] > prices[index]:
            num, p = stack.pop()
            answer[p] = index - p
        stack.append([prices[index], index])

    # 마지막까지 가격이 떨어지지 않은 경우
    for num, index in stack:
        answer[index] = len(prices) - index - 1

    return answer


prices = [1, 2, 3, 4, 5, 2, 1]
print(solution(prices))
