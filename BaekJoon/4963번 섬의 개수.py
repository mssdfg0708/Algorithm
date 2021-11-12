from collections import deque
# 섬 = 0 / 바다 = 1
# 섬과 바다의 정보가 입력된 graph[][] / 크기 h X w
# 방문 여부가 입력된 visited[]
# BFS 를 이용하여 구현


def bfs(root_x, root_y):
    w, h = len(graph[0]), len(graph)
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
# BFS Module ========================================
    q = deque([[root_x, root_y]])
    visited[root_x][root_y] = True
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h:
                continue
            if ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 0 or visited[nx][ny]:
                continue
            q.append([nx, ny])
            visited[nx][ny] = True
# BFS Module ========================================


while True:
    w, h = map(int, input().split())
    result = 0
    # 종료 조건
    if w == 0 and h == 0:
        break

    visited = []
    for _ in range(h):
        visited.append([False for _ in range(w)])

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1 and not visited[x][y]:
                result += 1
                bfs(x, y)

    print(result)
