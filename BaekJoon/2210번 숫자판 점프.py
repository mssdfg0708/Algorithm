board = []
answer = set()
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(5):
    row = list(input().split())
    board.append(row)


def dfs(x, y, item):
    if len(item) == 6:
        answer.add(item)
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= 5:
            continue
        if ny < 0 or ny >= 5:
            continue
        dfs(nx, ny, item + board[nx][ny])


for x in range(5):
    for y in range(5):
        dfs(x, y, board[x][y])

print(len(answer))
