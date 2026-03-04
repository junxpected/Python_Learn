# Розділ 2 — Функції в Python

# --- Базова функція ---
def greet(name):
    return f"Привіт, {name}!"

print(greet("Аня"))

# --- Параметри за замовчуванням ---
def power(base, exp=2):
    return base ** exp

print(power(3))      # 9
print(power(2, 10))  # 1024

# --- Довільна кількість аргументів (*args) ---
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4, 5))  # 15

# --- Іменовані аргументи (**kwargs) ---
def describe(**info):
    for key, val in info.items():
        print(f"  {key}: {val}")

describe(name="Богдан", age=21, city="Львів")

# --- Повернення кількох значень ---
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([5, 2, 8, 1, 9, 3])
print(f"min={lo}, max={hi}")

# --- Lambda функція ---
square = lambda x: x ** 2
nums = [1, 2, 3, 4, 5]
print(list(map(square, nums)))

# --- Рекурсія ---
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")
