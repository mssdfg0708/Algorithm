def solution(n, stages):
    failed_nums = [0 for _ in range(n + 2)]
    for stage in stages:
        failed_nums[stage] += 1

    reached_num = len(stages)
    failure_list = [[0, stage] for stage in range(n + 1)]

    for index in range(len(failed_nums) - 1):
        failed_num = failed_nums[index]
        if failed_num > 0:
            failure_list[index][0] = failed_num / reached_num
            reached_num -= failed_num

    failure_list.sort(key=lambda x: (-1 * x[0], x[1]))

    answer = []
    for failure, stage in failure_list:
        if stage == 0:
            continue
        answer.append(stage)

    return answer


input_n = 5
input_stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(input_n, input_stages)
