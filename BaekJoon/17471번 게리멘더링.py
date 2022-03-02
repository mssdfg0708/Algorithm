from collections import deque
import sys


def bfs(section):
    q = deque()
    check = [0 for _ in range(n)]
    q.append(section[0])
    check[section[0]] = 1
    cnt, ans = 1, 0
    while q:
        x = q.popleft()
        ans += people[x]
        for nx in a[x]:
            if nx in section and not check[nx]:
                check[nx] = 1
                cnt += 1
                q.append(nx)
    if cnt == len(section):
        return ans
    else:
        return 0


def dfs(cnt, x, end):
    global min_ans
    if cnt == end:
        section1, section2 = deque(), deque()
        for i in range(n):
            if c[i]:
                section1.append(i)
            else:
                section2.append(i)
        ans1 = bfs(section1)
        if not ans1:
            return
        ans2 = bfs(section2)
        if not ans2:
            return
        min_ans = min(min_ans, abs(ans2 - ans1))
        return

    for i in range(x, n):
        if c[i]:
            continue
        c[i] = 1
        dfs(cnt + 1, i, end)
        c[i] = 0


n = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))

a = [[] for _ in range(n)]
for i in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    for j in range(1, x[0] + 1):
        a[i].append(x[j] - 1)

INF = 9876543210
min_ans = INF
for i in range(1, n // 2 + 1):
    c = [0 for _ in range(n)]
    dfs(0, 0, i)

if min_ans == INF:
    print(-1)
else:
    print(min_ans)
