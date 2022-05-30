import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    q = deque()
    visited[0][0] = 1
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


time = 0
while True:
    visited = [[0] * m for _ in range(n)]
    bfs()
    flag = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                flag = True
            elif graph[i][j] == 2:
                graph[i][j] = 1
    if flag:
        time += 1
    else:
        break

print(time)
