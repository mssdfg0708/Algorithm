def solution(dartResult):
    scores = []

    buffer = ''
    for dart in dartResult:
        if dart.isdigit():
            buffer += dart
            continue

        if buffer:
            scores.append(int(buffer))
            buffer = ''

        if dart == 'S':
            continue
        if dart == 'D':
            scores[-1] = scores[-1] ** 2
            continue
        if dart == 'T':
            scores[-1] = scores[-1] ** 3
            continue
        if dart == '*':
            scores[-1] = scores[-1] * 2
            if len(scores) >= 2:
                scores[-2] = scores[-2] * 2
            continue
        if dart == '#':
            scores[-1] = scores[-1] * -1
            continue

    answer = 0
    for score in scores:
        answer += score

    return answer


dartResult = '1D2S#10S'
solution(dartResult)
