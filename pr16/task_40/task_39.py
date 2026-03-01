# Завдання 39 — Перетворення списку в кортежі пар

def pairwise(lst):
    return [(lst[i], lst[i+1]) for i in range(0, len(lst) - 1, 2)]

data = [1, 2, 3, 4, 5, 6]
print("Список:", data)
print("Пари:", pairwise(data))

# Варіант через zip
pairs_zip = list(zip(data[::2], data[1::2]))
print("Через zip:", pairs_zip)
