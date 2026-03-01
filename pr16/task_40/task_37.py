# Завдання 37 — Зсув списку вправо на k позицій

def rotate_right(lst, k):
    n = len(lst)
    k = k % n
    return lst[-k:] + lst[:-k]

data = [1, 2, 3, 4, 5]
print("Оригінал:", data)
print("Зсув на 1:", rotate_right(data, 1))
print("Зсув на 2:", rotate_right(data, 2))
print("Зсув на 3:", rotate_right(data, 3))
