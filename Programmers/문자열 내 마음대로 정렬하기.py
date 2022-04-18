def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x: x[n])

    return strings


input_strings = ["sun", "bed", "car"]
input_n = 1
print(solution(input_strings, input_n))
