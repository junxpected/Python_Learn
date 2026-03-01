# Завдання 26 — Обробка OverflowError та MemoryError

import math

# OverflowError
try:
    result = math.exp(1000)
except OverflowError as e:
    print(f"OverflowError: {e}")

# Перевірка великих чисел через try
try:
    big = 10 ** 10000
    print(f"10**10000 має {len(str(big))} цифр (Python справляється!)")
except OverflowError as e:
    print(f"OverflowError: {e}")
