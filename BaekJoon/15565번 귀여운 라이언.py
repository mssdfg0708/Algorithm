import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

answer = 987654321
indexes_of_target = deque()

for index in range(len(numbers)):
    if numbers[index] == 1 and len(indexes_of_target) < K - 1:
        indexes_of_target.append(index)
        continue
    if numbers[index] == 1 and len(indexes_of_target) == K - 1:
        indexes_of_target.append(index)
        length = indexes_of_target[-1] - indexes_of_target[0] + 1
        answer = min(answer, length)
        continue
    if numbers[index] == 1 and len(indexes_of_target) == K:
        indexes_of_target.popleft()
        indexes_of_target.append(index)
        length = indexes_of_target[-1] - indexes_of_target[0] + 1
        answer = min(answer, length)

if answer == 987654321:
    answer = -1

print(answer)
