import math
from itertools import combinations


def solution(nums):
    answer = 0

    # prime number list
    MAX_NUM = 3000
    prime_number = [True for _ in range(MAX_NUM)]
    prime_number[1] = False
    for i in range(2, int(math.sqrt(MAX_NUM)) + 1):
        if prime_number[i]:
            for j in range(2, MAX_NUM):
                if i * j >= MAX_NUM:
                    break
                prime_number[i * j] = False

    # Algorithm
    candidates = list(combinations(nums, 3))
    for candidate in candidates:
        result = 0
        for item in candidate:
            result += item
        if prime_number[result]:
            answer += 1

    return answer


nums = [1, 2, 7, 6, 4]
print(solution(nums))
