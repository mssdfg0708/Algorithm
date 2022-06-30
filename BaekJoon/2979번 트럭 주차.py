import sys

truck_count_list = [0 for _ in range(100)]
costs = list(map(int, sys.stdin.readline().split()))
for _ in range(3):
    start, end = map(int, sys.stdin.readline().split())
    for time in range(start, end):
        truck_count_list[time] += 1

answer = 0
for count in truck_count_list:
    count -= 1
    if count >= 0:
        answer += (count + 1) * costs[count]

print(answer)
