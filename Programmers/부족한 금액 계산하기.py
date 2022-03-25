def solution(price, money, count):
    total = 0
    for c in range(count):
        total += (c + 1) * price

    answer = total - money
    if answer < 0:
        answer = 0

    return answer


input_price = 3
input_money = 20
input_count = 4
print(solution(input_price, input_money, input_count))
