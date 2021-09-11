# 재생 시작 시각 list(sort)
# 재생 종료 시각 list(sort)
# 재생 길이 만큼의 배열(watching) 0 으로 초기화
# watching 보는 사람의 수를 증감하며 입력
# 광고 시작 가능 시각 설정
# 재생 시작 시각 list 를 순회하며 광고 시작 시각을 그 값으로 지정
# 매 초 마다 watching 의 값을 더해서 result에 입력
# max(result) 출력
def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)        # 1
    adv_time = str_to_int(adv_time)
    all_time = [0 for i in range(play_time + 1)]

    for l in logs:                           # 2
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):       # 3
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):       # 4
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0                           # 5
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s
