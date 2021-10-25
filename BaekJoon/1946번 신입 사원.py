from sys import stdin

t = int(input())
for _ in range(t):
    # 입력 받기
    n = int(input())
    ranks = []
    for _ in range(n):
        ranks.append(list(map(int, stdin.readline().split())))
    ranks.sort()

    # 알고리즘
    passed = 1
    cut_line = ranks[0][1]
    for i in range(1, len(ranks)):
        if ranks[i][1] > cut_line:
            pass
        else:
            cut_line = ranks[i][1]
            passed += 1
    print(passed)
