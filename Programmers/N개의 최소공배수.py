def parse_num(target):
    parses = []
    for num in range(2, 101):
        while target % num == 0:
            target = target // num
            parses.append(num)
    return parses


def solution(arr):
    parse_list = []
    for target in arr:
        parses = parse_num(target)
        parse_list.append(parses)

    count_parse = dict()
    for parses in parse_list:
        for num in parses:
            if num not in count_parse:
                count_parse[num] = parses.count(num)
            else:
                count_parse[num] = max(parses.count(num), count_parse[num])

    answer = 1
    for key, value in count_parse.items():
        temp = key ** value
        answer *= temp

    return answer


input_arr = [2, 6, 8, 14]
print(solution(input_arr))
