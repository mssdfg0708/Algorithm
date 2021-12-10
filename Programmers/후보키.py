def check_unique(arr, row):
    return True if len(set(zip(*arr))) == row else False


def check_min(num, unique):
    for i in unique:
        if i & num == i: return False
    return True


def solution(relation):
    relation = tuple(zip(*relation))
    col = len(relation)
    row = len(relation[0])
    candidate = []

    for num in range(1, 1 << col):
        tmp = tuple(relation[i] for i in range(col) if num & (1 << i))

        if check_unique(tmp, row) and check_min(num, candidate):
            candidate.append(num)

    return len(candidate)


relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
solution(relation)
