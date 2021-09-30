inputData = input().upper()
keys = list(set(inputData))

count = []
for key in keys:
    count.append(inputData.count(key))

if count.count(max(count)) > 1:
    print("?")
else:
    print(keys[count.index(max(count))])
