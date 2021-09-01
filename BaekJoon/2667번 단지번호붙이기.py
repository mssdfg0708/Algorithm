# BFS 사용
from collections import deque


# BFS 함수
def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    member = 1
    graph[i][j] = group

    while queue:
        x, y = queue.popleft()
        for move in range(4):
            move_x = x + dx[move]
            move_y = y + dy[move]
            if move_x < 0 or move_x >= n:
                continue
            if move_y < 0 or move_y >= n:
                continue
            if graph[move_x][move_y] == 1:
                queue.append([move_x, move_y])
                member += 1
                graph[move_x][move_y] = group

    return member


# 입력 받기
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    row = input()
    for item in row:
        graph[i].append(int(item))
# 알고리즘
visited = [[False for i in range(n)] for j in range(n)]
group = 2
group_member = [0, 0]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            group_member.append(bfs(i, j))
            group += 1
# 출력
print(group - 2)
group_member.sort()
for item in group_member:
    if item:
        print(item)
