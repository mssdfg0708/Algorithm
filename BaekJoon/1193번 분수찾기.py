iter_target = int(input())

num_sum = 2
next_iter = 1
x, y = 1, 1

while True:
    if iter_target - next_iter <= 0:
        x = num_sum - iter_target
        y = iter_target
        if num_sum % 2 == 1:
            x, y = y, x
        break
    iter_target -= next_iter
    next_iter += 1
    num_sum += 1

print(str(x) + "/" + str(y))
