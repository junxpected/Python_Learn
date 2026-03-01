# Завдання 30 — Обробка помилок у списковому включенні

data = ["1", "abc", "3", None, "5", "6.7"]

# Без обробки — впаде на першому некоректному
# result = [int(x) for x in data]  # TypeError на None

# З обробкою через допоміжну функцію
def safe_int(x):
    try:
        return int(x)
    except (ValueError, TypeError):
        return None

result = [safe_int(x) for x in data]
valid = [x for x in result if x is not None]
print("Всі:", result)
print("Тільки числа:", valid)
