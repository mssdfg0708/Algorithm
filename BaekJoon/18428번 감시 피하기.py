import sys

# O에 가려지지 않고 S 와 T 가 일직선상에 위치하는지 확인
def check(graph, s, t, n):
    for x_original, y_original in s:
        x, y = x_original, y_original
        while x >= 0:
            if graph[x][y] == 'T':
                return False
            if graph[x][y] == 'O':
                break
            x -= 1
        x, y = x_original, y_original
        while x < n:
            if graph[x][y] == 'T':
                return False
            if graph[x][y] == 'O':
                break
            x += 1
        x, y = x_original, y_original
        while y >= 0:
            if graph[x][y] == 'T':
                return False
            if graph[x][y] == 'O':
                break
            y -= 1
        x, y = x_original, y_original
        while y < n:
            if graph[x][y] == 'T':
                return False
            if graph[x][y] == 'O':
                break
            y += 1
    return True

# 입력 받기
n = int(input())
graph = []
for i in range(n):
    graph.append(input().split())

# S, T 위치 저장
s = []
t = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 'S':
            s.append([x, y])
        elif graph[x][y] == 'T':
            t.append([x, y])

# 장애물 배치
space = list()
for x in range(n):
    for y in range(n):
        if [x, y] in s or [x, y] in t:
            continue
        else:
            space.append([x, y])

# space 조합
checkYes = False
for a, b in space:
    for c, d in space:
        for e, f in space:
            graph[a][b], graph[c][d], graph[e][f] = 'O', 'O', 'O'
            if check(graph, s, t, n):
                if not checkYes:
                    print("YES")
                    checkYes = True
            graph[a][b], graph[c][d], graph[e][f] = 'X', 'X', 'X'
if not checkYes:
    print("NO")
