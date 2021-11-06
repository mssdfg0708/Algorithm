def solution(numbers, hand):
    answer = ''
    # 각 숫자의 x, y 좌표를 따로 저장
    target_x = [3, 0, 0, 0, 1, 1, 1, 2, 2, 2]
    target_y = [1, 0, 1, 2, 0, 1, 2, 0, 1, 2]
    # right hand, left hand 의 초기 x, y 값
    right_x, right_y = 3, 2
    left_x, left_y = 3, 0

    # numbers 의 각 number 마다 반복
    for target in numbers:

        if target == 3 or target == 6 or target == 9:
            right_x = target_x[target]
            right_y = target_y[target]
            answer += 'R'
            continue
        if target == 1 or target == 4 or target == 7:
            left_x = target_x[target]
            left_y = target_y[target]
            answer += 'L'
            continue

        right_cost = abs(right_x - target_x[target]) + abs(right_y - target_y[target])
        left_cost = abs(left_x - target_x[target]) + abs(left_y - target_y[target])

        if right_cost > left_cost:
            left_x = target_x[target]
            left_y = target_y[target]
            answer += 'L'
            continue
        if right_cost == left_cost and hand == "right":
            right_x = target_x[target]
            right_y = target_y[target]
            answer += 'R'
            continue
        if right_cost == left_cost and hand == "left":
            left_x = target_x[target]
            left_y = target_y[target]
            answer += 'L'
            continue
        if right_cost < left_cost:
            right_x = target_x[target]
            right_y = target_y[target]
            answer += 'R'
            continue

    print(answer)
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
solution(numbers, hand)
