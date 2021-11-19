def solution(string):
    stack = []
    for char in string:
        if not stack:
            stack.append(char)
            continue
        if stack[-1] == char:
            stack.pop()
            continue
        if stack[-1] != char:
            stack.append(char)

    print(stack)
    if stack:
        return 0
    if not stack:
        return 1


s = 'cdcd'
print(solution(s))
