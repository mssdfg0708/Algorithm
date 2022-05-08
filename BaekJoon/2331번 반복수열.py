import sys


def get_next_num(num, exponent):
    next_num = 0
    for item in num:
        next_num += int(item) ** exponent

    next_num = str(next_num)
    return next_num


num, exponent = sys.stdin.readline().split()
exponent = int(exponent)
num_count = 0
num_list = []

while num not in num_list:
    num_list.append(num)
    num = get_next_num(num, exponent)

answer = []
for item in num_list:
    if item == num:
        break
    answer.append(item)

print(len(answer))
