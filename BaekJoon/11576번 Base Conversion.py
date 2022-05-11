cur_base, next_base = map(int, input().split())
dummy = input()
numbers = list(map(int, input().split()))
numbers.reverse()

target_number = 0
for index in range(len(numbers)):
    number = numbers[index]
    target_number += number * (cur_base ** index)

answer_list = []
while target_number:
    answer_list.append(target_number % next_base)
    target_number = target_number // next_base

answer_list.reverse()
for item in answer_list:
    print(item, end=' ')
