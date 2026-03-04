# Розділ 4 — Стандартні бібліотеки: itertools та math

import itertools
import math

# --- math ---
print("=== math ===")
print("sqrt(144):", math.sqrt(144))
print("pi:", round(math.pi, 6))
print("factorial(10):", math.factorial(10))
print("ceil(3.2):", math.ceil(3.2))
print("floor(3.9):", math.floor(3.9))
print("log2(1024):", math.log2(1024))

# --- itertools.chain ---
print("\n=== itertools.chain ===")
a, b, c = [1, 2], [3, 4], [5, 6]
print(list(itertools.chain(a, b, c)))

# --- itertools.cycle ---
print("\n=== itertools.cycle (перші 7) ===")
colors = itertools.cycle(["червоний", "зелений", "синій"])
for _ in range(7):
    print(next(colors), end=" ")
print()

# --- itertools.combinations ---
print("\n=== combinations ===")
for combo in itertools.combinations([1, 2, 3, 4], 2):
    print(combo, end=" ")
print()

# --- itertools.accumulate ---
print("\n=== accumulate (накопичена сума) ===")
import itertools
nums = [1, 2, 3, 4, 5]
print(list(itertools.accumulate(nums)))

# --- itertools.groupby ---
print("\n=== groupby ===")
data = [("фрукт","яблуко"),("овоч","морква"),("фрукт","банан"),("овоч","цибуля")]
data.sort(key=lambda x: x[0])
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f"  {key}: {[g[1] for g in group]}")
