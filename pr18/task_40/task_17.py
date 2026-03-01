# Завдання 17 — Конвертація всіх елементів списку у числа

def convert_all(lst):
    result = []
    errors = []
    for i, item in enumerate(lst):
        try:
            result.append(float(item))
        except (ValueError, TypeError):
            print(f"  [i={i}] Не вдалося конвертувати '{item}'")
            errors.append(i)
    print(f"  Успішно: {result}")
    print(f"  Помилок: {len(errors)}")
    return result

convert_all(["1", "2.5", "abc", "4", None, "6"])
