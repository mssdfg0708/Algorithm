from collections import deque


def check_left(queue, num):
    q = deque()
    for item in queue:
        q.append(item)
    result = 0
    while q[0] != num:
        result += 1
        x = q.popleft()
        q.append(x)
    return result


def check_right(queue, num):
    q = deque()
    for item in queue:
        q.append(item)
    result = 0
    while q[0] != num:
        result += 1
        x = q.pop()
        q.appendleft(x)
    return result


def move_left(q, num):
    while q[0] != num:
        x = q.pop()
        q.appendleft(x)


def move_right(q, num):
    while q[0] != num:
        x = q.popleft()
        q.append(x)


n, m = map(int, input().split())
queue = deque()
for item in range(1, n+1):
    queue.append(item)
numbers = list(map(int, input().split()))
numbers.reverse()
result = 0

while numbers:
    target_num = numbers.pop()
    left = check_left(queue, target_num)
    right = check_right(queue, target_num)
    if left >= right:
        move_right(queue, target_num)
        queue.popleft()
        result += right
    else:
        move_left(queue, target_num)
        queue.popleft()
        result += left

print(result)
