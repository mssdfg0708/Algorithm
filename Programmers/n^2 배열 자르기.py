# 1 <= n <= 10^7 이므로 10^7행 10^7열을 가지는 2차원 배열을 만들수 없다 (시간복잡도)
# right - left = 10^5 를 이용해야 한다
# n = 3 / left = 2 / right = 5 [[1,2,3],[2,2,3],[3,3,3]]
# row = right // n
# col = right % n

def solution(n, left, right):
    arr = []
    for index in range(left, right+1):
        row, col = index // n, index % n
        item = max(row, col) + 1
        arr.append(item)

    return arr


n = 3
left, right = 2, 5
print(solution(n, left, right))
