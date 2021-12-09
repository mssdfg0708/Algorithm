def solution(n, a, b):
    round = 0
    while a != b:
        round += 1
        # A 번호 계산
        if a % 2 == 1:
            a = a // 2 + 1
        else:
            a = a // 2
        # B 번호 계산
        if b % 2 == 1:
            b = b // 2 + 1
        else:
            b = b // 2

    return round



n, a, b = 8, 4, 7
print(solution(n, a, b))
