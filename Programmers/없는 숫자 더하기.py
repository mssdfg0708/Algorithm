def solution(numbers):
    result = 0
    for num in range(10):
        if num in numbers:
            continue
        result += num
    return result


numbers = [1, 2, 3, 4, 6, 7, 8, 0]
solution(numbers)
