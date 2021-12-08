from collections import deque


def solution(maps):
    visited = []
    for _ in range(len(maps)):
        visited.append([False for _ in range(len(maps[0]))])

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    answer = -1
# BFS -------------------------------------------
    q = deque()
    q.append([0, 0, 1])
    visited[0][0] = True
    while q:
        x, y, count = q.popleft()
        # 도착 하면 종료
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            answer = count
            break
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= len(maps):
                continue
            if ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if visited[nx][ny]:
                continue
            q.append([nx, ny, count + 1])
            visited[nx][ny] = True
# BFS -------------------------------------------
    return answer


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(maps))

# BFS 이용하여 진행
# 1 = 벽이 없는자리 / 0 = 벽이 있는자리
# q 의 원소는 [x, y, 지나간 칸의 개수] 를 의미
