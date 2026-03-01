# Розділ 6 — Реальна задача: інвертований індекс статей

articles = {
    "python_basics":   "python змінні типи дані функції",
    "python_oop":      "python клас об'єкт метод спадкування",
    "web_dev":         "html css javascript функції",
    "data_science":    "python дані статистика функції numpy",
    "algorithms":      "алгоритм дані структури метод складність",
}

# Будуємо інвертований індекс: слово → {статті}
index = {}
for article, content in articles.items():
    for word in content.split():
        index.setdefault(word, set()).add(article)

print("=== ІНВЕРТОВАНИЙ ІНДЕКС ===")
for word in sorted(index):
    print(f"  {word:<15} → {sorted(index[word])}")

# Пошук статей за ключовими словами
def search(query_words):
    results = None
    for word in query_words:
        matches = index.get(word, set())
        results = matches if results is None else results & matches
    return sorted(results) if results else []

print("\n=== ПОШУК ===")
print("'python' + 'функції':", search(["python", "функції"]))
print("'дані' + 'метод':",     search(["дані", "метод"]))
print("'python' + 'клас':",    search(["python", "клас"]))

# Унікальні слова у всіх статтях
all_words = set(word for content in articles.values() for word in content.split())
print(f"\nВсього унікальних слів: {len(all_words)}")
print("Слова:", sorted(all_words))
