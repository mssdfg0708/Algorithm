def solution(n):
    binary_root = str(bin(n))
    root_count = binary_root.count('1')

    answer = n
    answer_count = -1
    while answer_count != root_count:
        answer += 1
        binary_answer = str(bin(answer))
        answer_count = binary_answer.count('1')

    return answer


n = 78
print(solution(n))
