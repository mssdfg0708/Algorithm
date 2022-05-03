import heapq


def solution(operations):
    answer = []
    heap = []

    for data in operations:
        order = data[0]
        num = int(data[2:])
        if order == "I":
            heapq.heappush(heap, int(data[2:]))
            continue
        if heap and num == -1:
            heapq.heappop(heap)
            continue
        if heap and num == 1:
            heap = heapq.nlargest(len(heap), heap)[1:]
            heapq.heapify(heap)

    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer = [0, 0]

    return answer


input_answer = ["I 7", "I 5", "I -5", "D -1"]
print(solution(input_answer))
