# Розділ 3 — Цикли та функції в комбінації

def is_prime(n):
    """Перевіряє чи число просте."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]

print("Прості до 50:", primes_up_to(50))

# --- Обробка матриці ---
def matrix_sum(matrix):
    total = 0
    for row in matrix:
        for val in row:
            total += val
    return total

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Сума матриці:", matrix_sum(m))
print("Транспонована:")
for row in transpose(m):
    print(" ", row)

