def check_matched_block(board, matched, x, y):
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    match = 0
    for d in range(3):
        nx = x + dx[d]
        ny = y + dy[d]
        if board[nx][ny] == board[x][y]:
            match += 1
    if match >= 3:
        matched.append([x, y])
        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]
            matched.append([nx, ny])


def change_block_index(board, m, n):
    for y in range(n):
        for x in range(m - 2, -1, -1):
            if board[x][y] == "0":
                continue
            while x + 1 < m and board[x + 1][y] == "0":
                board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
                x += 1


def solution(m, n, string):

    board = [[0 for _ in range(n)] for _ in range(m)]
    for x in range(len(string)):
        for y in range(len(string[0])):
            board[x][y] = string[x][y]

    # matched 블록이 없을때까지 반복
    while True:
        matched = []
        for x in range(m-1):
            for y in range(n-1):
                if board[x][y] == "0":
                    continue
                # 각 블록 matched 여부 확인
                check_matched_block(board, matched, x, y)

        # 종료 조건 확인
        if not matched:
            break
        # matched 블록 지우기
        for x, y in matched:
            board[x][y] = "0"
        # 블록 아래로 당기기
        change_block_index(board, m, n)

    # 지워진 블록 개수 확인
    answer = 0
    for row in board:
        for item in row:
            if item == "0":
                answer += 1
    # 지워진 블록 개수 출력
    return answer


m, n = 4, 5
string = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
solution(m, n, string)

# matched = [] 에 각 board 상태에서 지워지는 [x, y] 값 저장
# 지워지는 부분은 "0" 로 변경
# "0"이 아닌 모든 블록에 대해서 바로 아래 블록을 확인
# 아래 블록이 "0"이 아닐때 까지 [x, y] 좌표에서 x+=1 실행
# matched 의 길이가 0 일때까지 반복
# 결과 "0" 개수 출력
