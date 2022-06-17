import sys

INF = 99999999999
X, Y, BLOCK = map(int, sys.stdin.readline().split())
land = []
for _ in range(X):
    row = list(map(int, sys.stdin.readline().split()))
    land.append(row)

answer = [INF, 0]

for height_target in range(257):
    min_cost, max_height = answer
    block_cost = 0
    time_cost = 0
    for row in land:
        for height in row:
            differ = height_target - height
            if differ > 0:
                time_cost += differ
                block_cost += differ
            if differ < 0:
                time_cost -= differ*2
                block_cost += differ

    if block_cost > BLOCK:
        break
    if time_cost <= min_cost:
        answer = [time_cost, height_target]
        continue

print(answer[0], answer[1])
