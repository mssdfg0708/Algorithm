def solution(n):
    answer = ''
    for num in range(n):
        if num % 2 == 0:
            answer += '수'
        if num % 2 == 1:
            answer += '박'

    return answer


input_n = 3
print(solution(input_n))
