# Завдання 06 — Калькулятор з обробкою помилок

def calc(a, op, b):
    try:
        a, b = float(a), float(b)
        if op == "+": return a + b
        if op == "-": return a - b
        if op == "*": return a * b
        if op == "/":
            if b == 0: raise ZeroDivisionError("ділення на нуль")
            return a / b
        raise ValueError(f"Невідомий оператор '{op}'")
    except (ValueError, ZeroDivisionError) as e:
        print(f"  Помилка: {e}")
        return None

for expr in [("10","+","3"), ("abc","*","2"), ("8","/","0"), ("9","/","3")]:
    r = calc(*expr)
    if r is not None: print(f"  {expr[0]} {expr[1]} {expr[2]} = {r}")
