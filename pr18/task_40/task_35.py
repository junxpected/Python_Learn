# Завдання 35 — Обробка виключень у генераторі

def safe_generator(items):
    for item in items:
        try:
            yield int(item)
        except (ValueError, TypeError):
            print(f"  Пропускаємо '{item}'")

data = ["1", "два", "3", None, "5", "шість", "7"]
result = list(safe_generator(data))
print("Результат:", result)
