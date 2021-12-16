from collections import deque


def solution(bridge_length, weight, truck_weights):
    passing_q = deque()
    passed_q = []
    wait_q = deque()
    for item in truck_weights:
        wait_q.append(item)

    time = 1
    bridge_weight = 0
    while len(passed_q) < len(truck_weights):
        # 트럭 출발 가능한지 확인 이후 출발
        if wait_q and bridge_weight + wait_q[0] <= weight:
            truck = wait_q.popleft()
            passing_q.append([truck, 0])
            bridge_weight += truck
        # 시간 경과
        time += 1
        for i in range(len(passing_q)):
            passing_q[i][1] += 1
        # 도착한 트럭 확인
        if passing_q[0][1] >= bridge_length:
            truck, local_time = passing_q.popleft()
            bridge_weight -= truck
            passed_q.append(truck)

    return time


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))
