# Завдання 16 — Функція enumerate()

colors = ["червоний", "зелений", "синій", "жовтий"]
for index, color in enumerate(colors):
    print(f"  [{index}] {color}")

# З іншим початковим індексом
print("\nНумерація з 1:")
for index, color in enumerate(colors, start=1):
    print(f"  {index}. {color}")
