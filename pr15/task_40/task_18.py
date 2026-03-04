# Завдання 18 — filter() з функцією

def is_positive(n):
    return n > 0

numbers = [-3, 7, -1, 0, 5, -8, 2]
positive = list(filter(is_positive, numbers))
print("Всі:", numbers)
print("Позитивні:", positive)
