def solution(s):
    s = s.lower().capitalize()

    string = [char for char in s]
    for index in range(1, len(string)):
        if string[index-1] == ' ':
            string[index] = string[index].upper()

    return "".join(string)


input_s = "3people unFollowed me"
print(solution(input_s))
