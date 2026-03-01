# Завдання 05 — Доступ до відсутнього ключа словника (KeyError)

d = {"name": "Аня", "age": 21}
for key in ["name", "email", "age", "city"]:
    try:
        print(f"  {key}: {d[key]}")
    except KeyError:
        print(f"  Ключ '{key}' відсутній")
