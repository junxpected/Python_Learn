# Завдання 27 — itertools.combinations та permutations

import itertools
items = [1, 2, 3, 4]
print("combinations(2):", list(itertools.combinations(items, 2)))
print("permutations(2):", list(itertools.permutations(items, 2)))
