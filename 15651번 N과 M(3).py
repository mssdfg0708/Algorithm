# 'dfs 버전'과 'itertools 버전' 2가지로 해결 했습니다
from itertools import *


def use_dfs():
    max_n, max_depth = map(int, input().split())
    result = []

    def dfs(depth, n):
        if depth > max_depth:
            for item in result:
                print(item, end = ' ')
            print()
            return
        for n in range(n, max_n + 1):
            result.append(n)
            dfs(depth + 1, 1)
            result.pop()

    dfs(1, 1)             


def use_itertools():
    max_n, max_depth = map(int, input().split())
    list_n = [n for n in range (1, max_n+1)]

    for tuple in product(list_n, repeat = max_depth):
        for item in tuple:
            print(item, end = ' ')
        print()
