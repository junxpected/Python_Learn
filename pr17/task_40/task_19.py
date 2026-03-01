# Завдання 19 — Словникове включення (dict comprehension)

squares = {x: x**2 for x in range(1, 8)}
even_sq = {x: x**2 for x in range(1, 8) if x % 2 == 0}
print("Квадрати:", squares)
print("Парні квадрати:", even_sq)
