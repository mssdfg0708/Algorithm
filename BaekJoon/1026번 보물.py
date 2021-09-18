import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

answer = 0
a.sort()
for i in range(n):
    x = a[i]
    y = b.pop(b.index(max(b)))
    answer += x * y

print(answer)
