from collections import deque


def solution(priorities, location):
    answer = 1
    q = deque()
    for priority in priorities:
        q.append([priority])
    q[location].append('target')

    while q:
        target = q.popleft()
        max_priority = -1
        for item in q:
            max_priority = max(max_priority, item[0])

        if target[0] < max_priority:
            q.append(target)
            continue

        if len(target) == 2:
            return answer
        else:
            answer += 1


priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))


# deque 에 priority 입력
# deque[location] 의 길이를 2로 만든다
# 가장 앞의 문서를 확인하여
# 중요도가 더 높은 문서가 이외의 문서중 존재하면 deque 의 맨 뒤로 이동
# (높은 숫자가 더 높은 중요도를 가진다)
# 존재하지 않으면 popleft 이후 길이를 확인
# 인쇄 순서 출력
