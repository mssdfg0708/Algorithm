import sys
from collections import deque

# BFS 로 풀이

# n 도시개수 m 도로개수 k 거리정보 x 출발도시
n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
distance = [-1 for i in range(n + 1)]

# graph 에 정보 입력
for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

# BFS 모듈
queue = deque([x])
distance[x] = 0
while queue:
    v = queue.popleft()
    for item in graph[v]:
        if distance[item] == -1:
            queue.append(item)
            distance[item] = distance[v] + 1

# 거리가 k 인 도시 출력
result = 0
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        result += 1
if not result:
    print(-1)
