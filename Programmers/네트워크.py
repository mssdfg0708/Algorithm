from collections import deque


def bfs(n, node, computers, visited):
    q = deque()

    q.append(node)
    visited[node] = True

    while q:
        cur_node = q.popleft()
        for next_node in range(n):
            if cur_node == next_node:
                continue
            if visited[next_node]:
                continue
            if computers[cur_node][next_node]:
                q.append(next_node)
                visited[next_node] = True


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for node in range(n):
        if not visited[node]:
            answer += 1
            bfs(n, node, computers, visited)

    return answer


input_n = 3
input_computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(input_n, input_computers))

# visited[node] 를 확인하여 visited[node] == False 이면
# answer += 1 이후 BFS 진행
