w, h = map(int, input().split())
heights = list(map(int, input().split()))

answer = 0
for index in range(len(heights)):
    height = heights[index]
    max_left = 0
    max_right = 0

    for idx in range(index, -1, -1):
        if heights[idx] > max_left:
            max_left = heights[idx]

    for idx in range(index, len(heights)):
        if heights[idx] > max_right:
            max_right = heights[idx]

    base = min(max_left, max_right)
    water = base - height
    if water < 0:
        water = 0
    answer += water

print(answer)
