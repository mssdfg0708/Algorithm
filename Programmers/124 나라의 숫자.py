def convert(number_list):
    result = ''
    number_list.reverse()
    for number in number_list:
        if number == 0:
            result += '1'
        if number == 1:
            result += '2'
        if number == 2:
            result += '4'

    return result


def solution(n):
    number_list = []
    while True:
        # 종료 지점 확인
        if n == 1:
            number_list.append(0)
            return convert(number_list)
        if n == 2:
            number_list.append(1)
            return convert(number_list)
        if n == 3:
            number_list.append(2)
            return convert(number_list)

        share = (n-1) // 3
        remainder = (n-1) % 3
        number_list.append(remainder)
        n = share


for n in range(1, 20):
    print(n, ":", solution(n))
