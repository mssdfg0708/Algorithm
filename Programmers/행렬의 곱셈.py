def calculate(x, y, arr1, arr2):
    result = 0
    for index in range(len(arr2)):
        result += arr1[x][index] * arr2[index][y]
    return result


def solution(arr1, arr2):
    x_range = len(arr1)
    y_range = len(arr2[0])
    answer = [[0 for _ in range(y_range)] for _ in range(x_range)]

    for x in range(x_range):
        for y in range(y_range):
            result = calculate(x, y, arr1, arr2)
            answer[x][y] = result

    return answer


input_arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
input_arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(input_arr1, input_arr2))
