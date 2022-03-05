info = input()
board = []
for item in info:
    board.append(item)

for start in range(len(board)):
    if board[start] != 'X':
        continue
    if board[start:start+4] == ['X', 'X', 'X', 'X']:
        for offset in range(4):
            board[start+offset] = 'A'
            continue
    if board[start:start+2] == ['X', 'X']:
        for offset in range(2):
            board[start+offset] = 'B'

if 'X' in board:
    print(-1)
else:
    print(''.join(board))
