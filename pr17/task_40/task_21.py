# Завдання 21 — Підрахунок частоти елементів

words = ["яблуко", "банан", "яблуко", "вишня", "банан", "яблуко"]
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print("Частота:", freq)
print("Найчастіше:", max(freq, key=freq.get))
