from collections import deque


def convert_time(time):
    hour, minute = time.split(':')
    result = int(hour)*60 + int(minute)
    return result


def convert_minute(answer_minute):
    hour = str(answer_minute // 60)
    minute = str(answer_minute % 60)

    if len(hour) == 1:
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute

    result = hour + ":" + minute

    return result


def make_bus_time(count_limit, interval):
    result = []
    for count in range(count_limit):
        time = 540 + count * interval
        if count >= 1440:
            break
        result.append(time)

    return result


def target_safe(new_timetable, bus_time, m):
    wait_table = deque()
    time_table = deque()
    for time in new_timetable:
        time_table.append(time)
    bus_table = deque()
    for time in bus_time:
        bus_table.append(time)

    while bus_table:
        next_bus = bus_table.popleft()
        crew_count = 0
        while time_table and time_table[0][0] <= next_bus:
            target = time_table.popleft()
            wait_table.append(target)
        while crew_count < m and wait_table:
            crew_count += 1
            crew = wait_table.popleft()
            if crew[1]:
                return True

    return False


def solution(n, t, m, old_timetable):
    answer_minute = 0
    root_timetable = []
    for time in old_timetable:
        minute = convert_time(time)
        root_timetable.append([minute, False])

    root_timetable.sort()

    bus_time = make_bus_time(n, t)

    for minute in range(0, 1440):
        new_timetable = []
        for time, isTarget in root_timetable:
            new_timetable.append([time, isTarget])

        for index in range(len(new_timetable)):
            if new_timetable[index][0] > minute:
                new_timetable.insert(index, [minute, True])
                break
            if index == len(new_timetable) - 1:
                new_timetable.append([minute, True])
                break

        if target_safe(new_timetable, bus_time, m):
            answer_minute = minute

    answer = convert_minute(answer_minute)
    return answer


input_n = 2
input_t = 10
input_m = 2
timetable = ["09:10", "09:09", "08:00"]
print(solution(input_n, input_t, input_m, timetable))

# HH:MM 은 1-1440 사이의 숫자로 변환
# 버스 도착 시간 목록
# timetable 변형
# [시간, Boolean] / target.boolean = True
# 만약 탑승객중 target.boolean ==  True 라면
# 탑승 시간 갱신
# 23:59 까지 반복
