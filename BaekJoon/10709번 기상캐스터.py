import sys


def check_cloud(root_x, root_y):
    count = 0
    for y in range(root_y, -1, -1):
        if board[root_x][y] == 'c':
            counts[root_x][root_y] = count
            break
        count += 1


height_limit, width_limit = map(int, sys.stdin.readline().split())
counts = [[-1 for _ in range(width_limit)] for _ in range(height_limit)]
board = []
for _ in range(height_limit):
    line = sys.stdin.readline().strip()
    board_line = []
    for item in line:
        board_line.append(item)
    board.append(board_line)

for root_x in range(height_limit):
    for root_y in range(width_limit - 1, -1, -1):
        check_cloud(root_x, root_y)

for row in counts:
    for item in row:
        print(item, end=' ')
    print()
