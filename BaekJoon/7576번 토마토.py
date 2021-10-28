# 1 = 익은 토마토 / 0 = 안 익은 토마토 / -1 = 토마토가 없는 칸
# queue 에 익은 토마토의 위치 입력
# BFS 를 이용하여 알고리즘 실행

from sys import stdin
from collections import deque


def bfs(q):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # bfs 실행
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not 0 <= nx < n:
                continue
            if not 0 <= ny < m:
                continue
            if graph[nx][ny] >= 1:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])


def find_max(graph):
    result = -1
    for row in graph:
        for item in row:
            if item == 0:
                return -1
            result = max(result, item)
    return result - 1


# [n X m] 2차원 graph 입력
m, n = map(int, stdin.readline().split())
graph = []
queue = deque()
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

# 알고리즘 실행
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])
            graph[i][j] = 1
bfs(queue)
print(find_max(graph))
