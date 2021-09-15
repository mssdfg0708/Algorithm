# 처음 해결한 풀이
def sol1():
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


# 개선된 풀이
def sol2():
    n, m = map(int, input().split())
    board = []
    result_list = []

    # board 값 입력
    for _ in range(n):
        board.append(input())

    # 타일의 Black or White 판별
    def check_element(start_i, start_j):
        start_black = 0
        start_white = 0
        for i in range(start_i, start_i + 8):
            for j in range(start_j, start_j + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'B':
                        start_black += 1
                    if board[i][j] != 'W':
                        start_white += 1
                else:
                    if board[i][j] != 'W':
                        start_black += 1
                    if board[i][j] != 'B':
                        start_white += 1

        result_list.append(start_white)
        result_list.append(start_black)

    # start_i, start_j = 시작점
    for start_i in range(n-7):
        for start_j in range(m-7):
            # 시작점을 기준으로 8X8 크기 만큼 탐색
            check_element(start_i, start_j)
    print(min(result_list))
