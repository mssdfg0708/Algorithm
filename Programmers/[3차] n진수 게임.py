def solution(n, t, m, p):
    orders = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              'A', 'B', 'C', 'D', 'E', 'F']
    order_index_list = [0]
    result = ""
    for _ in range(t*m):
        num = ""
        for order_index in order_index_list:
            num += orders[order_index]
        reverse = num[::-1]
        result += reverse
        order_index_list[0] += 1

        index = 0
        while index < len(order_index_list):
            if order_index_list[index] < n:
                break
            order_index_list[index] = 0
            index += 1
            if index >= len(order_index_list):
                order_index_list.append(1)
                break
            order_index_list[index] += 1

    answer = ""
    for count in range(t):
        answer += result[count*m + p-1]
    return answer


n, t, m, p = 16, 16, 2, 1
print(solution(n, t, m, p))
