# Завдання 32 — Сума елементів без максимуму та мінімуму

def sum_without_extremes(lst):
    return sum(lst) - max(lst) - min(lst)

data = [1, 2, 3, 4, 5]
print("Список:", data)
print("Сума всіх:", sum(data))
print("Сума без min/max:", sum_without_extremes(data))
