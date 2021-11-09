# 1 열만 존재 하는 경우 = 1
# 2 열만 존재 하는 경우 / 3 행 이상인 경우 = 2 / 3행 미만인 경우 = 1
# 3 열만 존재 하는 경우 / 3 행 이상인 경우 = 3 / 2행인 경우 = 2 / 1행인 경우 = 1
# 4 열만 존재 하는 경우 / 1 행인 경우 = 1 / 2 행인 경우 = 2 / 3 행 이상인 경우 = 4
# 5 열만 존재 하는 경우 / 1 행인 경우 = 1 / 2 행인 경우 = 3 / 3 행 이상인 경우 = 4
# 6 열만 존재 하는 경우 동일
# 7 열만 존재 하는 경우 1행인 경우  1 / 2 행인 경우 = 4 / 3행 이상인 경우 = 5

# 7열 초과인 경우 / 1행인 경우 = 1 / 2행인 경우 = 4 / 3행 이상인 경우 5 + (열 길이 - 7)

# n = 가로 / m = 세로
def solution():
    n, m = map(int, input().split())
    if n == 1:
        return 1
    if m == 1:
        return 1
    if m == 2 and n < 3:
        return 1
    if m == 2 and n >= 3:
        return 2
    if m == 3 and n == 2:
        return 2
    if m == 3 and n >= 3:
        return 3
    if m == 4 and n == 2:
        return 2
    if m == 4 and n >= 3:
        return 4
    if m == 5 and n == 2:
        return 3
    if m == 5 and n >= 3:
        return 4
    if m == 6 and n == 2:
        return 3
    if m == 6 and n >= 3:
        return 4
    if m >= 7 and n == 2:
        return 4
    return m-2


print(solution())
