import sys

n = int(input())
A = list(map(int,sys.stdin.readline().split()))
m = int(input())
B = list(map(int,sys.stdin.readline().split()))

A.sort()

def bs(num, bound):
    start, end = 0, n
    while(start < end):
        mid = (start + end) // 2
        if bound == 0:
            if A[mid] < num:
                start = mid + 1
            else:
                end = mid
        else:
            if A[mid] <= num:
                start = mid + 1
            else:
                end = mid
    return end

result = []
answer = ''
for i in B:
    result.append(bs(i,1) - bs(i,0))
for item in result:
    answer += str(item) + ' '
print(answer[:-1])
