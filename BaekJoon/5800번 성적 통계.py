import sys

Num = int(sys.stdin.readline().strip())
for num in range(Num):
    score_list = list(map(int, sys.stdin.readline().split()))[1:]
    min_score = 999
    max_score = -1

    for score in score_list:
        min_score = min(min_score, score)
        max_score = max(max_score, score)

    score_list.sort(reverse=True)
    largest_gap = 0
    for index in range(len(score_list)-1):
        gap = abs(score_list[index] - score_list[index+1])
        largest_gap = max(largest_gap, gap)

    print("Class %d" % (num+1))
    print("Max %d, Min %d, Largest gap %d" % (max_score, min_score, largest_gap))
