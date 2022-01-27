from collections import deque
import sys

T = int(input())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    visited = [False for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    visited_country = 0

    q.append(1)
    visited[1] = True
    while q:
        now = q.popleft()
        for next_country in graph[now]:
            if not visited[next_country]:
                visited[next_country] = True
                visited_country += 1
                q.append(next_country)

    print(visited_country)
