def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    dict1 = dict()
    dict2 = dict()
    for i in range(len(str1)-1):
        sub_str1 = str1[i:i+2]
        if sub_str1.isalpha():
            if sub_str1 not in dict1:
                dict1[sub_str1] = 1
                continue
            dict1[sub_str1] += 1

    for i in range(len(str2) - 1):
        sub_str2 = str2[i:i+2]
        if sub_str2.isalpha():
            if sub_str2 not in dict2:
                dict2[sub_str2] = 1
                continue
            dict2[sub_str2] += 1

    intersection = 0
    union = 0
    for key, value in dict1.items():
        if key in dict2:
            intersection += min(dict1[key], dict2[key])
            continue
        union += dict1[key]

    for key, value in dict2.items():
        if key in dict1:
            union += max(dict1[key], dict2[key])
            continue
        union += dict2[key]

    if union == 0:
        return 65536

    result = int(intersection/union * 65536)
    return result


str1 = 'FRANCE'
str2 = 'french'
print(solution(str1, str2))

# dict 를 이용하여 개수 확인
