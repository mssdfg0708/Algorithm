# 각 line 의 시작 시간부터 1초간 탐색 한다
# 각 line 의 시작 지점 부터 뒤로 가며 line 이 시작 할때 종료 되지 않은 line 을 체크 한다
# 그 기간 동안 시작 된 처리 의 개수를 확인한다
# 각 line 의 종료 시간 부터 1초간 탐색 한다
# 각 line 의 종료 지점 부터 뒤로 가며 line 이 시작 할때 종료 되지 않은 line 을 체크 한다
# 그 기간 동안 시작 된 처리 의 개수를 확인한다
# 가장 많은 처리 개수 를 출력한다

def convert_end_time(time):
    hour, minute, second = time.split(":")
    hour = int(hour) * 60 * 60 * 1000
    minute = int(minute) * 60 * 1000
    second = int(float(second) * 1000)
    result = hour + minute + second
    return result


def convert_process_time(time):
    time = time[:-1]
    time = float(time)
    time *= 1000
    time = int(time)
    return time


def check_section(root, answer, converted_lines):
    temp = 0
    for start_time, process_time, end_time in converted_lines:
        if start_time < root <= end_time:
            temp += 1
            continue
        if root <= start_time < root + 1000:
            temp += 1
            continue
    answer = max(answer, temp)
    return answer


def solution(lines):
    # 입력 데이터 가공하기
    new_lines = []
    converted_lines = []
    for line in lines:
        new_lines.append(line.split())
    for line in new_lines:
        end_time = convert_end_time(line[1])
        process_time = convert_process_time(line[2])
        start_time = end_time - process_time + 1
        converted_lines.append([start_time, process_time, end_time])

    # 1초 간 구간별 처리량 판별
    answer = 0
    for root_line in converted_lines:
        # 시작 지점 기준 판별
        root = root_line[0]
        answer = check_section(root, answer, converted_lines)
        # 종료 지점 기준 판별
        root = root_line[2]
        answer = check_section(root, answer, converted_lines)

    return answer


lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
    ]
solution(lines)
