# rows, columns 값을 받으면 그 값을 꼭지점으로 가지는 정사각형을 그린다.
# row 값이 일치하거나 columns 값이 일치하는 경우 array list 에 값을 저장
# 또한 row list, col list 에도 값을 저장한다.
# 이후 row[i]col[i] 는 array[i+1] 을 저장
# row[-1] col[-1]은 array[0]을 저장
# min(array) 를 answer 에 저장
# answer 출력
def solution(rows, cols, queries):
    answer = []
    graph = []
    item = 1
    for i in range(rows):
        graph.append([])
        for j in range(cols):
            graph[i].append(item)
            item += 1

    def move(x1, y1, x2, y2):
        array = []
        row = []
        col = []
        for y in range(y1, y2):
            array.append(graph[x1][y])
            row.append(x1)
            col.append(y)
        for x in range(x1, x2):
            array.append(graph[x][y2])
            row.append(x)
            col.append(y2)
        for y in range(y2, y1, -1):
            array.append(graph[x2][y])
            row.append(x2)
            col.append(y)
        for x in range(x2, x1, -1):
            array.append(graph[x][y1])
            row.append(x)
            col.append(y1)

        for k in range(len(array)-1):
            graph[row[k+1]][col[k+1]] = array[k]
        graph[row[0]][col[0]] = array[-1]

        answer.append(min(array))

    for x1, y1, x2, y2 in queries:
        move(x1-1, y1-1, x2-1, y2-1)

    return answer


rows, cols = 100, 97
queries = [[1, 1, 100, 97]]
solution(rows, cols, queries)
