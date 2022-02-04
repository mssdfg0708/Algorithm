import sys


N, M = map(int, sys.stdin.readline().split())

parent = set()
child = list()

for _ in range(N):
    parent.add(sys.stdin.readline())

answer = 0
for _ in range(M):
    child = sys.stdin.readline()

    if child in parent:
        answer += 1

print(answer)
