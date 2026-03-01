# Завдання 23 — Фільтрація словника за значенням

scores = {"Аня": 95, "Богдан": 62, "Віта": 88, "Гліб": 55}
passed = {k: v for k, v in scores.items() if v >= 70}
failed = {k: v for k, v in scores.items() if v < 70}
print("Склали:", passed)
print("Не склали:", failed)
