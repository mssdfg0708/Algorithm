import sys

N = int(sys.stdin.readline().strip())
num_list = []
num_dict = dict()
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    string_num = str(num)
    num_list.append(num)

    if string_num not in num_dict:
        num_dict[string_num] = 1
    else:
        num_dict[string_num] += 1

# 산술 평균
average = round(sum(num_list) / N)
print(average)

# 중앙값
num_list.sort()
mid_num = num_list[N//2]
print(mid_num)

# 최빈값
max_count = 0
arr = []
for num, count in num_dict.items():
    num = int(num)
    if count > max_count:
        arr.clear()
        arr.append(num)
        max_count = count
        continue
    if count == max_count:
        arr.append(num)
        continue

arr.sort()
if len(arr) == 1:
    print(arr[0])
else:
    print(arr[1])

# 범위
max_num = max(num_list)
min_num = min(num_list)
print(max_num - min_num)
