from collections import deque
import heapq


def solution(jobs):
    jobs.sort()

    job_queue = deque()
    for item in jobs:
        job_queue.append(item)

    total_cost_sum = 0
    total_cost_divide = len(job_queue)
    current_time = 0
    wait_heap = []

    # 만약 처리 대기중인 작업이 있다면 진행
    while job_queue or wait_heap:
        # 현재 이전에 요청된 작업이 있는지 확인
        while job_queue and job_queue[0][0] <= current_time:
            start_time, cost_time = job_queue.popleft()
            wait_time = current_time - start_time
            heapq.heappush(wait_heap, [cost_time, start_time, wait_time])

        # 대기중인 작업이 있으면 수행
        if wait_heap:
            cost_time, start_time, wait_time = heapq.heappop(wait_heap)
            current_time += cost_time
            total_cost_sum += current_time - start_time
        # 대기중인 작업이 없다면 시간 점프
        else:
            current_time = job_queue[0][0]

    answer = total_cost_sum // total_cost_divide
    return answer


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
