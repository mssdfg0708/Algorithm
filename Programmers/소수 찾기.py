from itertools import permutations
import math


# 소수 판별 함수
def is_prime_number(x):
    # 0, 1 은 소수가 아니다
    if x == 1 or x == 0:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어지는지 확인
        if x % i == 0:
            return False
    return True


def solution(numbers):
    prime_number_candidates = []
    for sub_len in range(1, len(numbers)+1):
        candidates = list(permutations(numbers, sub_len))
        for candidate in candidates:
            num = ''
            for item in candidate:
                num += item
            prime_number_candidates.append(int(num))

    prime_number_candidates = list(set(prime_number_candidates))

    answer = 0
    for num in prime_number_candidates:
        if is_prime_number(num):
            answer += 1

    return answer


numbers = "011"
print(solution(numbers))
