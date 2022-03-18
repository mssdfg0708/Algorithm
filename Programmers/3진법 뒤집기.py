def solution(n):
    three_notation = []

    while n:
        remainder = n % 3
        three_notation.append(remainder)
        n = n // 3

    index_zero = 0
    for num in three_notation:
        if num != 0:
            break
        index_zero += 1

    three_notation = three_notation[index_zero:]
    three_notation.reverse()

    answer = 0
    numerical_index = 1
    for num in three_notation:
        answer += num * numerical_index
        numerical_index *= 3

    return answer


input_n = 125
solution(input_n)
