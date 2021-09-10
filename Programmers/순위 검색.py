from bisect import bisect_left
from itertools import combinations


# 기존 버전
def solution1(info, query):
    answer = []
    table = []
    for s in info:
        table.append(list(s.split()))
    for s in query:
        count = 0
        query_li = list(s.split())
        for language, task, period, food, score in table:
            if query_li[0] != '-' and query_li[0] != language:
                continue
            if query_li[2] != '-' and query_li[2] != task:
                continue
            if query_li[4] != '-' and query_li[4] != period:
                continue
            if query_li[6] != '-' and query_li[6] != food:
                continue
            if int(query_li[7]) <= int(score):
                count += 1
        answer.append(count)
    return answer


# solution2 에서 사용될 함수
def make_all_cases(temp):
    cases = []
    for k in range(5):
        for li in combinations([0, 1, 2, 3], k):
            case = ''
            for idx in range(4):
                if idx not in li:
                    case += temp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases


# 성능 개선 버전
def solution2(info, query):
    answer = []
    all_people = {}
    for i in info:
        separate_info = i.split()
        cases = make_all_cases(i.split())
        for case in cases:
            if case not in all_people.keys(): all_people[case] = [int(separate_info[4])]
            else: all_people[case].append(int(separate_info[4]))

    for key in all_people.keys():
        all_people[key].sort()

    for q in query:
        separate_q = q.split()
        target = separate_q[0] + separate_q[2] + separate_q[4] + separate_q[6]
        if target in all_people.keys():
            answer.append(len(all_people[target]) - bisect_left(all_people[target], int(separate_q[7]), lo=0, hi=len(all_people[target])))
        else:
            answer.append(0)

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210",
        "python frontend senior chicken 150", "cpp backend senior pizza 260",
        "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
         "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution2(info, query))
