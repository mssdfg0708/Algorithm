city_limit = int(input())
bus_limit = int(input())
INF = 987654321
cost = [[INF] * city_limit for _ in range(city_limit)]

for index in range(bus_limit):
    a, b, c = map(int, input().split())
    if cost[a - 1][b - 1] > c:
        cost[a - 1][b - 1] = c

for start in range(city_limit):
    for mid in range(city_limit):
        for end in range(city_limit):
            if mid != end and cost[mid][end] > cost[mid][start] + cost[start][end]:
                cost[mid][end] = cost[mid][start] + cost[start][end]

for city in cost:
    for cost in city:
        if cost == INF:
            print(0, end=' ')
            continue
        print(cost, end=' ')
    print()
