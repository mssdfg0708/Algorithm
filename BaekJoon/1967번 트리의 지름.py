import sys

sys.setrecursionlimit(10 ** 9)


def dfs(parent, distance):
    for child, weight in graph[parent]:
        if distance_memory[child] == -1:
            distance_memory[child] = distance + weight
            dfs(child, distance + weight)


N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    parent, child, distance = map(int, sys.stdin.readline().split())
    graph[parent].append([child, distance])
    graph[child].append([parent, distance])

distance_memory = [-1 for _ in range(N + 1)]
distance_memory[1] = 0
dfs(1, 0)

max_distance = -1
max_index = -1
for index in range(len(distance_memory)):
    if max_distance < distance_memory[index]:
        max_index = index
        max_distance = distance_memory[index]

distance_memory = [-1 for _ in range(N + 1)]
distance_memory[max_index] = 0
dfs(max_index, 0)

max_distance = -1
max_index = -1
for index in range(len(distance_memory)):
    if max_distance < distance_memory[index]:
        max_index = index
        max_distance = distance_memory[index]

print(max_distance)

"""
루트 노드에서 가장 거리가 먼 노드를 N1
N1 에서 가장 거리가 먼 노드를 N2 라고 한다
N1 과 N2 사이의 거리가 트리의 지름이 된다

루트, N1 에서 DFS 를 돌려 N1, N2 를 찾을 수 있다
"""
