# Завдання 12 — Перехоплення будь-якої помилки (Exception)

operations = [
    lambda: 1 / 0,
    lambda: int("xyz"),
    lambda: [1,2,3][10],
    lambda: {"a":1}["b"],
    lambda: 2 + 2,
]
for i, op in enumerate(operations):
    try:
        result = op()
        print(f"  [{i}] Успіх: {result}")
    except Exception as e:
        print(f"  [{i}] {type(e).__name__}: {e}")
