from itertools import permutations

N = int(input())
graph = []
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

orders = permutations(range(N), N)

answer = 999999999
for order in orders:
    distance_total = 0
    for index in range(N-1):
        now = order[index]
        next = order[index+1]
        distance = graph[now][next]
        if distance == 0:
            distance_total = -1
            break
        distance_total += distance

    now = order[-1]
    next = order[0]
    distance = graph[now][next]
    if distance == 0 or distance_total == -1:
        distance_total = -1
    else:
        distance_total += distance

    if distance_total > 0:
        answer = min(answer, distance_total)

print(answer)
