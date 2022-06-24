import sys

length = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline().strip())

answer = 0
need_nums = set()
for item in arr:
    if item in need_nums:
        answer += 1
        need_nums.remove(item)
        continue
    need_num = target - item
    need_nums.add(need_num)

print(answer)
