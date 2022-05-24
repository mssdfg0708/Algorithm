from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

answer = 0
for i in range(n):
    for j in range(m):
        # 가장자리가 아님
        if i > 0 and i + 1 < n:
            if board[i - 1][j] == "L" and board[i + 1][j] == "L":
                continue
        if j > 0 and j + 1 < m:
            if board[i][j - 1] == "L" and board[i][j + 1] == "L":
                continue

        # BFS 진행
        if board[i][j] == "L" and not visit[i][j]:
            q = deque([(i, j)])
            visit_tmp = [i[:] for i in visit]
            visit_tmp[i][j] = 1
            r = 0
            while q:
                x, y = q.popleft()
                for a, b in move:
                    dx = x + a
                    dy = y + b
                    if n > dx >= 0 and m > dy >= 0 and not visit_tmp[dx][dy] and board[dx][dy] == "L":
                        visit_tmp[dx][dy] = visit_tmp[x][y] + 1
                        r = max(r, visit_tmp[dx][dy])
                        q.append((dx, dy))

            answer = max(answer, r)

print(answer - 1)
