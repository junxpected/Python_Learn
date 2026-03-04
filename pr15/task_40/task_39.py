# Завдання 39 — Функції map + filter + reduce

from functools import reduce

numbers = list(range(1, 11))

doubled = list(map(lambda x: x * 2, numbers))
evens   = list(filter(lambda x: x % 2 == 0, numbers))
product = reduce(lambda a, b: a * b, numbers)

print("Подвоєні:", doubled)
print("Парні:   ", evens)
print("Добуток 1..10:", product)
