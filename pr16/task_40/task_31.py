# Завдання 31 — Другий за величиною елемент

def second_max(lst):
    unique = sorted(set(lst), reverse=True)
    return unique[1] if len(unique) >= 2 else None

data = [3, 1, 4, 1, 5, 9, 2, 6]
print("Список:", data)
print("Максимум:", max(data))
print("Другий максимум:", second_max(data))
