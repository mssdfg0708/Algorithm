import sys
import heapq

heap = []
minus_counter = dict()
N = int(sys.stdin.readline().strip())

for _ in range(N):
    query = int(sys.stdin.readline().strip())

    if heap and query == 0:
        num = heapq.heappop(heap)
        if minus_counter[num] > 0:
            minus_counter[num] -= 1
            num *= -1
        print(num)
        continue
    if not heap and query == 0:
        print(0)
        continue

    if query < 0:
        abs_query = abs(query)
        heapq.heappush(heap, abs_query)
        if abs_query not in minus_counter:
            minus_counter[abs_query] = 0
        minus_counter[abs_query] += 1
        continue
    if query > 0:
        abs_query = abs(query)
        if abs_query not in minus_counter:
            minus_counter[abs_query] = 0
        heapq.heappush(heap, abs_query)
