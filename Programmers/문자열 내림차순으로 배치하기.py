def solution(s):
    list01 = []
    for item in s:
        list01.append(item)
    list01.sort(reverse=True)

    answer = "".join(list01)
    return answer


input_s = "Zbcdefg"
print(solution(input_s))
