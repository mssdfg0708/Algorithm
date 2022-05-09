import sys


def make_number_true(num):
    for x in range(5):
        for y in range(5):
            if bingo_board[x][y][0] == num:
                bingo_board[x][y][1] = True
                return x, y


bingo_board = [[] for _ in range(5)]
for x in range(5):
    row = map(int, sys.stdin.readline().split())
    for num in row:
        bingo_board[x].append([num, False])

number_orders = []
for _ in range(5):
    row = map(int, sys.stdin.readline().split())
    for num in row:
        number_orders.append(num)

answer = 0
bingo_counter = 0
for num in number_orders:
    answer += 1
    x, y = make_number_true(num)

    counter = 0
    for index_x in range(5):
        if bingo_board[index_x][y][1]:
            counter += 1
    if counter == 5:
        bingo_counter += 1

    counter = 0
    for index_y in range(5):
        if bingo_board[x][index_y][1]:
            counter += 1
    if counter == 5:
        bingo_counter += 1

    counter = 0
    if x == y:
        for index in range(5):
            if bingo_board[index][index][1]:
                counter += 1
        if counter == 5:
            bingo_counter += 1

    counter = 0
    if x + y == 4:
        if bingo_board[0][4][1]:
            counter += 1
        if bingo_board[1][3][1]:
            counter += 1
        if bingo_board[2][2][1]:
            counter += 1
        if bingo_board[3][1][1]:
            counter += 1
        if bingo_board[4][0][1]:
            counter += 1
        if counter == 5:
            bingo_counter += 1

    if bingo_counter >= 3:
        break

print(answer)
