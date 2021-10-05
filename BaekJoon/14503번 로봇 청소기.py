# n 세로 / m 가로
n, m = map(int, input().split())
# direction
# direction flow 3 2 1 0 3
# 0 = 북 / 1 = 동 / 2 = 남 / 3 = 서
north, west, direction = map(int, input().split())
# graph (n x m)
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
result = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def clean(result, north, west):
    graph[north][west] = 2
    result += 1
    return result


if graph[north][west] == 0:
    result = clean(result, north, west)

while True:
    key = 1
    # 4 방향 확인
    for _ in range(4):
        if direction == 0:
            direction = 3
        else:
            direction -= 1
        nx = north + dx[direction]
        ny = west + dy[direction]
        if graph[nx][ny] == 0:
            north, west = nx, ny
            if graph[north][west] == 0:
                result = clean(result, north, west)
                key = 0
            break
    # 4방향 모두 벽이거나 청소완료 인 경우
    if key:
        # 후방 확인
        nx = north - dx[direction]
        ny = west - dy[direction]
        # 후진 가능
        if graph[nx][ny] != 1:
            north, west = nx, ny
        # 후진 불가능
        else:
            print(result)
            break
