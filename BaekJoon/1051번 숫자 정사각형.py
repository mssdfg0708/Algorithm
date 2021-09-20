import sys

n, m = map(int, sys.stdin.readline().split())
arr = []

for _ in range(n):
    arr.append([int(x) for x in sys.stdin.readline().rstrip()])

dist = 0

for row in range(n - 1):
    for col in range(m - 1):
        x = arr[row][col]
        i = min(n - row, m - col) - 1
        while i > dist:
            if arr[row][col + i] == x and arr[row + i][col] == x and arr[row + i][col + i] == x:
                dist = i
            i -= 1

print((dist + 1) * (dist + 1))
