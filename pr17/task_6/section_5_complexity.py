# Розділ 5 — Конфлікти у словниках та часова складність

# --- Конфлікт ключів при злитті ---
defaults = {"theme": "light", "lang": "uk", "timeout": 30}
user_settings = {"theme": "dark", "font_size": 14}

# Метод 1: update (user перезаписує defaults)
merged = defaults.copy()
merged.update(user_settings)
print("update (user перемагає):", merged)

# Метод 2: {**a, **b} — те саме, але в один рядок
merged2 = {**defaults, **user_settings}
print("{**a, **b}:              ", merged2)

# Метод 3: user НЕ перезаписує defaults (defaults перемагають)
merged3 = {**user_settings, **defaults}
print("defaults перемагають:   ", merged3)

# --- setdefault — додати тільки якщо ключа ще немає ---
config = {"host": "localhost"}
config.setdefault("port", 8080)
config.setdefault("host", "example.com")  # не змінить, бо вже є
print("\nsetdefault:", config)

# --- Часова складність (демонстрація) ---
import time

n = 1_000_000
big_list = list(range(n))
big_set = set(range(n))
big_dict = {i: i for i in range(n)}

target = n - 1  # шукаємо останній елемент

t = time.perf_counter()
_ = target in big_list
print(f"\nПошук у list  (O(n)): {(time.perf_counter()-t)*1000:.3f} мс")

t = time.perf_counter()
_ = target in big_set
print(f"Пошук у set   (O(1)): {(time.perf_counter()-t)*1000:.3f} мс")

t = time.perf_counter()
_ = target in big_dict
print(f"Пошук у dict  (O(1)): {(time.perf_counter()-t)*1000:.3f} мс")

print("\nВисновок: set і dict на порядок швидші за list при пошуку.")
