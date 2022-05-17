name = input()
name_dic = {}
for i in range(len(name)):
    if name[i] in name_dic:
        name_dic[name[i]] += 1
    else:
        name_dic[name[i]] = 1

letters = []
for letter in name_dic:
    letters.append((letter, name_dic[letter]))
letters.sort()

even = ""
odd = ""
break_cnt = 0
for letter in letters:
    if letter[1] % 2 != 0:
        break_cnt += 1
        odd += letter[0]
    even += letter[0]*(letter[1]//2)

answer = even + odd
answer += even[::-1]

if break_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(answer)
