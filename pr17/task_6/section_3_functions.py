# Розділ 3 — Вбудовані функції та методи

d = {"python": 90, "java": 75, "c++": 85, "js": 88}
s = {3, 1, 4, 1, 5, 9, 2, 6}  # дублікати автоматично прибираються

print("Словник:", d)
print("Множина:", s)

# Функції для словника
print("\nlen():", len(d))
print("keys():", list(d.keys()))
print("values():", list(d.values()))
print("items():", list(d.items()))
print("sum(values):", sum(d.values()))
print("max(values):", max(d.values()))
print("min(values):", min(d.values()))

# Методи словника
d2 = {"go": 70, "rust": 92}
d.update(d2)
print("\nПісля update:", d)

copy_d = d.copy()
copy_d.clear()
print("copy + clear:", copy_d)

# Функції для множини
print("\nlen(s):", len(s))
print("sum(s):", sum(s))
print("max(s):", max(s))
print("min(s):", min(s))
print("sorted(s):", sorted(s))

# Методи множини
s.add(100)
s.discard(1)
print("\nПісля add(100) + discard(1):", s)
print("issubset {3,4}:", {3, 4}.issubset(s))
print("issuperset:", s.issuperset({3, 4}))
