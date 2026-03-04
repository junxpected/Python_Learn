# Завдання 38 — while — ітерація Ньютона (sqrt)

def my_sqrt(n, precision=1e-9):
    x = n
    while True:
        x_new = (x + n / x) / 2
        if abs(x_new - x) < precision:
            return x_new
        x = x_new

import math
for val in [2, 9, 144, 1000]:
    my = my_sqrt(val)
    builtin = math.sqrt(val)
    print(f"sqrt({val}): my={my:.8f}  built-in={builtin:.8f}")
