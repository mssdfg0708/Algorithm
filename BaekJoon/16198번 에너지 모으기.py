import copy
from itertools import permutations

N = int(input())
energies = list(map(int, input().split()))

answer = -1
orders = permutations(range(1, N-1), N-2)

for order in orders:
    energies_copy = copy.deepcopy(energies)
    saved_energy = 0

    for index in order:
        left_index = index - 1
        while energies_copy[left_index] == 0:
            left_index -= 1

        right_index = index + 1
        while energies_copy[right_index] == 0:
            right_index += 1

        saved_energy += energies_copy[left_index] * energies_copy[right_index]
        energies_copy[index] = 0

    answer = max(answer, saved_energy)

print(answer)
