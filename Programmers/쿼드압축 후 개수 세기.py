def split(x, y, n, arr, answer):
    # 정사각형 구역의 크기가 1이면 분할 종료
    if n <= 1:
        item = arr[x][y]
        answer[item] += 1
        return
    # 정사각형 구역의 원소중 다른 값이 존재한다면 4분할
    for nx in range(x, x+n):
        for ny in range(y, y+n):
            if arr[nx][ny] != arr[x][y]:
                split(x, y, n//2, arr, answer)
                split(x+n//2, y, n//2, arr, answer)
                split(x, y+n//2, n//2, arr, answer)
                split(x+n//2, y+n//2, n//2, arr, answer)
                return
    # 정사각형 구역의 원소가 모두 같다면 압축 후 분할 종료
    item = arr[x][y]
    answer[item] += 1
    return


def solution(arr):
    answer = [0, 0]
    x, y = 0, 0
    n = len(arr)
    split(x, y, n, arr, answer)
    return answer


arr = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
print(solution(arr))
