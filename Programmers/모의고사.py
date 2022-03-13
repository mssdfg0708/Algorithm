def solution(answers):
    person1_pattern = [1, 2, 3, 4, 5]
    person2_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    person3_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    person1_answer = [person1_pattern[index % len(person1_pattern)] for index in range(len(answers))]
    person2_answer = [person2_pattern[index % len(person2_pattern)] for index in range(len(answers))]
    person3_answer = [person3_pattern[index % len(person3_pattern)] for index in range(len(answers))]

    highest_person = []
    max_score = -1

    temp = 0
    for index in range(len(answers)):
        if person1_answer[index] == answers[index]:
            temp += 1

    if temp == max_score:
        highest_person.append(1)

    if temp > max_score:
        highest_person.clear()
        max_score = temp
        highest_person.append(1)

    temp = 0
    for index in range(len(answers)):
        if person2_answer[index] == answers[index]:
            temp += 1

    if temp == max_score:
        highest_person.append(2)

    if temp > max_score:
        highest_person.clear()
        max_score = temp
        highest_person.append(2)

    temp = 0
    for index in range(len(answers)):
        if person3_answer[index] == answers[index]:
            temp += 1

    if temp == max_score:
        highest_person.append(3)

    if temp > max_score:
        highest_person.clear()
        max_score = temp
        highest_person.append(3)

    highest_person.sort()
    return highest_person


input_answers = [1, 2, 3, 4, 5]
print(solution(input_answers))
