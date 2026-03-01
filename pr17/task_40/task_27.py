# Завдання 27 — Групування елементів у словник списків

data = [("фрукт", "яблуко"), ("овоч", "морква"),
        ("фрукт", "банан"), ("овоч", "картопля"), ("фрукт", "вишня")]
grouped = {}
for category, item in data:
    grouped.setdefault(category, []).append(item)
print("Групи:", grouped)
