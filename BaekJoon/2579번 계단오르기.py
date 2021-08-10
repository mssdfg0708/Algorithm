import sys

number = int(input())
score_list = []
dp = []

for i in range(number):
    score_list.append(int(sys.stdin.readline()))

if number == 1:
    print(score_list[0])
elif number == 2:
    print(score_list[0] + score_list[1])
elif number == 3:
    print(max(score_list[0] + score_list[2], score_list[1] + score_list[2]))
else:
    dp.append(score_list[0])
    dp.append(score_list[0] + score_list[1])
    dp.append(max(score_list[0] + score_list[2], score_list[1] + score_list[2]))

    for i in range(3, number):
        dp.append(max(dp[i-2] + score_list[i], dp[i-3] + score_list[i-1] + score_list[i]))

    print(dp[-1])
