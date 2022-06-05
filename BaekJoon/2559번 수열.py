import sys

n, k = map(int, sys.stdin.readline().split())
temperatures = list(map(int, sys.stdin.readline().split()))

temperature_sum = 0
for index in range(k):
    temperature_sum += temperatures[index]

answer = temperature_sum
for index in range(k, n):
    temperature_sum -= temperatures[index-k]
    temperature_sum += temperatures[index]
    if temperature_sum > answer:
        answer = temperature_sum

print(answer)
