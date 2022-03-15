def solution(nums):
    max_type = len(nums) // 2
    pocketmon_type = set(nums)

    answer = min(max_type, len(pocketmon_type))
    return answer


input_nums = [3, 3, 3, 2, 2, 2]
solution(input_nums)
