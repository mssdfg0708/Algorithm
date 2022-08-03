from sys import stdin
from itertools import combinations

alphabets = {'b': 20, 'd': 19, 'e': 18, 'f': 17, 'g': 16, 'h': 15, 'j': 14,
             'k': 13, 'l': 12, 'm': 11, 'o': 10, 'p': 9, 'q': 8, 'r': 7,
             's': 6, 'u': 5, 'v': 4, 'w': 3, 'x': 2, 'y': 1, 'z': 0}


def word_to_bin(word):
    answer = 0b0
    for x in word:
        answer = answer | (1 << alphabets[x])

    return answer


n, k = map(int, stdin.readline().split())
words = []
for _ in range(n):
    word = stdin.readline().rstrip()[4:-4]
    words.append(set(word).difference('a', 'c', 'i', 't', 'n'))

if k < 5:
    print(0)
else:
    binary_list = [word_to_bin(x) for x in words]
    max_count = 0
    powers = [2 ** i for i in range(21)]

    for item in combinations(powers, k - 5):
        current = sum(item)
        count = 0
        for bin_number in binary_list:
            if bin_number & current == bin_number:
                count += 1

        max_count = max(max_count, count)

    print(max_count)
