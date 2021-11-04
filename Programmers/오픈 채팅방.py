# dict 를 이용하여 목록 관리, 사용자 닉네임 입력
# 모든 Change query 종료 이후 순서대로 출력 실행

def solution(record):
    answer = []
    # return answer
    user_dict = dict()
    new_record = []
    for item in record:
        new_record.append(list(item.split()))

    # 사용자 정보 입력 받기
    for item in new_record:
        # Enter Query
        if item[0] == 'Enter' and item[1] not in user_dict:
            user_dict[item[1]] = item[2]
            continue
        if item[0] == 'Enter' and item[1] in user_dict:
            user_dict[item[1]] = item[2]
            continue
        # Change Query
        if item[0] == 'Change' and item[1] in user_dict:
            user_dict[item[1]] = item[2]
            continue

    # answer 입력
    for item in new_record:
        # Enter Query
        if item[0] == 'Enter':
            user_nickname = user_dict[item[1]]
            sentence = user_nickname + "님이 들어왔습니다."
            answer.append(sentence)
            continue
        # Leave Query
        if item[0] == 'Leave':
            user_nickname = user_dict[item[1]]
            sentence = user_nickname + "님이 나갔습니다."
            answer.append(sentence)
            continue

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
solution(record)
