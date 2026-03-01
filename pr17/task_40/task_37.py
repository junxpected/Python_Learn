# Завдання 37 — Словник з лічильником через get()

sentence = "the quick brown fox jumps over the lazy dog the fox"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

print("Лічильник слів:", word_count)
print("Слово 'the' зустрічається:", word_count["the"], "разів")
