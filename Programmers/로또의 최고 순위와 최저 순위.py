def solution(lottos, win_nums):
    zero_num = lottos.count(0)
    match = 0

    for item in lottos:
        if item in win_nums:
            match += 1

    min_val = 7 - match
    if min_val > 6:
        min_val = 6

    max_val = 7 - (match + zero_num)
    if max_val > 6:
        max_val = 6

    answer = [max_val, min_val]
    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
solution(lottos, win_nums)
