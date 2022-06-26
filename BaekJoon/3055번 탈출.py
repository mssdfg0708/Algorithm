from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        length = len(q)
        while length:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == '.' and c[nx][ny] == 0:
                        c[nx][ny] = c[x][y] + 1
                        q.append([nx, ny])
                    elif a[nx][ny] == 'D':
                        print(c[x][y])
                        return
            length -= 1
        water()

    print("KAKTUS")
    return


def water():
    length = len(q_second)
    while length:
        x, y = q_second.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == '.':
                    a[nx][ny] = '*'
                    q_second.append([nx, ny])
        length -= 1


n, m = map(int, input().split())
a = [list(map(str, input())) for _ in range(n)]
c = [[0] * m for _ in range(n)]
q, q_second = deque(), deque()

x1, y1 = -1, -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            x1, y1 = i, j
            a[i][j] = '.'
        elif a[i][j] == '*':
            q_second.append([i, j])

water()
bfs(x1, y1)
