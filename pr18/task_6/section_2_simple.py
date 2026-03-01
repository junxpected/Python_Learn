# Розділ 2 — Обробка виключень у простих сценаріях

# --- Ділення на нуль ---
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  Помилка: ділення {a} на нуль неможливе")
        return None
    else:
        print(f"  {a} / {b} = {result}")
        return result

print("=== Ділення ===")
safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(7, 3)

# --- Перевірка введення (симуляція) ---
def parse_age(value):
    try:
        age = int(value)
        if age < 0 or age > 150:
            raise ValueError("Вік поза допустимим діапазоном")
        return age
    except ValueError as e:
        print(f"  Некоректний вік '{value}': {e}")
        return None

print("\n=== Перевірка віку ===")
inputs = ["25", "-5", "abc", "200", "18"]
for inp in inputs:
    result = parse_age(inp)
    if result:
        print(f"  Вік прийнято: {result}")
