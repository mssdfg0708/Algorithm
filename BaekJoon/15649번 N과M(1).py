max_n, max_depth = map(int, input().split())
result = []
visited = [False] * (max_n+1)

def dfs(depth, n = 1):
    if depth >= max_depth + 1:
        for item in result:
            print(item, end = ' ')
        print()
        return
    for n in range(1, max_n + 1):
        if not visited[n]:
            visited[n] = True
            result.append(n)
            dfs(depth + 1, n)
            visited[n] = False
            result.pop()

# 초기 depth 는 1
dfs(1)
