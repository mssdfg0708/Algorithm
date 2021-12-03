def solution(phone_book):
    answer = True
    phone_dict = dict()

    for phone_num in phone_book:
        string = ''
        for char in phone_num:
            string += char
            if string in phone_dict:
                phone_dict[string] += 1
            else:
                phone_dict[string] = 1

    for phone_num in phone_book:
        if phone_dict[phone_num] > 1:
            answer = False
            break

    return answer


phone_book = ["123","456","789"]
print(solution(phone_book))
