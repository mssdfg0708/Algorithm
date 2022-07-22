import sys
import heapq

TEST = int(sys.stdin.readline().rstrip())
for _ in range(TEST):
    N = int(sys.stdin.readline().rstrip())
    min_heap = []
    max_heap = []
    visited = [False for _ in range(1000001)]

    for query_id in range(N):
        query_order, query_num = list(sys.stdin.readline().split())
        query_num = int(query_num)

        if query_order == 'I':
            item = [query_num, query_id]
            heapq.heappush(min_heap, item)
            item = [query_num * -1, query_id]
            heapq.heappush(max_heap, item)
            visited[query_id] = True
            continue

        if query_order == 'D' and query_num == 1:
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
            continue

        if query_order == 'D' and query_num == -1:
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)
            continue

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if min_heap and max_heap:
        print(max_heap[0][0] * -1, min_heap[0][0])
    else:
        print('EMPTY')
