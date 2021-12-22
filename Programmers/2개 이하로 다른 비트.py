# 시간 초과 코드
def solution1(numbers):
    answer = []
    # numbers 안의 각 num 마다 알고리즘 실행
    for num in numbers:
        offset = 0
        while True:
            offset += 1
            candidate = num + offset
            result = str(bin(num ^ candidate))
            # 종료 조건
            if result.count('1') <= 2:
                answer.append(candidate)
                break

    # 결과 반환
    return answer


# 시간복잡도 해결 코드
def solution2(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'

        if number % 2 == 1:
            bin_number[idx + 1] = '0'

        answer.append(int(''.join(bin_number), 2))

    return answer


numbers = [2, 7]
solution2(numbers)
