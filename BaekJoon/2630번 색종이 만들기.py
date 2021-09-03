n = int(input())
graph = []
# white = 0
# blue = 1
color_count = [0, 0]
for i in range(n):
    graph.append(list(map(int, input().split())))


def cut(x, y, n):
    color = graph[x][y]
    # [x][y]의 색과 다른 색을 탐색한다
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != graph[i][j]:
                # 다른 색이 발견된 경우
                cut(x, y, n // 2)
                cut(x, y + n // 2, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                return
    # 모두 같은색인 경우
    if color == 0:
        color_count[0] += 1
    else:
        color_count[1] += 1


cut(0, 0, n)
print(color_count[0])
print(color_count[1])
