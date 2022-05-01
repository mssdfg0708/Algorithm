def rotate_key(key, lock):
    next_key = [[-1 for _ in range(len(key))] for _ in range(len(key))]
    for x in range(len(key)):
        for y in range(len(key)):
            next_key[y][len(key) - 1 - x] = key[x][y]

    return next_key


def check_key(offset_x, offset_y, key, board, count):
    check_count = 0
    for x in range(len(key)):
        for y in range(len(key)):
            board_x = x + offset_x
            board_y = y + offset_y
            if board[board_x][board_y] == 1 and key[x][y] == 1:
                return False
            if board[board_x][board_y] == 0 and key[x][y] == 1:
                check_count += 1

    if check_count == count:
        return True
    else:
        return False


def solution(key, lock):
    answer = False
    count = 0
    k = len(key) * 2 + len(lock)
    board = [[-1 for _ in range(k)] for _ in range(k)]

    for x in range(len(lock)):
        for y in range(len(lock)):
            board[x + len(key)][y + len(key)] = lock[x][y]
            if lock[x][y] == 0:
                count += 1

    for _ in range(4):
        key = rotate_key(key, lock)
        for x in range(len(board)-len(key)):
            for y in range(len(board)-len(key)):
                if check_key(x, y, key, board, count):
                    answer = True

    return answer


input_key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
input_lock = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 1, 1]]
print(solution(input_key, input_lock))
