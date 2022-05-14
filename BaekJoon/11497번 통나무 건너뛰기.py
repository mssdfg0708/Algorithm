from sys import stdin


test = int(stdin.readline())

for _ in range(test):
    n = int(stdin.readline())
    heights = [int(x) for x in stdin.readline().split()]
    heights.sort()

    max_level = 0
    for i in range(2, n):
        max_level = max(max_level, abs(heights[i] - heights[i - 2]))

    print(max_level)
