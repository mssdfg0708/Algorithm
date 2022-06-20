offset = int(input())
arr = []
max_data = [(0, 0), (0, 0)]

for index in range(6):
    direction, w = map(int, input().split())
    direction = 0 if direction <= 2 else 1
    if w > max_data[direction][1]:
        max_data[direction] = (index, w)
    arr.append((direction, w))

max_area = max_data[0][1] * max_data[1][1]
check = [False] * 6
for idx, dummy in max_data:
    for index in idx, (idx + 1) % 6, idx - 1:
        check[index] = True

min_area = 1
for index in range(6):
    if not check[index]:
        min_area *= arr[index][1]
print((max_area - min_area) * offset)
