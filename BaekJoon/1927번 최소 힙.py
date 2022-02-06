import sys
import heapq

heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())

    # heap 에 push
    if num:
        heapq.heappush(heap, num)
        continue

    # heap 에서 최소 값 출력
    if heap:
        print(heapq.heappop(heap))
    else:
        print(0)
