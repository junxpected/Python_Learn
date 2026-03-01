# Завдання 33 — Перевірка чи список є паліндромом

def is_palindrome(lst):
    return lst == lst[::-1]

print(is_palindrome([1, 2, 3]))        # False
print(is_palindrome([1, 2, 1]))        # True
print(is_palindrome([1, 2, 2, 1]))     # True
print(is_palindrome(["а", "б", "а"]))  # True
