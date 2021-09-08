import heapq
import sys
INF = 987654321


# 입력 받기 V = vertex | E = edge
V, E = map(int, sys.stdin.readline().split())
start_vertex = 1
distance = [INF for _ in range(V + 1)]

# graph 입력 받기
# u = 시작점 | v = 도착점 | w = 거리
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])
    graph[v].append([u, w])


# 최단 경로 알고리즘
def dijkstra(case, start, end):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, vertex = heapq.heappop(q)
        for item in graph[vertex]:
            cost = dist + item[1]
            if distance[item[0]] > cost:
                distance[item[0]] = cost
                heapq.heappush(q, (distance[item[0]], item[0]))
    if distance[end] == INF:
        return False
    waypoint_distance[case] += distance[end]
    return True


# 경유 노드
waypoint = [1]
way = list(map(int, input().split()))
for item in way:
    waypoint.append(item)
waypoint.append(V)
waypoint_distance = [0] * 2

# 1차 진입 지점
for i in range(1, len(waypoint)):
    case = 0
    if not dijkstra(case, waypoint[i-1], waypoint[i]):
        waypoint_distance[case] = INF
        break
    distance = [INF for _ in range(V + 1)]

# 경유 노드 재 지정
waypoint[1], waypoint[2] = waypoint[2], waypoint[1]

# 2차 진입 지점
for i in range(1, len(waypoint)):
    case = 1
    if not dijkstra(case, waypoint[i-1], waypoint[i]):
        waypoint_distance[case] = INF
        break
    distance = [INF for _ in range(V + 1)]


# 츌력 형식 적용
result = min(waypoint_distance)
if result == INF:
    print(-1)
else:
    print(result)
