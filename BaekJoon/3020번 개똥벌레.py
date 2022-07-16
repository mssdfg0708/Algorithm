import sys

W, H = map(int, sys.stdin.readline().split())
minus_obstacle_height = [0 for _ in range(H)]
add_obstacle_height = [0 for _ in range(H)]

for _ in range(W//2):
    height = int(sys.stdin.readline().rstrip())
    minus_obstacle_height[height] += 1

    height = int(sys.stdin.readline().rstrip())
    add_obstacle_height[H-height] += 1


crash = W//2
min_crash = crash
duplicate_counter = 1
for height in range(1, H):
    crash -= minus_obstacle_height[height]
    crash += add_obstacle_height[height]
    if crash < min_crash:
        duplicate_counter = 1
        min_crash = crash
        continue
    if crash == min_crash:
        duplicate_counter += 1

print(min_crash, duplicate_counter)
