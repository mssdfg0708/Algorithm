import sys


def checking(temp, sticker):
    for sy in range(len(sticker)):
        for sx in range(len(sticker[0])):
            if temp[i + sy][j + sx] + sticker[sy][sx] > 1:
                return False
    return True


def attach(temp, sticker):
    for sy in range(len(sticker)):
        for sx in range(len(sticker[0])):
            temp[i + sy][j + sx] += sticker[sy][sx]
    return


def rotate_90(arr):
    n = len(arr)
    m = len(arr[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = arr[i][j]
    return result


Y, X, k = map(int, sys.stdin.readline().split())
notebook = [[0] * X for _ in range(Y)]

for _ in range(k):
    y, x = map(int, sys.stdin.readline().split())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(y)]
    is_check = False
    count = 0
    while count < 4:
        if is_check:
            break
        for i in range(Y - len(sticker) + 1):
            if is_check:
                break
            for j in range(X - len(sticker[0]) + 1):
                if checking(notebook, sticker):
                    attach(notebook, sticker)
                    is_check = True
                    break
        sticker = rotate_90(sticker)
        count += 1

answer = 0
for i in range(Y):
    for j in range(X):
        answer += notebook[i][j]

print(answer)
