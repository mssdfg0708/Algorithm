n, m = map(int, input().split())
tree_list = list(map(int, input().split()))

max_height = 0
for height in tree_list:
    max_height = max(max_height, height)


def binary_search(low, mid, high):
    while True:
        if mid == low or mid == high:
            print(mid)
            return
        total = 0
        for height in tree_list:
            if height - mid > 0:
                total += (height - mid)
        if total < m:
            high = mid
            mid = (high+low)//2
        if total > m:
            low = mid
            mid = (high+low)//2
        if total == m:
            print(mid)
            return


binary_search(0, max_height//2, max_height)
