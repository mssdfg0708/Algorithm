# sum = start 부터 end 까지의 총합
def solution(num):
    answer = 0
    sum = 0
    start = 1
    for end in range(1, num+1):
        sum += end
        while sum > num:
            sum -= start
            start += 1
        if sum == num:
            answer += 1

    return answer


num = 15
print(solution(num))
