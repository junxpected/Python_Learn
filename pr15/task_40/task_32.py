# Завдання 32 — Накопичення результатів у список

def squares_list(n):
    result = []
    for i in range(1, n + 1):
        result.append(i ** 2)
    return result

def cubes_list(n):
    return [i ** 3 for i in range(1, n + 1)]

print("Квадрати:", squares_list(8))
print("Куби:    ", cubes_list(8))
