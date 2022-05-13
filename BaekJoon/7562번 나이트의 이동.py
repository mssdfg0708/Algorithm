import sys
from collections import deque

t = int(sys.stdin.readline())
dxy = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

for _ in range(t):
    length = int(sys.stdin.readline())
    cur_x, cur_y = list(map(int, sys.stdin.readline().split()))
    des_x, des_y = list(map(int, sys.stdin.readline().split()))

    visited = [[False for _ in range(length)] for _ in range(length)]
    q = deque([(cur_x, cur_y, 0)])
    while q:
        x, y, cnt = q.popleft()
        visited[x][y] = True
        if (x, y) == (des_x, des_y):
            print(cnt)
            break

        for dx, dy in dxy:
            if 0 <= x+dx < length and 0 <= y+dy < length and not visited[x + dx][y + dy]:
                visited[x+dx][y+dy] = True
                q.append((x+dx, y+dy, cnt+1))
