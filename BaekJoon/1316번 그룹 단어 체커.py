import sys

def check_group_word(word):
    last_letter = word[0]
    letter_list = []
    for letter in word:
        if last_letter != letter:
            letter_list.append(last_letter)
        if letter in letter_list:
            return 0
        last_letter = letter
    return 1

num = int(input())
word_list = []
result = 0

for i in range(num):
    word_list.append(sys.stdin.readline().strip())

for word in word_list:
    result += (check_group_word(word))

print(result)
