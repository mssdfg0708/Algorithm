import sys

n = int(sys.stdin.readline())
arr = []
visit = [[0] * n for i in range(n)]


def floyd():
    for k in range(n):
        for i in range(n):
            for m in range(n):
                if i == m:
                    continue
                if arr[i][m] == "Y" or (arr[i][k] == "Y" and arr[k][m] == "Y"):
                    visit[i][m] = 1


for i in range(n):
    arr.append(list(sys.stdin.readline().strip()))
floyd()
result = 0

for i in range(n):
    cnt = 0
    for j in range(n):
        if visit[i][j] == 1:
            cnt += 1
    result = max(result, cnt)

print(result)
