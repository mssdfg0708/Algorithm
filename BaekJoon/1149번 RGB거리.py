import sys

n = int(input())
cost_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

for i in range(1, n):
    cost_list[i][0] = cost_list[i][0] + min(cost_list[i-1][1], cost_list[i-1][2])
    cost_list[i][1] = cost_list[i][1] + min(cost_list[i-1][0], cost_list[i-1][2])
    cost_list[i][2] = cost_list[i][2] + min(cost_list[i-1][0], cost_list[i-1][1])

print(min(cost_list[-1]))
