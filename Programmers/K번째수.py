def solution(array, commands):
    answer = []
    for command in commands:
        string = array[command[0] - 1: command[1]]
        string.sort()
        answer.append(string[command[2] - 1])

    return answer
