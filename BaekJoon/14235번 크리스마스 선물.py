import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = []
queries = []
for _ in range(N):
    query = sys.stdin.readline().rstrip()
    queries.append(query)

for query in queries:
    if len(query) == 1 and heap:
        num = heapq.heappop(heap) * -1
        print(num)
        continue
    if len(query) == 1 and not heap:
        print(-1)
        continue
    numbers = list(map(int, query.split()))
    numbers = numbers[1:]
    for item in numbers:
        heapq.heappush(heap, item * -1)
