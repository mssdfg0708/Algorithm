def solution(sizes):
    for size in sizes:
        size.sort()

    max_width = -1
    max_height = -1
    for width, height in sizes:
        max_width = max(max_width, width)
        max_height = max(max_height, height)

    answer = max_width * max_height
    return answer


input_sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(input_sizes))
