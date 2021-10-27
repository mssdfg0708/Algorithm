# 주사위는 dice = [아래, 앞, 위, 뒤, 오른쪽, 왼쪽] 으로 구성

# 초기값 입력
# 지도의 크기 [n][m]
# 주사위의 시작 위치 [x][y]
# 주어지는 명령의 개수 = k
n, m, x, y, k = map(int, input().split())
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
EAST = 1
WEST = 2
NORTH = 3
SOUTH = 4
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dice = [0, 0, 0, 0, 0, 0]
orders = list(map(int, input().split()))

# 알고리즘 실행
for order in orders:
    nx = x + dx[order]
    ny = y + dy[order]
    # Out Of Index 확인
    if not (0 <= nx < n):
        continue
    if not (0 <= ny < m):
        continue
    x = nx
    y = ny

    # dice = [아래, 앞, 위, 뒤, 오른쪽, 왼쪽]
    if order == EAST:
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]
    elif order == WEST:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]
    elif order == NORTH:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif order == SOUTH:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]

    if graph[x][y] == 0:
        graph[x][y] = dice[0]
    else:
        dice[0] = graph[x][y]
        graph[x][y] = 0

    print(dice[2])
