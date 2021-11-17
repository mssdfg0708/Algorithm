import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) >= 2:
        food01 = heapq.heappop(scoville)
        food02 = heapq.heappop(scoville)
        new_food = food01 + food02 * 2
        heapq.heappush(scoville, new_food)
        answer += 1

    for item in scoville:
        if item < K:
            return -1
    return answer


scovile = [1, 2]
K = 6
print(solution(scovile, K))
