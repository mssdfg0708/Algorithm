def solution(s):
    # answer = 0
    # return answer
    answer = ""
    digit_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
                  "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    buffer = ""

    for item in s:
        if item.isdigit():
            answer += item
            continue
        if item.isalpha():
            buffer += item
        if buffer in digit_dict:
            number = str(digit_dict[buffer])
            answer += number
            buffer = ""

    return int(answer)
