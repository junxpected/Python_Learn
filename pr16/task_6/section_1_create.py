# Розділ 1 — Створення списків та кортежів

# --- Список ---
my_list = [1, "два", 3.0, True, None]
print("Список:", my_list)

my_list.append("новий")
my_list.insert(2, 99)
print("Після append + insert:", my_list)

my_list.remove("два")
deleted = my_list.pop(0)
print("Після remove + pop:", my_list, "| видалено:", deleted)

# --- Кортеж ---
my_tuple = (10, 20, 30, "текст", False)
print("\nКортеж:", my_tuple)
print("Кортежі незмінні — для 'зміни' створюємо новий:")
new_tuple = my_tuple[:2] + (99,) + my_tuple[3:]
print("Новий кортеж:", new_tuple)
