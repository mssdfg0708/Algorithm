import heapq


def solution(numbers):
    if sum(numbers) % 3 != 0:
        return -1
    if 0 not in numbers:
        return -1

    answer = ""
    for index in range(len(numbers)):
        answer += str(-1 * heapq.heappop(numbers))
    return answer


data = input()

numbers = []
for number in data:
    heapq.heappush(numbers, -1 * int(number))

print(solution(numbers))
