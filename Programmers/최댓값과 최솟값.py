def solution(s):
    numbers = list(map(int, s.split()))
    num_min = min(numbers)
    num_max = max(numbers)
    answer = str(num_min) + " " + str(num_max)

    return answer


s = "-1 2 -3 4"
solution(s)
