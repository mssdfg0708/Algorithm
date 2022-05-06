import sys


def check_strike_ball(target):
    validate_count = 0
    validate_limit = len(answer_list)

    for query, strike_limit, ball_limit in answer_list:
        strike_count = 0
        ball_count = 0

        for idx in range(len(query)):
            if target[idx] == query[idx]:
                strike_count += 1
                continue
            if target[idx] in query:
                ball_count += 1

        if strike_count == strike_limit and ball_count == ball_limit:
            validate_count += 1

    if validate_count == validate_limit:
        return True
    else:
        return False


def make_target():
    result = 0
    for x in range(1, 10):
        for y in range(1, 10):
            if x == y:
                continue
            for z in range(1, 10):
                if x == z or y == z:
                    continue
                target[0] = str(x)
                target[1] = str(y)
                target[2] = str(z)
                if check_strike_ball(target):
                    result += 1

    return result


QUESTION = int(sys.stdin.readline().strip())

answer_list = []
for index in range(QUESTION):
    answer = list(sys.stdin.readline().split())
    answer[1] = int(answer[1])
    answer[2] = int(answer[2])
    answer_list.append(answer)

target = ['0', '0', '0']
result = make_target()
print(result)

# 최대 경우의 수 = 10 * 10 * 100 = 100000
# 으로 모든 경우의 수 탐색 가능
