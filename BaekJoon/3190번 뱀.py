# 이동정보 저장
# 머리의 궤적을 Queue 에 입력 하여 추적
# 사과를 먹으면 append 만 실행 먹지 못하면 append 와 popleft 실행
# 매 초 마다 이동방향으로 뱀을 이동
# ------------------------------------------------------------
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# ------------------------------------------------------------
# 만약 머리 가 벽에 부딪히거나 몸과 겹치게 되면 게임 종료
# 0 빈타일  / 1 사과
# L 왼쪽 / D 오른쪽

import sys
from collections import deque


def check_head(h, s, n):
    if h[0] < 0 or h[0] >= n:
        return True
    if h[1] < 0 or h[1] >= n:
        return True
    if h in s:
        return True
    return False


def check_apple(graph, head):
    if graph[head[0]][head[1]] == 1:
        graph[head[0]][head[1]] = 0
        return True
    return False


def move_snake(snake, cur_dir):
    for i in range(len(snake)):
        snake[i][0] += dx[cur_dir]
        snake[i][1] += dy[cur_dir]


def change_direction(cur_dir):
    next_time, next_dir = next_move.pop()
    if cur_dir == UP:
        if next_dir == 'L':
            cur_dir = LEFT
        if next_dir == 'D':
            cur_dir = RIGHT
    elif cur_dir == DOWN:
        if next_dir == 'L':
            cur_dir = RIGHT
        if next_dir == 'D':
            cur_dir = LEFT
    elif cur_dir == LEFT:
        if next_dir == 'L':
            cur_dir = DOWN
        if next_dir == 'D':
            cur_dir = UP
    elif cur_dir == RIGHT:
        if next_dir == 'L':
            cur_dir = UP
        if next_dir == 'D':
            cur_dir = DOWN
    return cur_dir


# 상, 하, 좌, 우
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# graph 정보 입력
n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
k = int(input())
for _ in range(k):
    apple = list(map(int, sys.stdin.readline().split()))
    graph[apple[0]-1][apple[1]-1] = 1

# 방향 전환 정보 입력
p = int(input())
d = []
for _ in range(p):
    time, direction = sys.stdin.readline().split()
    time = int(time)
    d.append([time, direction])
d.reverse()

# 뱀 정보 저장
head = [0, 0]
snake = deque([[0, 0]])
cur_dir = RIGHT

# 시간 진행
timer = 0
# next_dir = [time, direction]
next_move = []
next_time = 987654321
while True:
    if not next_move and d:
        next_move.append(d.pop())
        next_time = next_move[0][0]
    timer += 1
    # 머리 이동
    head[0] += dx[cur_dir]
    head[1] += dy[cur_dir]
    x, y = head[0], head[1]
    # 충돌 확인
    if check_head(head, snake, n):
        break
    # 사과 확인
    if check_apple(graph, head):
        snake.append([x, y])
    else:
        snake.append([x, y])
        p, q = snake.popleft()
    # 방향 전환
    if timer == next_time:
        cur_dir = change_direction(cur_dir)

print(timer)
