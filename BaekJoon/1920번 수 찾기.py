import sys


# 이분 탐색, 재귀 함수 사용
def solution1():
    n = int(input())
    memory_list = list(map(int, sys.stdin.readline().split()))
    memory_list.sort()

    m = int(input())
    find_list = list(map(int, sys.stdin.readline().split()))

    def binary_search(start, end, target):
        mid = (start + end) // 2
        if target == memory_list[mid]:
            return 1
        if start == end:
            return 0
        if target > memory_list[mid]:
            return binary_search(mid + 1, end, target)
        if target < memory_list[mid]:
            return binary_search(start, mid, target)

    for target in find_list:
        print(binary_search(0, n - 1, target))


# Python Set 자료형 사용
def solution2():
    n = int(input())
    memory_set = set(map(int, sys.stdin.readline().split()))

    m = int(input())
    find_list = list(map(int, sys.stdin.readline().split()))

    for item in find_list:
        if item in memory_set:
            print(1)
        else:
            print(0)
