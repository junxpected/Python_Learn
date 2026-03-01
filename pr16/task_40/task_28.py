# Завдання 28 — Сортування списку кортежів за ключем

def sort_tuples_by(lst, key_index):
    return sorted(lst, key=lambda t: t[key_index])

students = [("Богдан", 19, 85), ("Аня", 22, 92), ("Віта", 18, 78)]
print("За іменем:", sort_tuples_by(students, 0))
print("За віком:", sort_tuples_by(students, 1))
print("За оцінкою:", sort_tuples_by(students, 2))
