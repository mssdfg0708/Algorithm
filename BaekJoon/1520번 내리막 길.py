import sys

sys.setrecursionlimit(10 ** 9)


def dfs(x, y):
    if x == X-1 and y == Y-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= X:
            continue
        if ny < 0 or ny >= Y:
            continue
        if graph[x][y] <= graph[nx][ny]:
            continue
        dp[x][y] += dfs(nx, ny)

    return dp[x][y]


X, Y = map(int, sys.stdin.readline().split())
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
dp = [[-1 for _ in range(Y)] for _ in range(X)]
graph = []
for _ in range(X):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)

answer = dfs(0, 0)
print(answer)
