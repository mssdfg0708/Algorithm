from collections import deque
import sys


def bfs():
    while q:
        a, b, c = q.popleft()
        visit[c][a][b] = 1
        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]
            if x < 0 or x >= n:
                continue
            if y < 0 or y >= m:
                continue
            if z < 0 or z >= h:
                continue
            if box[z][x][y] != 0 or visit[z][x][y] != 0:
                continue
            q.append([x, y, z])
            box[z][x][y] = box[c][a][b] + 1
            visit[z][x][y] = 1


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

m, n, h = map(int, sys.stdin.readline().split())
box = [[] for i in range(h)]
visit = [[[0 for x in range(m)] for y in range(n)] for z in range(h)]
q = deque()
isRipe = False

for i in range(h):
    for j in range(n):
        box[i].append(list(map(int, sys.stdin.readline().split())))

for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 1:
                q.append([x, y, z])

bfs()

max_num = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 0:
                isRipe = True
            max_num = max(max_num, box[z][x][y])

if isRipe:
    print(-1)

else:
    print(max_num - 1)
