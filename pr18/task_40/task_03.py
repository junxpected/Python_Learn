# Завдання 03 — Конвертація рядка у ціле число

def safe_int(s):
    try:
        return int(s)
    except ValueError:
        print(f"Не вдалося конвертувати '{s}'")
        return None

for s in ["42", "3.14", "hello", "-7"]:
    print(f"  '{s}' → {safe_int(s)}")
