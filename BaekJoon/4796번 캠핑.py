case = 0
while True:
    case += 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    use = V//P * L
    remain_day = V - V//P * P
    if remain_day >= L:
        use += L
    else:
        use += remain_day
    print("Case", case, end='')
    print(":", use)
