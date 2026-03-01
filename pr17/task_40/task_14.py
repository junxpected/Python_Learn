# Завдання 14 — Видалення елементів словника (pop, del, popitem)

d = {"a": 1, "b": 2, "c": 3, "d": 4}
val = d.pop("b")
del d["c"]
last = d.popitem()
print("Результат:", d, "| pop:", val, "| popitem:", last)
