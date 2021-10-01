n = int(input())
input_list = []
for _ in range(n):
    input_list.append(input())

word_list = [[]for _ in range(51)]
for word in input_list:
    length = len(word)
    word_list[length].append(word)

for item in word_list:
    item.sort()

buffer = ''
for item in word_list:
    for word in item:
        if word != buffer:
            print(word)
            buffer = word
