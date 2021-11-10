from collections import deque


MAX_POINT = 100000
start, target = map(int, input().split())
visited = [False for _ in range(MAX_POINT + 1)]

q = deque([[start, 0]])
while q:
    location, time = q.popleft()
    visited[location] = True
    if location == target:
        print(time)
        break

    next_location = location + 1
    if 0 <= next_location <= MAX_POINT and not visited[next_location]:
        q.append([next_location, time + 1])

    next_location = location - 1
    if 0 <= next_location <= MAX_POINT and not visited[next_location]:
        q.append([next_location, time + 1])

    next_location = location * 2
    if 0 <= next_location <= MAX_POINT and not visited[next_location]:
        q.append([next_location, time + 1])
