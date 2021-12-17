import math


def solution(brown, yellow):
    total = brown + yellow
    divisors = []
    limit = int(math.sqrt(total))+1
    for num in range(3, limit):
        if total % num == 0:
            divisors.append(num)

    for height in divisors:
        length = total//height
        brown_candidate = ((length-1) * 2) + ((height-1) * 2)
        yellow_candidate = total - brown_candidate
        if brown == brown_candidate and yellow == yellow_candidate:
            answer = [length, height]
            return answer


brown, yellow = 24, 24
print(solution(brown, yellow))

# row * col = brown + yellow = total
# total 의 약수를 모두 구해서 모든 경우의 수 탐색
