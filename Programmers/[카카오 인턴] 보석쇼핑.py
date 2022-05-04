def solution(gems):
    gems_index = dict()
    for gem in gems:
        if gem not in gems_index:
            gems_index[gem] = -1

    gem_type_count = len(gems_index)

    trigger_index = -1
    min_length = 987654321
    answer = []
    gem_count = 0
    for index in range(len(gems)):
        gem = gems[index]
        if gems_index[gem] == -1:
            gem_count += 1

        modified_index = gems_index[gem]
        gems_index[gem] = index + 1

        if gem_count < gem_type_count:
            continue

        if trigger_index == -1 or modified_index == trigger_index:
            min_index = 987654321
            max_index = -1
            for key, value in gems_index.items():
                min_index = min(min_index, value)
                max_index = max(max_index, value)
            trigger_index = min_index

            length = max_index - min_index + 1
            if length < min_length:
                min_length = length
                answer = [min_index, max_index]

    return answer


input_gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA", "RUBY"]
print(solution(input_gems))
# gems_index = dict() 에 각 gem 이 마지막으로 발견된 지점 저장 (초기값 -1)
