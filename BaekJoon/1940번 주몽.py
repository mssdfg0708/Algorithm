import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.sort()

answer = 0
start, end = 0, N-1

while start < end:
    if nums[start] + nums[end] == M:
        answer += 1
        start += 1
        end -= 1
    elif nums[start] + nums[end] < M:
        start += 1
    else:
        end -= 1

print(answer)
