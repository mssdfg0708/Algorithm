import sys

n, m = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
B = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
answer = 0


def flip(X, Y):
    for x in range(X, X + 3):
        for y in range(Y, Y + 3):
            A[x][y] = 1 - A[x][y]


for i in range(n - 2):
    for j in range(m - 2):
        if A[i][j] != B[i][j]:
            flip(i, j)
            answer += 1

        if A == B:
            break
    if A == B:
        break

if A != B:
    print(-1)
else:
    print(answer)
