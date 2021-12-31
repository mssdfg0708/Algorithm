def convert(s, answer):
    if s[:2] == '0b':
        s = s[2:]

    length = len(s)
    one = s.count('1')
    zero = length - one

    answer[0] += 1
    answer[1] += zero

    result = bin(one)
    return result


def solution(s):
    answer = [0, 0]
    # 예외 처리
    if s == '1':
        return answer

    while s != '0b1':
        s = convert(s, answer)
    return answer


s = "1"
solution(s)
