import sys

number = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
result = 0

time.sort()

for i in range(len(time)):
    result += time[i] * (len(time) - i)

print(result)
