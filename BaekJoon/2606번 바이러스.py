from collections import deque


def bfs(vertex):
    count = 0
    queue = deque()
    queue.append(vertex)
    visited[vertex] = True

    while queue:
        vertex = queue.popleft()
        for item in graph[vertex]:
            if not visited[item]:
                queue.append(item)
                visited[item] = True
                count += 1

    print(count)


max_vertex = int(input())
max_edge = int(input())
graph = [[] for _ in range(max_vertex + 1)]
visited = [False] * (max_vertex + 1)

for _ in range(max_edge):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for item in graph:
    item.sort()

bfs(1)
