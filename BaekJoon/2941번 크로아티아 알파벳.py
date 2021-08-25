import sys

croatia_word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input_word = sys.stdin.readline().strip()

for croatia_word in croatia_word_list:
    input_word = input_word.replace(croatia_word, '*')

print(len(input_word))
