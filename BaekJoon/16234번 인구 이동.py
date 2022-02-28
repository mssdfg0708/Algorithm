"""
BFS 를 이용하여 연합을 형성
연합의 각 국가는 [x, y, population] 으로 구성

연합 목록을 보며 연합 사이에 인구 이동
연합 목록이 비어 있다면 종료
"""

from collections import deque
import sys

N, min_differ, max_differ = map(int, sys.stdin.readline().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def check_population(x, y, visited):
    q = deque()
    union = []

    visited[x][y] = True
    q.append([x, y, graph[x][y]])

    while q:
        x, y, population = q.popleft()
        union.append([x, y, population])
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= N:
                continue
            if ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue

            differ = abs(population - graph[nx][ny])
            if differ < min_differ or differ > max_differ:
                continue
            visited[nx][ny] = True
            q.append([nx, ny, graph[nx][ny]])

    return union


def solution():
    date = 0

    while True:
        visited = [[False for _ in range(N)] for _ in range(N)]
        unions = []
        for x in range(N):
            for y in range(N):
                if not visited[x][y]:
                    union = check_population(x, y, visited)
                    if len(union) > 1:
                        unions.append(union)
        if unions:
            date += 1
            for union in unions:
                union_population = 0
                union_nation = 0

                for x, y, population in union:
                    union_population += population
                    union_nation += 1

                new_population = union_population//union_nation
                for x, y, population in union:
                    graph[x][y] = new_population
            continue

        return date


print(solution())
