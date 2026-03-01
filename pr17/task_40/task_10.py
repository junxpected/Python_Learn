# Завдання 10 — Frozenset — незмінна множина

fs = frozenset([1, 2, 3, 4, 5])
print("frozenset:", fs)
print("Перетин з {3,4,5,6}:", fs & {3, 4, 5, 6})
# fs.add(6)  # TypeError — незмінна
