from collections import deque

n, m = map(int, input().split())
graph = []

for x in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


paint = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            paint.append(bfs(graph, x, y))

if not paint:
    print(0)
    print(0)
else:
    print(len(paint))
    print(max(paint))
