n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = arr[(n - 1) // 2]

print(answer)
