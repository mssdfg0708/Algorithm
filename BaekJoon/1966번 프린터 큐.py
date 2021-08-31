from collections import deque

test_set = int(input())
queue = deque()
checklist = deque()
for _ in range(test_set):
    # 입력 받기
    count = 0
    queue.clear()
    checklist.clear()
    max_num, num = map(int, input().split())
    array = [i for i in input().split()]
    for i in range(len(array)):
        if i == num:
            queue.append(array[i])
            checklist.append(True)
        else:
            queue.append(array[i])
            checklist.append(False)
    # 알고리즘
    while queue:
        priority = queue.popleft()
        max_priority = priority
        target = checklist.popleft()
        for item in queue:
            max_priority = max(max_priority, item)
        if max_priority == priority:
            count += 1
            if target:
                print(count)
                break
        else:
            queue.append(priority)
            checklist.append(target)
