import heapq
import sys
INF = 987654321

# 입력 받기 V = vertex | E = edge
V, E = map(int, sys.stdin.readline().split())
start_vertex = int(input())
distance_list = [INF for _ in range(V + 1)]

# graph 입력 받기
# u = 시작점 | v = 도착점 | w = 거리
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])


# 최단 경로 알고리즘
def dijkstra(start):
    distance_list[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        distance, vertex = heapq.heappop(q)
        for item in graph[vertex]:
            if distance_list[item[0]] > distance + item[1]:
                distance_list[item[0]] = distance + item[1]
                heapq.heappush(q, (distance_list[item[0]], item[0]))


dijkstra(start_vertex)

# 출력 형식 적용
for item in distance_list[1:]:
    if item == INF:
        print('INF')
    else:
        print(item)
