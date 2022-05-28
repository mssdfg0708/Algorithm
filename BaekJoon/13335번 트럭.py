import sys
from collections import deque

N, W, L = map(int, sys.stdin.readline().split())
trucks = deque(list(map(int, sys.stdin.readline().split())))

answer = 0
bridge = deque([0 for _ in range(W)])

while trucks:
    bridge.popleft()
    if len(bridge) < W:
        if sum(bridge) + trucks[0] <= L:
            truck = trucks.popleft()
            bridge.append(truck)
        else:
            bridge.append(0)
    answer += 1

answer += W
print(answer)
