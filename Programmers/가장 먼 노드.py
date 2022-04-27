from collections import deque


def bfs(visited, graph):
    root = 1
    q = deque()
    max_distance = 0
    result = []

    # [vertex_num, distance]
    q.append([root, 0])
    visited[root] = True

    while q:
        v1, distance = q.popleft()
        if distance > max_distance:
            max_distance = distance
            result.clear()
        result.append(v1)

        for v2 in graph[v1]:
            if not visited[v2]:
                q.append([v2, distance+1])
                visited[v2] = True

    return len(result)


def solution(n, edges):
    visited = [False for _ in range(n + 1)]
    graph = [[] for _ in range(n+1)]
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    answer = bfs(visited, graph)
    return answer


input_n = 6
input_edges = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(input_n, input_edges))
