# Завдання 34 — Транспонування матриці

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(map(list, zip(*matrix)))

print("Оригінальна матриця:")
for row in matrix:
    print(" ", row)

print("Транспонована матриця:")
for row in transposed:
    print(" ", row)
