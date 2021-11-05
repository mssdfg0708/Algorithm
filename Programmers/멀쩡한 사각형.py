def find_gcd(num1, num2):
    gcd = -1
    for i in range(1, num1 + 1):
        if (num1 % i == 0) & (num2 % i == 0):
            gcd = i

    return gcd


def solution(w, h):
    if w != h:
        gcd = find_gcd(w, h)
    else:
        gcd = w
    unit_w = w//gcd
    unit_h = h//gcd

    if unit_w == 1 or unit_h == 1:
        blocked_square_per_unit = max(unit_w, unit_h)
    else:
        blocked_square_per_unit = unit_w + unit_h - 1
    total_blocked_square = blocked_square_per_unit * gcd
    total_square = w * h
    ans = total_square - total_blocked_square

    print(ans)
    return ans


w, h = 7894, 215674
solution(w, h)
