import sys
import heapq

heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())

    # heap 에 push
    if num:
        heapq.heappush(heap, -num)
        continue

    # heap 에서 최대 값 출력
    if heap:
        result = -1 * heapq.heappop(heap)
        print(result)
    else:
        print(0)
