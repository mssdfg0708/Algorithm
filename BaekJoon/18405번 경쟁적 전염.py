import sys
from collections import deque

# n 가로 세로 길이 k 바이러스 수 s 시간 x 좌표 y 좌표
n, k = map(int, sys.stdin.readline().split())
board = list()

# 정보 입력
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
final_s, final_x, final_y = map(int, sys.stdin.readline().split())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 모듈
queue = []
for x in range(n):
    for y in range(n):
        if board[x][y]:
            queue.append([board[x][y], 0, x, y])

queue.sort()
queue = deque(queue)
while queue:
    kind_of_virus, s, x, y = queue.popleft()
    if s == final_s:
        break
    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        if temp_y < 0 or temp_x < 0 or temp_y >= n or temp_x >= n:
            continue
        if board[temp_x][temp_y]:
            continue
        board[temp_x][temp_y] = kind_of_virus
        queue.append([kind_of_virus, s + 1, temp_x, temp_y])
print(board[final_x - 1][final_y - 1])
