from collections import deque
import sys


N = int(input())
parent_list = [-1 for _ in range(N+1)]
visited = [False for _ in range(N+1)]
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    node1, node2 = map(int, sys.stdin.readline().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

next_nodes = deque()
next_nodes.append(1)
visited[1] = True
while next_nodes:
    parent = next_nodes.popleft()
    if not tree[parent]:
        continue
    for child in tree[parent]:
        if not visited[child]:
            parent_list[child] = parent
            visited[child] = True
            next_nodes.append(child)

for index in range(2, len(parent_list)):
    print(parent_list[index])
