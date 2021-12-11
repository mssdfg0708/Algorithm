from collections import deque


def check_pair(q, stack):
    for item in q:
        if not stack:
            stack.append(item)
            continue
        if stack[-1] == '[' and item == ']':
            stack.pop()
        elif stack[-1] == '{' and item == '}':
            stack.pop()
        elif stack[-1] == '(' and item == ')':
            stack.pop()
        else:
            stack.append(item)


def solution(s):
    answer = 0
    q = deque()
    for item in s:
        q.append(item)
    # q 길이만큼 반복 하며 왼쪽으로 회전
    for _ in range(len(q)):
        item = q.popleft()
        q.append(item)
        # stack 을 이용한 괄호 확인
        stack = []
        check_pair(q, stack)
        # stack 이 비어있으면 answer += 1
        if not stack:
            answer += 1

    return answer


s = "[](){}"
solution(s)
