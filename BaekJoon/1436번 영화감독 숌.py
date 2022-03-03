target_index = int(input()) - 1

end_list = []
target = 0

while True:
    if len(end_list) > target_index:
        break
    num = str(target)
    if '666' in num:
        end_list.append(num)
    target += 1

print(end_list[target_index])
