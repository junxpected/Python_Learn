# Завдання 33 — Функція вищого порядку

def apply_twice(func, value):
    return func(func(value))

def double(x): return x * 2
def add_ten(x): return x + 10

print(apply_twice(double, 3))    # 12
print(apply_twice(add_ten, 5))   # 25
