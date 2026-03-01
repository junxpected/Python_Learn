# Завдання 11 — Створення словника різними способами

d1 = {"a": 1, "b": 2}
d2 = dict(x=10, y=20)
d3 = dict.fromkeys(["q", "w", "e"], 0)
d4 = {k: k**2 for k in range(1, 6)}
print(d1, d2, d3, d4, sep="\n")
