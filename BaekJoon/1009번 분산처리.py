import sys


def sol1():
    T = int(input())
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().split())
        list_b = [4, 1, 2, 3]
        last_num = a % 10
        b %= 4
        b = list_b[b]
        if b > 1:
            for _ in range(b - 1):
                last_num *= a
                last_num %= 10
        if last_num == 0:
            print(10)
        else:
            print(last_num)


def sol2():
    table = [[10, 10, 10, 10],
             [1, 1, 1, 1],
             [2, 4, 8, 6],
             [3, 9, 7, 1],
             [4, 6, 4, 6],
             [5, 5, 5, 5],
             [6, 6, 6, 6],
             [7, 9, 3, 1],
             [8, 4, 2, 6],
             [9, 1, 9, 1]]
    T = int(input())
    for _ in range(T):
        a, b = map(int, sys.stdin.readline().split())
        a %= 10
        b = (b - 1) % 4
        print(table[a][b])
