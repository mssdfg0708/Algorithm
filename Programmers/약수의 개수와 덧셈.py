import math


def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        identifier = math.floor(math.sqrt(num))

        if identifier ** 2 == num:
            answer -= num
        else:
            answer += num

    return answer


input_left = 13
input_right = 17
print(solution(input_left, input_right))
