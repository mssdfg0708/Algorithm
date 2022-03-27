def solution(s):
    length = len(s)

    answer = ''
    if length % 2 == 0:
        answer = s[length // 2 - 1: length // 2 + 1]
    if length % 2 == 1:
        answer = s[length // 2]

    return answer


input_s = "qwer"
solution(input_s)
