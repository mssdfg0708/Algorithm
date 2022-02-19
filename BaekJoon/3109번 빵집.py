import sys


def dfs(x, y):
    graph[x][y] = 'x'

    if y >= M - 1:
        answer[0] += 1
        return True

    for d in range(3):
        nx = x + dx[d]
        ny = y + 1
        if nx < 0 or nx >= N:
            continue
        if ny < 0 or ny >= M:
            continue
        if graph[nx][ny] == 'x':
            continue

        if dfs(nx, ny):
            return True


N, M = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1]
graph = [[]for _ in range(N)]

for row in range(N):
    line = sys.stdin.readline().strip()
    for item in line:
        graph[row].append(item)

answer = [0]
for x in range(N):
    dfs(x, 0)

print(answer[0])
