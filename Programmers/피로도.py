from itertools import permutations


def solution(k, dungeons):
    orders = list(permutations(range(len(dungeons)), len(dungeons)))
    result = []
    for order in orders:
        fatigue = k
        count = 0
        for o in order:
            if fatigue < dungeons[o][0]:
                break
            fatigue -= dungeons[o][1]
            count += 1
        result.append(count)

    answer = max(result)
    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))
