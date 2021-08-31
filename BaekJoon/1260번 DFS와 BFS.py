from collections import deque

max_vertex, max_edge, start_vertex = map(int, input().split())
graph = [[] for _ in range(max_vertex + 1)]

for _ in range(max_edge):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for item in graph:
    item.sort()

visited = [False] * (max_vertex + 1)
result = ''
order = []


def dfs(vertex):
    visited[vertex] = True
    order.append(vertex)
    for item in graph[vertex]:
        if not visited[item]:
            dfs(item)


def bfs(vertex):
    queue = deque()
    queue.append(vertex)

    while queue:
        vertex = queue.popleft()
        if not visited[vertex]:
            visited[vertex] = True
            order.append(vertex)
            for item in graph[vertex]:
                queue.append(item)


dfs(start_vertex)
for item in order:
    result += str(item) + ' '
print(result[:-1])

visited = [False] * (max_vertex + 1)
result = ''
order = []
bfs(start_vertex)
for item in order:
    result += str(item) + ' '
print(result[:-1])
