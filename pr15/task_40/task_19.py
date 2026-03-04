# Завдання 19 — Рекурсія — факторіал

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

for i in range(1, 9):
    print(f"{i}! = {factorial(i)}")
