def solution(participant, completion):
    par_dict = dict()
    for item in participant:
        if item not in par_dict:
            par_dict[item] = 1
            continue
        par_dict[item] += 1

    for item in completion:
        par_dict[item] -= 1

    for key, value in par_dict.items():
        if value != 0:
            return key


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
solution(participant, completion)
