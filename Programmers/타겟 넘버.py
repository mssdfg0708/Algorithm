# BFS 사용
# numbers[i] 에 + 와 - 를 대입하며 BFS 진행

from collections import deque


def solution(numbers, target):
    BREAK_POINT = len(numbers) - 1
# BFS Module ========================================
    q = deque()
    q.append([numbers[0], 0])
    q.append([-numbers[0], 0])
    while q:
        element, index = q.popleft()
        if index >= BREAK_POINT:
            q.append([element, index])
            break
        q.append([element + numbers[index+1], index+1])
        q.append([element - numbers[index+1], index+1])
# BFS Module ========================================

    answer = 0
    for element, index in q:
        if element == target:
            answer += 1

    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
