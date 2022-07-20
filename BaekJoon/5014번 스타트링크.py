from collections import deque

limit, start, goal, up, down = map(int, input().split())
min_depth = [-1 for _ in range(limit)]
dx = [up, -1 * down]
start -= 1
goal -= 1

q = deque()
min_depth[start] = 0
q.append([start, 0])
while q:
    floor, depth = q.popleft()
    if floor == goal:
        break
    for d in range(2):
        next_floor = floor + dx[d]
        if next_floor < 0 or next_floor >= limit:
            continue
        if min_depth[next_floor] >= 0:
            continue
        min_depth[next_floor] = depth + 1
        q.append([next_floor, depth+1])

answer = min_depth[goal]
if answer == -1:
    print("use the stairs")
else:
    print(min_depth[goal])
