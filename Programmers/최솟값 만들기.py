def solution(arr01, arr02):
    arr01.sort()
    arr02.sort(reverse=True)

    answer = 0
    for index in range(len(arr01)):
        temp = arr01[index] * arr02[index]
        answer += temp

    return answer


arr01 = [1, 4, 2]
arr02 = [5, 4, 4]
print(solution(arr01, arr02))
