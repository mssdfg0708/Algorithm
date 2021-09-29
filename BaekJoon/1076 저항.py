ome = ['black', 'brown', 'red', 'orange', 'yellow',
       'green', 'blue', 'violet', 'grey', 'white']
first = ome.index(input())
second = ome.index(input())
third = ome.index(input())
result = (first * 10 + second) * (10**third)
print(result)
