def solution(s):
    result = False
    if s.isdigit():
        if len(s) == 4 or len(s) == 6:
            result = True

    return result


input_s = "a234"
print(solution(input_s))
