def solution(numbers):
    info = []
    for num in numbers:
        info.append(str(num))

    info.sort(key=lambda x: x * 3, reverse=True)

    answer = ''
    for item in info:
        answer += item
    answer = int(answer)
    answer = str(answer)
    return answer


numbers = [0, 6, 1, 2, 1000]
print(solution(numbers))
