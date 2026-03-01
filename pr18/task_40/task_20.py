# Завдання 20 — Програма без обробки та з обробкою помилок

# БЕЗ обробки (симуляція — коментар показує що б сталося):
# int("hello")  → ValueError: invalid literal ...  CRASH

# З обробкою:
values = ["10", "hello", "30", "world", "50"]

print("З обробкою:")
total = 0
for v in values:
    try:
        total += int(v)
        print(f"  '{v}' — додано")
    except ValueError:
        print(f"  '{v}' — пропущено (не число)")
print(f"  Сума: {total}")
