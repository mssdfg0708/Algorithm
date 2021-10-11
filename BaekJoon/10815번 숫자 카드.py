import sys

n = int(input())
s = list(map(int, sys.stdin.readline().split()))
m = int(input())
s_ = list(map(int, sys.stdin.readline().split()))
s.sort()

for i in s_:
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if 0 <= mid < n:
            if s[mid] < i: low = mid + 1
            else: high = mid - 1
        else: break
    if 0 <= high + 1 < n:
        if s[high + 1] == i: print(1, end=" ")
        else: print(0, end=" ")
    else: print(0, end=" ")
