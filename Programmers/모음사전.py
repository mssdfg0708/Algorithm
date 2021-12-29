from itertools import product


def solution(word):
    dictionary = []
    for r in range(1, 6):
        temp = list(product("AEIOU", repeat=r))
        for item in temp:
            dictionary.append("".join(item))

    dictionary.sort()
    answer = dictionary.index(word)+1
    return answer


word = "AAAAE"
solution(word)
