# Завдання 21 — Цикл + функція: сума парних

def sum_evens(lst):
    total = 0
    for n in lst:
        if n % 2 == 0:
            total += n
    return total

print(sum_evens(list(range(1, 21))))   # 110
