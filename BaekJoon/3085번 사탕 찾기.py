n = int(input())

array = []
for _ in range(n):
    colors = list(map(str, input()))
    array.append(colors)

maxCount = 0


def width():
    global maxCount

    for k in range(n):
        count_row = 1
        for idx in range(n - 1):
            if array[k][idx] == array[k][idx + 1]:
                count_row += 1
                maxCount = max(maxCount, count_row)
            else:
                count_row = 1


def height():
    for k in range(n):
        global maxCount

        count_column = 1
        for idx in range(n - 1):
            if array[idx][k] == array[idx + 1][k]:
                count_column += 1
                maxCount = max(maxCount, count_column)
            else:
                count_column = 1


for i in range(n):
    for j in range(n - 1):
        if array[i][j] != array[i][j + 1]:
            array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]
            width()
            height()
            array[i][j + 1], array[i][j] = array[i][j], array[i][j + 1]
        if array[j][i] != array[j + 1][i]:
            array[j][i], array[j + 1][i] = array[j + 1][i], array[j][i]
            width()
            height()
            array[j + 1][i], array[j][i] = array[j][i], array[j + 1][i]

print(maxCount)
