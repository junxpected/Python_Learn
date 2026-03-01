# Розділ 1 — Вступ до обробки виключень: try, except, else, finally

# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

# ValueError
try:
    num = int("abc")
except ValueError as e:
    print("ValueError:", e)

# FileNotFoundError
try:
    with open("неіснуючий.txt") as f:
        content = f.read()
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

# TypeError
try:
    result = "5" + 5
except TypeError as e:
    print("TypeError:", e)

# IndexError
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError as e:
    print("IndexError:", e)

# KeyError
try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print("KeyError:", e)

print("\nПрограма продовжує роботу після всіх виключень.")
