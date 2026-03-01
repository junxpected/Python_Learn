# Завдання 20 — Конвертація між list та tuple

my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)

print("Список:", my_list, type(my_list))
print("Кортеж:", my_tuple, type(my_tuple))
print("Знову список:", back_to_list, type(back_to_list))
