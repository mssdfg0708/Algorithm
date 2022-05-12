N = int(input())
target = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

d = 3
point = [N // 2, N // 2]

answer = [0, 0]
for num in range(1, N ** 2 + 1):
    x, y = point
    board[x][y] = num
    if num == target:
        answer = [x, y]

    if board[x][y] == N ** 2:
        break

    nd = (d+1) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if board[nx][ny] == 0:
        d = nd
        point = [nx, ny]
        continue

    nx = x + dx[d]
    ny = y + dy[d]
    point = [nx, ny]

for row in board:
    data = ""
    for item in row:
        data += str(item) + " "
    print(data)

print(answer[0]+1, answer[1]+1)
