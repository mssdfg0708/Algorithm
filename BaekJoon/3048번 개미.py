import sys

N1, N2 = map(int, sys.stdin.readline().split())
ants1 = list(sys.stdin.readline().rstrip())
ants2 = list(sys.stdin.readline().rstrip())
T = int(sys.stdin.readline())

direction = {}
for ant in ants1:
    direction[ant] = 0
for ant in ants2:
    direction[ant] = 1

ants1.reverse()
ants1.extend(ants2)

for _ in range(T):
    i = 0
    while i < len(ants1) - 1:
        if direction[ants1[i]] == 0 and direction[ants1[i + 1]] == 1:
            ants1[i], ants1[i + 1] = ants1[i + 1], ants1[i]
            i += 1
        i += 1

for ant in ants1:
    print(ant, end='')
