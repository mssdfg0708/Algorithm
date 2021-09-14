n, m = map(int, input().split())
board = []
result_list = []

for _ in range(n):
    board.append(input())

start_with_black = [['C' for _ in range(8)] for _ in range(8)]
start_with_white = [['C' for _ in range(8)] for _ in range(8)]

def check_element(init_i, init_j):
    result_black, result_white = 0, 0
    for i in range(init_i, init_i + 8):
        for j in range(init_j, init_j + 8):
            if board[i][j] != start_with_black[i-init_i][j-init_j]:
                result_black += 1
            if board[i][j] != start_with_white[i-init_i][j-init_j]:
                result_white += 1
    result_list.append(result_black)
    result_list.append(result_white)


for i in range(8):
    for j in range(8):
        if i == 0 and j == 0:
            start_with_black[i][j] = 'B'
            continue
        if i == 1 and j == 0:
            start_with_black[i][j] = 'W'
            continue
        if j == 0:
            start_with_black[i][j] = start_with_black[i - 2][j]
            continue
        if start_with_black[i][j - 1] == 'B':
            start_with_black[i][j] = 'W'
        else:
            start_with_black[i][j] = 'B'

for i in range(8):
    for j in range(8):
        if i == 0 and j == 0:
            start_with_white[i][j] = 'W'
            continue
        if i == 1 and j == 0:
            start_with_white[i][j] = 'B'
            continue
        if j == 0:
            start_with_white[i][j] = start_with_white[i - 2][j]
            continue
        if start_with_white[i][j - 1] == 'W':
            start_with_white[i][j] = 'B'
        else:
            start_with_white[i][j] = 'W'

for init_i in range(n-7):
    for init_j in range(m-7):
        check_element(init_i, init_j)
print(min(result_list))
