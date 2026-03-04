# Завдання 29 — Генератор з yield

def count_up(start, end):
    while start <= end:
        yield start
        start += 1

for n in count_up(1, 8):
    print(n, end=" ")
print()
