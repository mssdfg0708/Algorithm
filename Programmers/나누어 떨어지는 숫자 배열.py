def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)

    if not answer:
        answer.append(-1)
    answer.sort()

    return answer


input_arr = [5, 9, 7, 10]
input_divisor = 5
print(solution(input_arr, input_divisor))
