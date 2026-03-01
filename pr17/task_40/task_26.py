# Завдання 26 — Об'єднання словників через {**a, **b}

defaults = {"theme": "light", "lang": "uk", "timeout": 30}
user = {"theme": "dark", "font": 14}
merged = {**defaults, **user}
print("Злитий (user перемагає):", merged)
