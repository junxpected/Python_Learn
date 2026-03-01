# Розділ 1 — Створення та операції із множинами

# Створення множин
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
mixed = {1, "текст", 3.14, True}
empty = set()

print("Множина A:", set_a)
print("Множина B:", set_b)
print("Змішана:", mixed)
print("Порожня:", empty)

# Операції
print("\nОб'єднання (A | B):", set_a | set_b)
print("Перетин  (A & B):", set_a & set_b)
print("Різниця  (A - B):", set_a - set_b)
print("Симетрична різниця (A ^ B):", set_a ^ set_b)

# Додавання та видалення
set_a.add(10)
print("\nПісля add(10):", set_a)

set_a.discard(1)
print("Після discard(1):", set_a)

popped = set_a.pop()
print("Після pop():", set_a, "| видалено:", popped)
