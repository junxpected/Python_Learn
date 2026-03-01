# Завдання 33 — Словник як кеш (мемоізація)

cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fib(n-1) + fib(n-2)
    cache[n] = result
    return result

print([fib(i) for i in range(10)])
print("Кеш:", cache)
