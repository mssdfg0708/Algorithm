from sys import stdin


def set_root(root):
    visited[root] = True
    for edge in edge_list[root]:
        stack.append(edge)


def set_graph(root):
    vertex = stack.pop()
    graph[vertex] = root
    if not visited[vertex]:
        visited[vertex] = True
        for edge in edge_list[vertex]:
            stack.append(edge)


# n = num of vertex / m = num of edge
n, m = map(int, stdin.readline().split())
graph = [i for i in range(0, n+1)]

edge_list = [[]for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    edge_list[u].append(v)
    edge_list[v].append(u)

visited = [False for _ in range(n+1)]
visited[0] = True
stack = []
for root in range(n+1):
    if not visited[root]:
        set_root(root)
    while stack:
        set_graph(root)

# 출력 형식 적용
graph = graph[1:]
graph = set(graph)
print(len(graph))
