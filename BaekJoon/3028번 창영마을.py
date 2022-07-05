import sys

temp = sys.stdin.readline().strip()
board = [1, 0, 0]

for index in range(len(temp)):
    if temp[index] == 'A':
        board[0], board[1] = board[1], board[0]
        continue
    if temp[index] == 'B':
        board[1], board[2] = board[2], board[1]
        continue
    board[0], board[2] = board[2], board[0]

for index in range(len(board)):
    if board[index] == 1:
        print(index + 1)
