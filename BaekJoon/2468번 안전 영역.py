from collections import deque


def bfs(root_x, root_y):
    n = len(graph)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
# BFS Module ========================================
    q = deque([[root_x, root_y]])
    graph[root_x][root_y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= n:
                continue
            if graph[nx][ny]:
                continue
            q.append([nx, ny])
            graph[nx][ny] = True
# BFS Module ========================================


# ====================== Main ======================
n = int(input())
root_graph = []
height_list = set()
height_list.add(0)
for _ in range(n):
    row = list(map(int, input().split()))
    root_graph.append(row)
    for item in row:
        height_list.add(item)

height_list = list(height_list)
result = 0
for height in height_list:
    temp = 0
    graph = []
    for _ in range(n):
        graph.append([False for _ in range(n)])

    for x in range(n):
        for y in range(n):
            if height >= root_graph[x][y]:
                graph[x][y] = True

    for x in range(n):
        for y in range(n):
            if not graph[x][y]:
                temp += 1
                bfs(x, y)

    result = max(result, temp)

print(result)
