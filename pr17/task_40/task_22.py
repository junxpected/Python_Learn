# Завдання 22 — Інвертування словника (ключ ↔ значення)

d = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in d.items()}
print("Оригінал:", d)
print("Інвертований:", inverted)
