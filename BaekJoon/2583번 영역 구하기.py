from collections import deque


def bfs(graph, X, Y, M, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    area = 0
    q = deque()
    q.append([X, Y])
    area += 1
    graph[X][Y] = True
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= M:
                continue
            if ny < 0 or ny >= N:
                continue
            if graph[nx][ny]:
                continue
            q.append([nx, ny])
            area += 1
            graph[nx][ny] = True

    return area


M, N, K = map(int, input().split())
graph = [[False for _ in range(N)] for _ in range(M)]

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = True

count = 0
area_list = []

for x in range(M):
    for y in range(N):
        if not graph[x][y]:
            count += 1
            area = bfs(graph, x, y, M, N)
            area_list.append(area)

area_list.sort()
answer = ""
for item in area_list:
    answer += str(item) + " "

print(count)
print(answer)
