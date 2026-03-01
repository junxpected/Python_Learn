# Завдання 17 — Функція zip()

names = ["Аня", "Богдан", "Віта"]
scores = [90, 85, 78]
cities = ["Київ", "Львів", "Одеса"]

pairs = list(zip(names, scores))
print("Імена + оцінки:", pairs)

triplets = list(zip(names, scores, cities))
print("Три списки разом:", triplets)
