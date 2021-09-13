import sys
k, n = map(int, sys.stdin.readline().split())
array = []
for _ in range(k):
    array.append(int(sys.stdin.readline()))
lower_bound, upper_bound = 1, max(array)
result = 0

while lower_bound <= upper_bound:
    mid = (lower_bound + upper_bound) // 2
    count = sum([(i//mid) for i in array])

    if count >= n:
        result = mid
        lower_bound = mid + 1
    elif count < n:
        upper_bound = mid - 1

print(result)
