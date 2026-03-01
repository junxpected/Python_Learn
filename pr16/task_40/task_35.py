# Завдання 35 — Спільні елементи двох списків

def common_elements(lst1, lst2):
    return sorted(set(lst1) & set(lst2))

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print("Список A:", a)
print("Список B:", b)
print("Спільні елементи:", common_elements(a, b))
