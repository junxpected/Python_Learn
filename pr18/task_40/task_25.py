# Завдання 25 — Обробка помилок у рекурсії (RecursionError)

import sys
sys.setrecursionlimit(100)

def infinite(n):
    return infinite(n + 1)

try:
    infinite(0)
except RecursionError:
    print("RecursionError: перевищено ліміт рекурсії")
finally:
    sys.setrecursionlimit(1000)
    print("[finally] Ліміт відновлено")
