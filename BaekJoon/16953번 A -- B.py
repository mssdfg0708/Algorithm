initiate_num, target_num = map(int, input().split())

count = 1
while target_num > initiate_num:
    count += 1
    target_string = str(target_num)

    if target_string[-1] == '1':
        target_string = target_string[:-1]
        target_num = int(target_string)
    elif (target_num % 10) % 2 == 0:
        target_num = target_num // 2
    else:
        break

if target_num == initiate_num:
    print(count)
else:
    print(-1)
