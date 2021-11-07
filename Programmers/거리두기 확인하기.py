from collections import deque


def solution(places):
    def bfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        q = deque()
        q.append([x, y])

        while q:
            nx, ny = q.popleft()
            if visited[nx][ny] == 0:
                visited[nx][ny] += 1
            for i in range(4):
                sx = nx + dx[i]
                sy = ny + dy[i]
                if 0 <= sx < 5 and 0 <= sy < 5 and visited[sx][sy] == 0:
                    if room[sx][sy] == 'X':
                        continue
                    if room[sx][sy] == 'P':
                        visited[sx][sy] = 1
                        distance.append(visited[nx][ny])
                        q.append([sx, sy])
                    else:
                        visited[sx][sy] = visited[nx][ny] + 1
                        q.append([sx, sy])
        return visited

    # main solution
    answer = []
    for place in places:

        room = []
        for pl in place:
            room.append(list(pl))

        distance = []
        visited = [[0 for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if room[i][j] == "P":
                    bfs(i, j)

        if 1 in distance or 2 in distance:
            answer.append(0)
        else:
            answer.append(1)

    return answer
