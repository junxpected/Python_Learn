# Завдання 22 — Список включення з умовою (парні числа)

evens = [x for x in range(1, 21) if x % 2 == 0]
odds = [x for x in range(1, 21) if x % 2 != 0]
print("Парні:", evens)
print("Непарні:", odds)
