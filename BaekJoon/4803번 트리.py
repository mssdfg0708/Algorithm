import sys


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


index = 0
while True:
    index += 1
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    parents = [current for current in range(n + 1)]
    cycle = set()

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if find(a) == find(b):
            cycle.add(parents[a])
            cycle.add(parents[b])

        if parents[a] in cycle or parents[b] in cycle:
            cycle.add(parents[a])
            cycle.add(parents[b])
        union(a, b)

    for node in range(n + 1):
        find(node)

    answer = -1
    parents = set(parents)
    for node in parents:
        if node not in cycle:
            answer += 1

    if answer == 0:
        print('Case %d: No trees.' % index)
    elif answer == 1:
        print('Case %d: There is one tree.' % index)
    else:
        print('Case %d: A forest of %d trees.' % (index, answer))
