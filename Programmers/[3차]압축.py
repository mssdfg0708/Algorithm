def solution(msg):
    answer = []
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    dictionary = dict()
    index_dictionary = 1
    for alpha in alphabet:
        dictionary[alpha] = index_dictionary
        index_dictionary += 1

    index_msg = 0
    while index_msg < len(msg):
        sub_msg = msg[index_msg]
        next_msg = sub_msg
        # dictionary 내에 존재하지 않는 최대 길이의 sub_msg 찾기
        while True:
            index_msg += 1
            # Out Of Range 확인
            if index_msg >= len(msg):
                break
            next_msg = sub_msg + msg[index_msg]
            # sub_msg 가 dictionary 에 존재하지 않으면 break
            if next_msg not in dictionary:
                break
            sub_msg = next_msg

        answer.append(dictionary[sub_msg])
        if next_msg not in dictionary:
            dictionary[next_msg] = index_dictionary
            index_dictionary += 1

    return answer


msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))
