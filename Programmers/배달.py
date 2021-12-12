def solution(n, roads, k):
    INF = 987654321
    # distance 초기 설정
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for a in range(1, n + 1):
        graph[a][a] = 0
    # 간선 정보 입력 a에서 b로 가는 거리는 c
    for road in roads:
        a, b, c = road[0], road[1], road[2]
        if c < graph[a][b]:
            graph[a][b] = c
            graph[b][a] = c
    # 점화식 수행
    for t in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][t] + graph[t][b])
    # 결과 출력
    answer = 0
    print(graph[1])
    for cost in graph[1]:
        if cost <= k:
            answer += 1

    return answer


n = 6
roads = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
k = 4
print(solution(n, roads, k))
