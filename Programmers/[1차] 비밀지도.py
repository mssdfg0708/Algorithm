def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    for num in arr1:
        binary_code = bin(num)[2:]
        binary_code = binary_code.zfill(n)
        map1.append(binary_code)

    for num in arr2:
        binary_code = bin(num)[2:]
        binary_code = binary_code.zfill(n)
        map2.append(binary_code)

    result = ['' for _ in range(n)]
    for x in range(n):
        for y in range(n):
            code = int(map1[x][y]) | int(map2[x][y])
            if code:
                result[x] += '#'
            else:
                result[x] += ' '

    return result


input_n = 5
input_ar1 = [9, 20, 28, 18, 11]
input_arr2 = [30, 1, 21, 17, 28]
print(solution(input_n, input_ar1, input_arr2))
