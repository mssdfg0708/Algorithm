from collections import deque
import math


def is_prime_number(x):
    x = int(x)
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    # 진법 변환
    q = deque()
    while n >= k:
        q.appendleft(n % k)
        n = int(n / k)
    q.appendleft(n)

    # 소수 판별
    buffer = ""
    result = 0
    for item in q:
        if item == 0:
            if buffer and is_prime_number(buffer):
                result += 1
            buffer = ""
            continue
        buffer += str(item)

    if buffer and is_prime_number(buffer):
        result += 1

    return result


n, k = 110011, 10
solution(n, k)
