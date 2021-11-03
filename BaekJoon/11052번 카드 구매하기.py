# 1개 사기 위한 최대값 P1
# 2개 사기 위한 최대값 max(P2, max[1] +P1)
# 3개 사기 위한 최대값 max(P3, max[2] +P1, max[1] +P2)
# 4개 사기 위한 최대값 max(P4, max[3] +P1, max[2] +P2, max[1] +P3)
# n개 사기 위한 최대값 max(Pn, max[n-1] +P[n-(n-1)], max[n-2] + P[n-(n-2)], ... , max[2] + P[n-2], max[1] + P[n-1])
from sys import stdin


n = int(input())
card_cost = [-1] + list(map(int, stdin.readline().split()))
dp = [-1, card_cost[1]]

for dp_index in range(2, n + 1):
    temp = [card_cost[dp_index]]
    for i in range(1, dp_index):
        temp.append(card_cost[i] + dp[dp_index - i])
    dp.append(max(temp))

print(max(dp))
