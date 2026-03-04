# Завдання 13 — Функція повертає кілька значень

def stats(lst):
    return min(lst), max(lst), sum(lst) / len(lst)

lo, hi, avg = stats([4, 7, 2, 9, 1, 6])
print(f"min={lo}, max={hi}, avg={avg:.2f}")
