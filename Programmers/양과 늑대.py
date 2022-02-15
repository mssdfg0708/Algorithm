def search(graph, nodes, info, index, sheep, wolf, answer):
    next_nodes = nodes.copy()

    parent = next_nodes[index]
    next_nodes.remove(parent)

    if info[parent] == "wolf":
        wolf += 1
        if wolf >= sheep:
            return
    if info[parent] == "sheep":
        sheep += 1
        answer[0] = max(answer[0], sheep)

    if graph[parent]:
        for node in graph[parent]:
            next_nodes.append(node)

    for index in range(len(next_nodes)):
        search(graph, next_nodes, info, index, sheep, wolf, answer)


def solution(info, edges):
    for index in range(len(info)):
        if info[index] == 1:
            info[index] = "wolf"
        else:
            info[index] = "sheep"

    root = 0
    graph = [[] for _ in range(len(info))]
    for parent, child in edges:
        graph[parent].append(child)

    next_nodes = [root]
    answer = [0]
    search(graph, next_nodes, info, 0, 0, 0, answer)

    return answer[0]


info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
print(solution(info, edges))
