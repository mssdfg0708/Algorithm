background = [[0 for _ in range(100)] for _ in range(100)]
num = int(input())

for _ in range(num):
    left, bottom = map(int, input().split())
    bottom = 100 - bottom
    for x in range(left, left + 10):
        for y in range(bottom - 10, bottom):
            background[x][y] = 1

cnt = 0
for row in background:
    for item in row:
        if item == 1:
            cnt += 1
print(cnt)
