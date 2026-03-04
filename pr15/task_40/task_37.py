# Завдання 37 — Рекурсія — сума цифр числа

def digit_sum(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

for num in [0, 7, 123, 9999, 54321]:
    print(f"digit_sum({num}) = {digit_sum(num)}")
