# Завдання 25 — Фільтрація слів за довжиною

animals = ["кіт", "слон", "пес", "тигр", "лев", "жираф", "мавпа"]
short = [w for w in animals if len(w) <= 3]
long = [w for w in animals if len(w) > 3]
print("Короткі (<=3):", short)
print("Довгі (>3):", long)
