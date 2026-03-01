# Завдання 36 — Підрахунок частоти елементів

def frequency_count(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

data = ["a", "b", "a", "c", "b", "a", "d"]
freq = frequency_count(data)
print("Список:", data)
print("Частота:", freq)
print("Найчастіший:", max(freq, key=freq.get))
