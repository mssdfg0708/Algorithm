def solution(id_list, reports, k):
    report_log = dict()
    for user_id in id_list:
        report_log[user_id] = set()

    for r in reports:
        user_id, reported_id = r.split()
        report_log[user_id].add(reported_id)

    reported_count = dict()
    for user_id in id_list:
        reported_count[user_id] = 0

    for key, value in report_log.items():
        for reported_id in value:
            reported_count[reported_id] += 1

    answer = []
    for key, value in report_log.items():
        num = 0
        for user_id in value:
            if reported_count[user_id] >= k:
                num += 1
        answer.append(num)

    return answer


input_id_list = ["muzi", "frodo", "apeach", "neo"]
input_report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "muzi frodo"]
input_k = 2
print(solution(input_id_list, input_report, input_k))
