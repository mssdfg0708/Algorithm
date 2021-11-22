n = int(input())
path = [[0 for _ in range(n)] for _ in range(n)]
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = 0
for x in range(n):
    for y in range(n):
        if x == 0 and y == 0:
            path[x][y] = 1
        if x == n-1 and y == n-1:
            result = path[x][y]
        jump = board[x][y]
        nx = x + jump
        ny = y + jump
        if nx < len(board):
            path[nx][y] += path[x][y]
        if ny < len(board):
            path[x][ny] += path[x][y]

print(result)


# 1 0 1 0
# 0 0 0 0
# 1 1 0 1
# 1 0 1 3

# 시작 지점 부터 각 부분까지의 경로 수를 차례대로 계산
# path[x][y] 만큼 진행한 부분에 숫자 더해서 입력
# 예외 처리
# 최종 결과 출력
