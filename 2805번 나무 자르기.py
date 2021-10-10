n, m = map(int, input().split())
tree_list = list(map(int, input().split()))

max_height = 0
for height in tree_list:
    max_height = max(max_height, height)

low, high = 0, max_height

while low <= high:
    mid = (low+high) // 2
    total = 0
    for height in tree_list:
        if height >= mid:
            total += height - mid

    if total >= m:
        low = mid + 1
    else:
        high = mid - 1

print(high)
