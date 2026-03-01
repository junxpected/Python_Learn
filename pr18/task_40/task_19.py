# Завдання 19 — Розрізнення помилок вводу та обчислення

def divide_input(a_str, b_str):
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print(f"  Помилка вводу: '{a_str}' або '{b_str}' не є числами")
        return
    try:
        print(f"  {a} / {b} = {a / b:.4f}")
    except ZeroDivisionError:
        print(f"  Помилка обчислення: ділення на нуль")

divide_input("10", "4")
divide_input("abc", "2")
divide_input("5", "0")
