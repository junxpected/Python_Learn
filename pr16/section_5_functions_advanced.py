# Розділ 5 — Функції для роботи зі списками та кортежами

def add_element(lst, element, position=None):
    """Додати елемент у список."""
    result = lst.copy()
    if position is None:
        result.append(element)
    else:
        result.insert(position, element)
    return result

def remove_duplicates(lst):
    """Видалити дублікати зі збереженням порядку."""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def sort_by_second(lst_of_tuples):
    """Відсортувати список кортежів за другим елементом."""
    return sorted(lst_of_tuples, key=lambda t: t[1])

def chunk(lst, n):
    """Розбити список на підсписки розміром n."""
    return [lst[i:i+n] for i in range(0, len(lst), n)]

def flatten(nested):
    """Розплющити вкладений список."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


# --- Тестування ---
lst = [3, 1, 2]
print("add_element:", add_element(lst, 99, 1))
print("remove_duplicates:", remove_duplicates([1, 2, 2, 3, 1, 4]))
print("sort_by_second:", sort_by_second([("Аня", 22), ("Богдан", 18), ("Віта", 25)]))
print("chunk:", chunk(list(range(1, 10)), 3))
print("flatten:", flatten([[1, [2, 3]], [4, [5, 6]]]))
