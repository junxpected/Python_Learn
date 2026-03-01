# Завдання 24 — Вкладені включення (матриця множення)

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Таблиця множення 3x3:")
for row in matrix:
    print(" ", row)
