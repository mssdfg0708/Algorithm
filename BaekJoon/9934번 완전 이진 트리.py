import sys


K = int(input())
node_list = list(map(int, sys.stdin.readline().split()))
visited = [False for _ in range(len(node_list))]

# 2 ** k 이 중점이므로 중점을 계속 출력
for k in range(K-1, -1, -1):
    sequence = 2 ** k
    count = 1
    while sequence * count - 1 < len(node_list):
        index = sequence * count - 1
        if not visited[index]:
            visited[index] = True
            print(node_list[index], end=' ')
        count += 1
    print()
