# Завдання 32 — Перевірка анаграм через множини

def is_anagram(s1, s2):
    from collections import Counter
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
