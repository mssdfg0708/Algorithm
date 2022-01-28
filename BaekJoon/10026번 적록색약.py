from collections import deque


def normal_bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append([x, y])
    visited[x][y] = True
    root = board[x][y]

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] != root:
                continue
            visited[nx][ny] = True
            q.append([nx, ny])


def other_bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append([x, y])
    visited[x][y] = True
    root = board[x][y]

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if root == 'R' and board[nx][ny] == 'B':
                continue
            if root == 'G' and board[nx][ny] == 'B':
                continue
            if root == 'B' and board[nx][ny] != root:
                continue
            visited[nx][ny] = True
            q.append([nx, ny])


n = int(input())
board = []

for _ in range(n):
    board.append(list(input()))

# 일반인
count = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            count += 1
            normal_bfs(x, y)

print(count)

# 적록색약
count = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            count += 1
            other_bfs(x, y)

print(count)

