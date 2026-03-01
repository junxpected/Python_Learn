# Завдання 33 — Перевірка типів з TypeError

def multiply(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError(f"Аргумент 'a' має бути числом, отримано {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Аргумент 'b' має бути числом, отримано {type(b).__name__}")
    return a * b

tests = [(3, 4), ("x", 2), (2.5, 4), ([], 3)]
for a, b in tests:
    try:
        print(f"  {a} * {b} = {multiply(a, b)}")
    except TypeError as e:
        print(f"  TypeError: {e}")
