# Розділ 5 — Реальна задача: аналіз тексту

def count_words(text):
    return len(text.split())

def word_frequency(text):
    freq = {}
    for word in text.lower().split():
        word = word.strip(".,!?;:")
        freq[word] = freq.get(word, 0) + 1
    return freq

def top_n_words(freq, n=5):
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]

def average_word_length(text):
    words = text.split()
    return sum(len(w) for w in words) / len(words) if words else 0

def find_longest_word(text):
    return max(text.split(), key=len)

def count_sentences(text):
    return sum(1 for ch in text if ch in ".!?")

# --- Демонстрація ---
text = """
Python — це мова програмування високого рівня. Python відомий своєю простотою
та читабельністю коду. Програмісти обирають Python для веб-розробки, аналізу
даних та машинного навчання. Python має велику спільноту та багато бібліотек.
"""

print("=== АНАЛІЗ ТЕКСТУ ===")
print(f"Слів:              {count_words(text)}")
print(f"Речень:            {count_sentences(text)}")
print(f"Середня довжина:   {average_word_length(text):.1f} символів")
print(f"Найдовше слово:    {find_longest_word(text)}")

freq = word_frequency(text)
print(f"\nТоп-5 слів:")
for word, count in top_n_words(freq, 5):
    bar = "█" * count
    print(f"  {word:<15} {bar} ({count})")
