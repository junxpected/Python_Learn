# Завдання 27 — Функція видалення дублікатів (зі збереженням порядку)

def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

data = [1, 2, 2, 3, 1, 4, 3, 5]
print("З дублікатами:", data)
print("Без дублікатів:", remove_duplicates(data))
