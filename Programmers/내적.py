def solution(a, b):
    answer = 0
    for i in range(len(a)):
        result = a[i] * b[i]
        answer += result

    return answer


a = [3, 5, -1]
b = [-2, 4, 8]
print(solution(a, b))
