max_n = int(input())
ability = [[] for _ in range(max_n+1)]
for row in range(1, max_n+1):
    ability[row] = [0] + list(map(int, input().split()))
member = [i for i in range(1, max_n+1)]
start_team = []
team_sum = [0, 0]
result = [987654321]
visited = [False] * (max_n+1)


def calculate_ability(team):
    res = 0
    for item1 in team:
        for item2 in team:
            if item1 != item2:
                res += ability[item1][item2]
    return res


def dfs(depth, n=0):
    if depth > max_n//2:
        link_team = []
        for i in range(1, max_n+1):
            if i not in start_team:
                link_team.append(i)
        temp_result = calculate_ability(start_team) - calculate_ability(link_team)
        if temp_result < 0:
            temp_result *= -1
        result[0] = min(result[0], temp_result)
        return
    for num in range(n+1, max_n+1):
        if not visited[num]:
            visited[num] = True
            start_team.append(num)
            dfs(depth+1, num)
            visited[num] = False
            start_team.pop()


dfs(1)
print(result[0])
