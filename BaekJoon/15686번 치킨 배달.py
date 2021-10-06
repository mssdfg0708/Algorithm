from itertools import combinations

# 입력 받기
n, m = map(int, input().split())
house_list = []
chicken_list = []
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# graph 에서 집과 치킨집 정보 추출
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house_list.append([i, j])
        if graph[i][j] == 2:
            chicken_list.append([i, j])

# 생존한 치킨집의 경우의 수 모두 확인
survive_list = list(combinations(chicken_list, m))
result = 987654321
for survive in survive_list:
    temp = 0
    for house in house_list:
        dist = 999
        for chicken in survive:
            row_dif = abs(chicken[0] - house[0])
            col_dif = abs(chicken[1] - house[1])
            dist = min(dist, row_dif + col_dif)
        temp += dist
    result = min(result, temp)
print(result)
