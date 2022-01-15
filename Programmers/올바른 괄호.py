def solution(string):
    stack = []
    for char in string:
        if not stack:
            stack.append(char)
            continue
        if char == '(':
            stack.append(char)
            continue
        if char == ')' and stack[-1] == '(':
            stack.pop()

    if stack:
        return False
    if not stack:
        return True


s = ")()("
print(solution(s))
