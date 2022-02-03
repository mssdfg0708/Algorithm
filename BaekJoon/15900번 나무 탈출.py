# root 부터 각각의 leaf 노드 까지의 거리를 모두 합한다
# root 부터 각각의 leaf 노드 까지의 거리는 dfs 를 이용하여 계산
# 합이 홀수라면 return Yes
# 합의 짝수라면 return No

import sys
sys.setrecursionlimit(10**6)


def dfs(node, distance):
    if node in leaf_nodes:
        total_distance[0] += distance
        return
    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            dfs(child, distance+1)
            visited[child] = False


N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

leaf_nodes = set()
for node in range(2, N+1):
    if len(graph[node]) <= 1:
        leaf_nodes.add(node)

total_distance = [0]
root = 1
visited[root] = True

# dfs(node, distance)
dfs(root, 0)
answer = total_distance[0]

if answer % 2 == 0:
    print("No")
else:
    print("Yes")
