import sys

n = int(sys.stdin.readline())

lines = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    lines.append((a, b))

lines.sort()

a_to_b = list(map(lambda x: x[1], lines))

max_length = [1] * n

for i in range(1, n):
    for j in range(i):
        if a_to_b[i] > a_to_b[j]:
            max_length[i] = max(max_length[i], max_length[j] + 1)

print(n - max(max_length))
