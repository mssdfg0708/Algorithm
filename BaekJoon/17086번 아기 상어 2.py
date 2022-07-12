from collections import deque


def bfs(root_x, root_y):
    distance = 0
    visited = [[False for _ in range(M)] for _ in range(N)]

    q = deque()
    q.append([root_x, root_y, 0])
    visited[root_x][root_y] = True
    while q:
        x, y, distance = q.popleft()
        if place[x][y] == 1:
            break

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N:
                continue
            if ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            q.append([nx, ny, distance+1])
            visited[nx][ny] = True

    return distance


N, M = map(int, input().split())
place = []
for _ in range(N):
    row = list(map(int, input().split()))
    place.append(row)

max_distance = 0
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for n in range(N):
    for m in range(M):
        local_distance = bfs(n, m)
        max_distance = max(max_distance, local_distance)

print(max_distance)
