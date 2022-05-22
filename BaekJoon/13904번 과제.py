import sys
import heapq

N = int(sys.stdin.readline())
reports = []
cost = [0] * 1001

for _ in range(N):
    day, value = map(int, sys.stdin.readline().split())
    reports.append([-value, day, value])

heapq.heapify(reports)

while reports:
    temp = heapq.heappop(reports)
    for i in range(temp[1], 0, -1):
        if cost[i] == 0:
            cost[i] = temp[2]
            break

answer = sum(cost)
print(answer)
