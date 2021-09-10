import heapq
INF = 987654321


def solution(n, s, a, b, fares):
    all_distance = [INF] * (n+1)
    # 0 ~ n 번까지 의 graph
    graph = [[]for _ in range(n + 1)]
    for u, v, w in fares:
        graph[u].append([v, w])
        graph[v].append([u, w])

    def dijkstra(start):
        distance = [INF] * (n+1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance

    for v in range(1, n+1):
        all_distance[v] = dijkstra(v)

    result = []
    for v in range(1, n+1):
        result.append(all_distance[s][v] + all_distance[v][a] + all_distance[v][b])
    return min(result)


n, s, a, b = 7, 3, 4, 1
# fares = [[4, 1, 10],
#          [3, 5, 24],
#          [5, 6, 2],
#          [3, 1, 41],
#          [5, 1, 24],
#          [4, 6, 50],
#          [2, 4, 66],
#          [2, 3, 22],
#          [1, 6, 25]]
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n, s, a, b, fares))
