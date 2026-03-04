# Завдання 17 — map() з функцією

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

temps_c = [0, 20, 37, 100]
temps_f = list(map(celsius_to_fahrenheit, temps_c))
print("Цельсій:   ", temps_c)
print("Фаренгейт:", temps_f)
