# 모든 정점마다 실행
# bfs 를 4 depth까지 실행
# bfs 로 계산이 불가능한 'ㅗ' 모양 블럭은 depth == 2 일 경우에 추가 연산을 통해 따로 해결
# 최대 값을 저장
# 각 정점을 계산할때 마다 최대값 갱신
# 최대값 출력
import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 전역 변수
result = 0
max_val = max(map(max, graph))
visit = [([0] * m) for _ in range(n)]
# 우, 좌, 하, 상
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(depth, row, col, res):
    global temp
    if temp >= res + max_val * (4 - depth):
        return
    if depth > 3:
        temp = max(res, temp)
        return
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if nx < 0 or nx >= n:
            continue
        if ny < 0 or ny >= m:
            continue
        if not visit[nx][ny]:
            # depth == 2인 경우 추가 연산
            if depth == 2:
                visit[nx][ny] = 1
                dfs(depth + 1, row, col, res + graph[nx][ny])
                visit[nx][ny] = 0
            visit[nx][ny] = 1
            dfs(depth + 1, nx, ny, res + graph[nx][ny])
            visit[nx][ny] = 0


# 모든 정점마다 실행
for row in range(n):
    for col in range(m):
        temp = -1
        visit[row][col] = 1
        dfs(1, row, col, graph[row][col])
        visit[row][col] = 0
        result = max(result, temp)

print(result)

