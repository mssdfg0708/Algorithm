import sys
from collections import deque

V = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    query = list(map(int, sys.stdin.readline().split()))
    for index in range(1, len(query) - 2, 2):
        graph[query[0]].append((query[index], query[index + 1]))


def bfs(start):
    distance_memory = [-1] * (V + 1)
    q = deque()
    q.append(start)
    distance_memory[start] = 0
    result = [0, 0]

    while q:
        cur_node = q.popleft()
        for next_node, distance in graph[cur_node]:
            if distance_memory[next_node] == -1:
                distance_memory[next_node] = distance_memory[cur_node] + distance
                q.append(next_node)
                if result[0] < distance_memory[next_node]:
                    result = distance_memory[next_node], next_node

    return result


distance, node = bfs(1)
distance, node = bfs(node)
print(distance)
