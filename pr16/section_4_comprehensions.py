# Розділ 4 — Спискові включення (List Comprehensions)

# Базовий синтаксис: [вираз for елемент in колекція if умова]

# Квадрати чисел
squares = [x**2 for x in range(1, 11)]
print("Квадрати:", squares)

# Фільтрація парних
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Парні:", evens)

# Рядки у верхній регістр
words = ["python", "list", "tuple"]
upper = [w.upper() for w in words]
print("Uppercase:", upper)

# Вкладені включення (матриця 3x3)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Матриця:")
for row in matrix:
    print(" ", row)

# Включення з умовою «парне → квадрат, непарне → куб»
result = [x**2 if x % 2 == 0 else x**3 for x in range(1, 8)]
print("Квадрат/куб:", result)

# Розплющення матриці
flat = [num for row in matrix for num in row]
print("Пласка матриця:", flat)
