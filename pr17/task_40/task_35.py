# Завдання 35 — Частотний аналіз тексту

text = "to be or not to be that is the question to be"
words = text.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

top3 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]
print("Топ-3 слова:", top3)
print("Унікальних слів:", len(set(words)))
