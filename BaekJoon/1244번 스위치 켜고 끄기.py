# 남1 여2
import sys

dummy = int(input())
switch_input = list(map(int, sys.stdin.readline().split()))
switch_list = [-1]
for item in switch_input:
    if item == 0:
        switch_list.append(False)
    else:
        switch_list.append(True)

num = int(input())
for _ in range(num):
    gender, switch = map(int, input().split())
    # 남자 인 경우
    if gender == 1:
        for i in range(len(switch_list)):
            if i % switch == 0:
                switch_list[i] = not switch_list[i]
    # 여자 인 경우
    else:
        i = switch
        left = i-1
        right = i+1
        switch_list[i] = not switch_list[i]
        if left > 0 and right < len(switch_list):
            while switch_list[left] == switch_list[right]:
                switch_list[left] = not switch_list[left]
                switch_list[right] = not switch_list[right]
                left -= 1
                right += 1
                if left <= 0 or right >= len(switch_list):
                    break

for i in range(1, len(switch_list)):
    if switch_list[i]:
        print(1, end=' ')
    else:
        print(0, end=' ')
    if i % 20 == 0:
        print()


