from collections import deque

N = int(input())
parents = [-1 for _ in range(N)]
input_list = list(map(int, input().split()))
root = -1
for current in range(N):
    parent = input_list[current]
    if parent == -1:
        root = current
        continue
    parents[current] = parent

delete_index = int(input())
q = deque()
q.append(delete_index)
parents[delete_index] = -2

while q:
    target = q.popleft()
    for current in range(len(parents)):
        if parents[current] == -2:
            continue
        if parents[current] != target:
            continue
        q.append(current)
        parents[current] = -2

graph = [[] for _ in range(N)]
for end in range(len(parents)):
    start = parents[end]
    if start < 0:
        continue
    graph[start].append(end)

answer = 0
if parents[root] != -2:
    q.clear()
    q.append(root)
    while q:
        index = q.popleft()
        if not graph[index]:
            answer += 1
            continue
        for next_index in graph[index]:
            q.append(next_index)

print(answer)
