# 각 점수 과녁 마다 2가지의 상태가 존재한다
# 어피치가 쏜 화살수+1 개 맞춤 : 점수 획득
# or 0 개 맞춤 : 점수 미획득
from itertools import product


def solution(arrow, info):
    info.reverse()
    appeach_sum = 0
    for score in range(len(info)):
        if info[score] > 0:
            appeach_sum += score

    arrow2score = []
    for index in range(len(info)):
        arrow2score.append(info[index]+1)

    candidates = []
    max_difference = -1 * appeach_sum
    candidates_booleans = list(product([True, False], repeat=11))
    for boolean in candidates_booleans:
        arrow_cost = 0
        candidate_sum = 0
        candidate = []

        # BitMask
        for score in range(len(boolean)):
            if boolean[score]:
                arrow_cost += arrow2score[score]
                candidate_sum += score
                candidate.append(arrow2score[score])
            else:
                candidate.append(0)

        # 화살 개수가 유효한지 확인
        if arrow_cost > arrow:
            continue

        # 남은 화살 0점에 모두 소진
        if arrow - arrow_cost > 0:
            candidate[0] += arrow - arrow_cost

        # 점수 차이가 최고 인지 확인
        score_difference = -1 * appeach_sum
        for score in range(len(boolean)):
            if candidate[score]:
                score_difference += score
                if info[score]:
                    score_difference += score

        if score_difference > max_difference:
            candidates.clear()
            candidates.append(candidate)
            max_difference = score_difference
            continue
        if score_difference == max_difference:
            candidates.append(candidate)
            continue

    # candidates 정렬
    candidates.sort(key=lambda x: (x[0] * -1, x[1] * -1, x[2] * -1, x[3] * -1, x[4] * -1,
                                   x[5] * -1, x[6] * -1, x[7] * -1, x[8] * -1, x[9] * -1, x[10] * -1))
    for index in range(len(candidates)):
        candidates[index].reverse()

    # 점수 차이가 양수인지 확인
    if max_difference <= 0:
        return [-1]

    return candidates[0]


n = 5
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
print(solution(n, info))
