# Завдання 20 — Рекурсія — числа Фібоначчі

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print([fib(i) for i in range(12)])
