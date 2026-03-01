# Завдання 38 — Розплющення вкладеного списку (flatten)

def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested = [[1, [2, 3]], [4, [5, [6, 7]]]]
print("Вкладений:", nested)
print("Плаский:", flatten(nested))
