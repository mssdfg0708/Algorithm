# append 코드
def solution(n):
    fibonacci = [0, 1, 1]
    for index in range(2, n):
        fibonacci.append(fibonacci[index] + fibonacci[index-1])

    fibo_num = fibonacci[n]
    return fibo_num % 1234567


# index 값 변경 코드
# def solution(n):
#     fibonacci = [0 for _ in range(n+1)]
#     fibonacci[1] = 1
#     fibonacci[2] = 1
#     for index in range(3, n+1):
#         fibonacci[index] = fibonacci[index-1] + fibonacci[index-2]
#
#     fibo_num = fibonacci[n]
#     return fibo_num % 1234567


print(solution(99999))


"""
append 코드
테스트 13 〉	통과 (335.12ms, 456MB)
테스트 14 〉	통과 (320.46ms, 439MB)

index 값 변경 코드
테스트 13 〉	통과 (356.38ms, 456MB)
테스트 14 〉	통과 (344.67ms, 439MB)

append 코드가 성능상 조금 우세하다
"""