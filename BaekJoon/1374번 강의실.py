import sys
import heapq

N = int(sys.stdin.readline().rstrip())
lecture_heap = []
for _ in range(N):
    lecture_info = list(map(int, sys.stdin.readline().split()))
    lecture_info = lecture_info[1:]
    heapq.heappush(lecture_heap, lecture_info)

room_heap = [0]
while lecture_heap:
    start, end = heapq.heappop(lecture_heap)
    if room_heap[0] > start:
        heapq.heappush(room_heap, end)
        continue
    heapq.heappop(room_heap)
    heapq.heappush(room_heap, end)

print(len(room_heap))
