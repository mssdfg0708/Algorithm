from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
candidates = permutations(arr, len(arr))

answer = 0
for candidate in candidates:
    temp = 0
    for index in range(len(candidate)-1):
        num = abs(candidate[index] - candidate[index+1])
        temp += num
    answer = max(answer, temp)

print(answer)
