def stick(x):
    num = 1
    total_stick = 64
    min_stick = 64

    while total_stick != x:
        min_stick = min_stick / 2
        if total_stick - min_stick > x:
            total_stick = total_stick - min_stick
        elif total_stick - min_stick < x:
            num = num + 1.
        else:
            return int(num)
    return int(num)


x = int(input())
print(stick(x))
