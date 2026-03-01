# Завдання 26 — Функція додавання елемента (append/insert)

def add_element(lst, element, position=None):
    """Додає елемент у список — в кінець або за позицією."""
    if position is None:
        lst.append(element)
    else:
        lst.insert(position, element)
    return lst

my_list = [1, 2, 3, 4]
print("Оригінал:", my_list)
add_element(my_list, 99)
print("Після append(99):", my_list)
add_element(my_list, 0, position=0)
print("Після insert(0, pos=0):", my_list)
