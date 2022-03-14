def solution(n, lost, reserve):
    reserve_set = set(reserve)
    lost.sort()

    for index in lost:
        if index in reserve_set:
            lost.remove(index)
            reserve_set.remove(index)

    lost_count = 0
    for index in lost:
        if index in reserve_set:
            reserve_set.remove(index)
            continue
        if index - 1 in reserve_set:
            reserve_set.remove(index - 1)
            continue
        if index + 1 in reserve_set:
            reserve_set.remove(index + 1)
            continue
        lost_count += 1

    answer = n - lost_count
    return answer


n = 5
lost = [1, 2, 4]
reserve = [2, 3]
print(solution(n, lost, reserve))
