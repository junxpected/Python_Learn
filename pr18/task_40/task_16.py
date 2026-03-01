# Завдання 16 — Повторний запит числа до коректного вводу

def get_number_from_list(attempts):
    for attempt in attempts:
        try:
            num = int(attempt)
            print(f"  Прийнято: {num}")
            return num
        except ValueError:
            print(f"  '{attempt}' не є числом, спробуйте ще")
    print("  Вичерпано спроби")
    return None

get_number_from_list(["abc", "xyz", "42"])
