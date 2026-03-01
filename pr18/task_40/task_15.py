# Завдання 15 — Функція повертає None при помилці конвертації

def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

data = ["10", "abc", None, "7", "3.14", "99"]
results = [to_int(v) for v in data]
print("Вхід:", data)
print("Вихід:", results)
print("Без None:", [r for r in results if r is not None])
