# Завдання 01 — Ділення на нуль (ZeroDivisionError)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Помилка:", e)
else:
    print("Результат:", result)
