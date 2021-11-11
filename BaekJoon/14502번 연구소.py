from collections import deque
from itertools import combinations
import copy


def bfs(virus_list):
    temp = copy.deepcopy(graph)
    n, m = len(graph), len(graph[0])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 바이러스 개수 만큼 실행
    for item in virus_list:
# BFS Module ========================================
        q = deque([[item[0], item[1]]])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n:
                    continue
                if ny < 0 or ny >= m:
                    continue
                if temp[nx][ny] != 0:
                    continue
                q.append([nx, ny])
                temp[nx][ny] = 2
# BFS Module ========================================
    # 안전지대 확인
    safe_zone = 0
    for row in temp:
        for item in row:
            if item == 0:
                safe_zone += 1

    return safe_zone


# MAIN START ========================================
# 입력 받기
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 바이러스(2), 공터(0) 위치 확인
virus_list = []
candidates = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 2:
            virus_list.append([x, y])
        if graph[x][y] == 0:
            candidates.append([x, y])

# 벽 3개를 세울 수 있는 조합 확인 후 실행
max_safe_zone = 0
candidates_of_wall_location = list(combinations(candidates, 3))
for p1, p2, p3 in candidates_of_wall_location:
    # 벽을 세운다
    graph[p1[0]][p1[1]] = 1
    graph[p2[0]][p2[1]] = 1
    graph[p3[0]][p3[1]] = 1

    # bfs 실행
    safe_zone = bfs(virus_list)
    max_safe_zone = max(max_safe_zone, safe_zone)

    # 벽을 제거한다
    graph[p1[0]][p1[1]] = 0
    graph[p2[0]][p2[1]] = 0
    graph[p3[0]][p3[1]] = 0

print(max_safe_zone)
