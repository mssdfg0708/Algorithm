import sys

n = int(input())
list = list(map(int,sys.stdin.readline().split()))
 
sum = [list[0]]
for i in range(1,len(list)):
    sum.append(max(sum[i-1]+list[i], list[i]))
    
print(max(sum))
