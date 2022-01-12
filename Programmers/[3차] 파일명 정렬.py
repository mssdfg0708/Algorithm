"""
문제 사이트 : Programmers
문제 이름 : [3차] 압축
예상 풀이 시간 : 30분
실제 걸린 시간 : 30분 미만
문제 선정 이유
매일 1문제씩 Programmers Level2 풀이 중이어서
"""


def solution(files):
    file_list = []
    for file_name in files:
        # HEAD, NUMBER, TAIL, INDEX
        info = ["", "", "", -1]
        file_index = 0

        # HEAD
        while not file_name[file_index].isdigit():
            info[0] += file_name[file_index]
            file_index += 1
        info[0] = info[0].lower()

        # NUMBER
        while file_index < len(file_name) and file_name[file_index].isdigit() :
            if len(info[1]) >= 5:
                break
            info[1] += file_name[file_index]
            file_index += 1
        info[1] = int(info[1])

        # TAIL
        while file_index < len(file_name):
            info[2] += file_name[file_index]
            file_index += 1

        # INDEX
        info[3] = files.index(file_name)
        file_list.append(info)

    file_list.sort(key=lambda x: (x[0], x[1]))

    answer = []
    for HEAD, NUMBER, TAIL, INDEX in file_list:
        answer.append(files[INDEX])

    return answer


files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))
