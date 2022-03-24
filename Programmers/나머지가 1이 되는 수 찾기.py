def solution(n):
    answer = -1
    for num in range(1, n+2):
        if n % num == 1:
            answer = num
            break

    return answer


input_n = 10
print(solution(input_n))
