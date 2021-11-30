# 시간 초과 나는 알고리즘
def solution01(n, times):
    # # Generate lcm
    # gcd = 1
    # for index in range(len(times) - 1):
    #     if index == 0:
    #         gcd = math.gcd(times[index], times[index + 1])
    #         break
    #     gcd = math.gcd(gcd, times[index + 1])
    #
    # lcm_list = list()
    # for index in range(len(times)):
    #     lcm_list.append(times[index]//gcd)
    # lcm = gcd
    # for item in lcm_list:
    #     lcm *= item
    # # Generate lcm End
    lcm = 1
    for item in times:
        lcm *= item

    ratio_list = list()
    for index in range(len(times)):
        ratio_list.append(lcm//times[index])

    multiple = n // sum(ratio_list)
    wait_list = []
    for index in range(len(times)):
        wait_list.append(ratio_list[index]*multiple)

    people = n - sum(wait_list)
    while people > 0:
        candidates = []
        for index in range(len(wait_list)):
            candidates.append((wait_list[index] + 1) * times[index])
        sol = candidates.index(min(candidates))
        wait_list[sol] += 1
        people -= 1

    result = []
    for index in range(len(wait_list)):
        result.append(wait_list[index] * times[index])
    return max(result)


# 정답 알고리즘
# N분에 심사 완료되는 사람의 수를 이용하여 많고 적음을 판별
# 시간(N)을 이분 탐색한다
def solution02(n, times):
    answer = 0
    # right 는 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우이다.
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            # people 은 모든 심사관들이 mid 분 동안 심사한 사람의 수
            people += mid // time
            # 모든 심사관을 거치지 않아도 mid 분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if people >= n:
                break

        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        elif people < n:
            left = mid + 1

    return answer


n = 30
times = [5, 7, 10]
print(solution02(n, times))
