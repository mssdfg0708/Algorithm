from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
durability_list = list(map(int, sys.stdin.readline().split()))

entry_point = 0
exit_point = n-1

belts_robot = deque()
belts_durability = deque()
for durability in durability_list:
    belts_robot.append(False)
    belts_durability.append(durability)

zero_count = 0
answer = 0
while zero_count < k:
    answer += 1
    data = belts_robot.pop()
    belts_robot.appendleft(data)
    data = belts_durability.pop()
    belts_durability.appendleft(data)

    belts_robot[exit_point] = False

    if belts_durability[0] > 0 and belts_robot[2*n-1] and not belts_robot[0]:
        belts_robot[2*n-1] = False
        belts_robot[0] = True
        belts_durability[0] -= 1
        if belts_durability[0] == 0:
            zero_count += 1
    for index in range(2*n-2, -1, -1):
        if belts_durability[index+1] > 0 and belts_robot[index] and not belts_robot[index+1]:
            belts_robot[index] = False
            belts_robot[index+1] = True
            belts_durability[index+1] -= 1
            if belts_durability[index+1] == 0:
                zero_count += 1
            belts_robot[exit_point] = False

    if not belts_robot[entry_point] and belts_durability[entry_point] > 0:
        belts_robot[entry_point] = True
        belts_durability[entry_point] -= 1
        if belts_durability[entry_point] == 0:
            zero_count += 1

print(answer)
