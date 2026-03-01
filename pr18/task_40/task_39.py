# Завдання 39 — Обробка помилок у багатоступеневому pipeline

def step_parse(data):
    try: return int(data)
    except ValueError: raise ValueError(f"Крок 1: '{data}' не є числом")

def step_validate(n):
    if n < 0: raise ValueError(f"Крок 2: від'ємне число {n}")
    return n

def step_transform(n):
    if n == 0: raise ZeroDivisionError("Крок 3: ділення на нуль")
    return 1000 / n

def pipeline(data):
    try:
        x = step_parse(data)
        x = step_validate(x)
        x = step_transform(x)
        return round(x, 2)
    except (ValueError, ZeroDivisionError) as e:
        print(f"  Pipeline помилка: {e}")
        return None

for inp in ["20", "abc", "-5", "0", "8"]:
    r = pipeline(inp)
    if r is not None: print(f"  pipeline({inp!r}) = {r}")
