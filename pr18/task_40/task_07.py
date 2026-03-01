# Завдання 07 — Блок else — виконується лише без помилок

for val in ["123", "45.6", "hello"]:
    try:
        num = int(val)
    except ValueError:
        print(f"  '{val}' — не ціле число")
    else:
        print(f"  Успіх: '{val}' → {num}")
