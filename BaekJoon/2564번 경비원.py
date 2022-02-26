n, m = map(int, input().split())
a = int(input())
info_list = []


def find_distance(x1, y1, x2, y2):
    # 북
    if x1 == 1:
        if x2 == 1:
            return abs(y1 - y2)
        if x2 == 2:
            return min((y1 + y2 + m), ((2 * n) + m - y1 - y2))
        if x2 == 3:
            return y1 + y2
        if x2 == 4:
            return n - y1 + y2
    # 남
    if x1 == 2:
        if x2 == 1:
            return min((y1 + y2 + m), ((2 * n) + m - y1 - y2))
        if x2 == 2:
            return abs(y1 - y2)
        if x2 == 3:
            return y1 + m - y2
        if x2 == 4:
            return n + m - y1 - y2
    # 서
    if x1 == 3:
        if x2 == 1:
            return y1 + y2
        if x2 == 2:
            return m - y1 + y2
        if x2 == 3:
            return abs(y1 - y2)
        if x2 == 4:
            return min((y1 + y2 + n), ((2 * m) + n - y1 - y2))
    # 동
    if x1 == 4:
        if x2 == 1:
            return n + y1 - y2  #
        if x2 == 2:
            return m - y2 + n - y1
        if x2 == 3:
            return min((y1 + y2 + n), ((2 * m) + n - y1 - y2))
        if x2 == 4:
            return abs(y1 - y2)


for i in range(a):
    b, c = map(int, input().split())
    info_list.append((b, c))

x, y = map(int, input().split())
res = 0

for i in info_list:
    res += find_distance(x, y, i[0], i[1])

print(res)
