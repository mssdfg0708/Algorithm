from itertools import combinations

def sol1():
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


def sol2():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    members = [i for i in range(N)]
    possible_team = []

    for team in list(combinations(members, N // 2)):
        possible_team.append(team)

    min_stat_gap = 987654321
    for i in range(len(possible_team) // 2):
        team = possible_team[i]
        stat_A = 0
        for j in range(N // 2):
            member = team[j]
            for k in team:
                stat_A += S[member][k]

        team = possible_team[-i - 1]
        stat_B = 0
        for j in range(N // 2):
            member = team[j]
            for k in team:
                stat_B += S[member][k]

        min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))

    print(min_stat_gap)


sol2()
