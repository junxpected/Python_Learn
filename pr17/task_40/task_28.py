# Завдання 28 — Сортування словника за ключем та значенням

d = {"банан": 3, "яблуко": 1, "вишня": 2}
by_key = dict(sorted(d.items()))
by_val = dict(sorted(d.items(), key=lambda x: x[1]))
print("За ключем:", by_key)
print("За значенням:", by_val)
