import sys

input_list=[]
index_list=[]
answer_list=[]

# 입력받기
man_number=int(input())
for i in range(man_number):
    input_list.append(list(map(int,sys.stdin.readline().split())))
# 인덱스 추가하기
for  i in range(man_number):
    input_list[i].append(i)

input_list.sort()

for i in range(man_number):
    weight,height=input_list[i][0],input_list[i][1]
    rank=1  
    for j in range(i+1,man_number):
        if height<input_list[j][1] and weight<input_list[j][0]  :
            rank+=1
    index_list.append((input_list[i][2],rank))

index_list.sort()

for i in range(man_number):
    answer_list.append(index_list[i][1])

answer = ''
for item in answer_list:
    answer += (str(item) + ' ')
print(answer)
