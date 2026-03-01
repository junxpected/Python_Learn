# Завдання 02 — Введення нечислового значення (ValueError)

value = "abc"
try:
    num = int(value)
    print("Число:", num)
except ValueError as e:
    print(f"'{value}' — не число:", e)
