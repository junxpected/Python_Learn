# Завдання 24 — Пошук унікальних елементів через множину

lst = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = set(lst)
duplicates = {x for x in lst if lst.count(x) > 1}
print("Унікальні:", unique)
print("Дублікати:", duplicates)
