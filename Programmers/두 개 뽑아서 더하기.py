def solution(numbers):

    answer_set = set()
    for index1 in range(len(numbers)):
        for index2 in range(len(numbers)):
            if index1 == index2:
                continue
            num1 = numbers[index1]
            num2 = numbers[index2]
            answer_set.add(num1 + num2)

    answer = list(answer_set)
    answer.sort()
    return answer


in_numbers = [5, 0, 2, 7]
print(solution(in_numbers))
