import math


def solution(a, b):
    if a > b:
        a, b = b, a

    answer = 0
    for num in range(a, b+1):
        answer += num

    return answer


# 시간 복잡도 최적화 버전
def solution2(a, b):
    if a > b:
        a, b = b, a

    sum_a = (a + 1) * (a // 2)
    sum_b = (b + 1) * (b // 2)

    if a % 2 == 1:
        sum_a += math.ceil(a/2)
    if b % 2 == 1:
        sum_b += math.ceil(b/2)

    answer = sum_b - sum_a + a
    return answer


input_a = 6
input_b = 6
print(solution2(input_a, input_b))
