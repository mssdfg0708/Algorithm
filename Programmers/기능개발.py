# progress 배열 뒤집기
# 가장 앞의 process 완료 여부 확인
# 바로 뒤의 process 가 완료 되어 있다면 같이 배포
# while progress 동안 반복
import math


def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()

    while progresses:
        # 가장 뒤의 progress 완료 날짜 계산
        temp_cost = (100 - progresses[-1]) / speeds[-1]
        cost = math.ceil(temp_cost)

        # 전체 progresses 계산
        for i in range(len(progresses)):
            progresses[i] += speeds[i] * cost

        # 완료된 작업 개수 파악
        count = 0
        while progresses and progresses[-1] >= 100:
            progresses.pop()
            speeds.pop()
            count += 1

        answer.append(count)

    return answer


progress, speeds = [20, 99, 93, 30, 55, 10], [5, 10, 1, 1, 30, 5]
print(solution(progress, speeds))
