# Завдання 38 — Безпечний парсер CSV рядка

def parse_csv_line(line, expected_cols=3):
    try:
        parts = line.strip().split(",")
        if len(parts) != expected_cols:
            raise ValueError(f"Очікувалось {expected_cols} колонок, отримано {len(parts)}")
        name = parts[0].strip()
        age = int(parts[1].strip())
        score = float(parts[2].strip())
        return {"name": name, "age": age, "score": score}
    except ValueError as e:
        print(f"  Помилка парсингу: {e}")
        return None

lines = [
    "Аня, 21, 95.5",
    "Богдан, двадцять, 80",
    "Віта, 19",
    "Гліб, 22, 88.0",
]
for line in lines:
    r = parse_csv_line(line)
    if r: print(f"  OK: {r}")
