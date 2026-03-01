# Завдання 29 — Злиття двох списків в один відсортований

def merge_sorted(lst1, lst2):
    return sorted(lst1 + lst2)

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
print("Список A:", a)
print("Список B:", b)
print("Злитий:", merge_sorted(a, b))
