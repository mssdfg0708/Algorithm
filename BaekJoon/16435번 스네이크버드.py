import sys

n, length = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort()

for i in range(n):
    if length < arr[i]:
        break
    length += 1

print(length)
