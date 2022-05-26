n, m = map(int, input().split())
dna = []
result = ""
count = 0

for i in range(n):
    alphabet = input()
    dna.append(alphabet.upper())

for i in range(m):
    alphabet = [0 for _ in range(26)]
    for j in range(n):
        alphabet[ord(dna[j][i]) - 65] += 1
    result += chr(alphabet.index(max(alphabet)) + 65)

for i in range(n):
    for j in range(m):
        if dna[i][j] != result[j]:
            count += 1

print(result)
print(count)
