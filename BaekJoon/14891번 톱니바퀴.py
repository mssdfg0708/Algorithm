# 회전 방향 / 1 = 시계    0 회전 없음   -1 = 반시계
# N극 = 0    S극 = 1
# gear[] 에 4개의 gear 상태 저장 0 - 3
# index 6 은 왼쪽과 닿아있고 index 2 는 오른쪽과 닿아있다. 0 - 7
# 회전이 입력되면 좌측과 우측으로 각각 회전을 전파
# 각 gear 의 회전 방향을 rotation[] 에 저장
# 각 gear 에 대하여 회전 실행

from collections import deque


def check_left(root_gear_num):
    gear_num = root_gear_num
    while gear_num > 0:
        gear_num -= 1
        if gears[gear_num][2] != gears[gear_num + 1][6]:
            list_rotation[gear_num] = list_rotation[gear_num + 1] * -1
            continue
        if gears[gear_num][2] == gears[gear_num + 1][6]:
            break


def check_right(root_gear_num):
    gear_num = root_gear_num
    while gear_num < 3:
        gear_num += 1
        if gears[gear_num][6] != gears[gear_num - 1][2]:
            list_rotation[gear_num] = list_rotation[gear_num - 1] * -1
            continue
        if gears[gear_num][6] == gears[gear_num - 1][2]:
            break


# 회전 방향 / 1 = 시계    0 회전 없음   -1 = 반시계
def execute_rotation():
    for gear_num in range(4):
        if list_rotation[gear_num] == 1:
            status = gears[gear_num].pop()
            gears[gear_num].appendleft(status)
        elif list_rotation[gear_num] == 0:
            pass
        elif list_rotation[gear_num] == -1:
            status = gears[gear_num].popleft()
            gears[gear_num].append(status)


# gear 상태 입력
gears = []
for _ in range(4):
    gear = deque()
    gear_status = input()
    for status in gear_status:
        gear.append(status)
    gears.append(gear)

# 알고리즘 실행
k = int(input())
for _ in range(k):
    list_rotation = [0, 0, 0, 0]
    root_gear_num, root_rotation = map(int, input().split())
    root_gear_num -= 1
    list_rotation[root_gear_num] = root_rotation
    # 왼쪽으로 전파
    check_left(root_gear_num)
    # 오른쪽으로 전파
    check_right(root_gear_num)
    # 회전 실행
    execute_rotation()

# 결과 출력
result = 0
for gear_num in range(4):
    isS = int(gears[gear_num][0])
    if isS:
        result += 2 ** gear_num
print(result)
