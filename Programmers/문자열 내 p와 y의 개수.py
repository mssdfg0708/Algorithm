def solution(s):
    s = s.lower()
    count_p = s.count('p')
    count_y = s.count('y')

    return count_p == count_y


input_s = "pPoooyY"
print(solution(input_s))
