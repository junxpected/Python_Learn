# Завдання 26 — itertools.chain

import itertools
a, b, c = [1, 2, 3], [4, 5, 6], [7, 8, 9]
combined = list(itertools.chain(a, b, c))
print("chain:", combined)
