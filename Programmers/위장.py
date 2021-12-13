def solution(clothes):
    clothes_dict = dict()
    for name, kind in clothes:
        if kind not in clothes_dict:
            clothes_dict[kind] = 1
            continue
        clothes_dict[kind] += 1

    count = []
    for key, value in clothes_dict.items():
        count.append(value)

    # 수식을 알아야 해결 가능하다..
    # combination 을 사용하면 시간초과..
    answer = 1
    for item in count:
        answer *= item+1
    answer -= 1

    return answer


clothes = [["yellowhat", "headgear"]]
print(solution(clothes))

# 옷 2 머리 1 바지 5
# 옷(2+1) * 머리(1+1) * 바지(5+1) - 1
# 요고가 정답 (2+1) * (1+1) * (5+1) -1
