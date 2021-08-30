max_n, max_depth = map(int, input().split())
result = []

def dfs(depth, n):
    if depth > max_depth:
        for item in result:
            print(item, end = ' ')
        print()
        return
    for n in range(n + 1, max_n + 1):
        result.append(n)
        dfs(depth + 1, n)
        result.pop()

dfs(1, 0)
