# Завдання 04 — Безпечний доступ до списку за індексом

lst = [10, 20, 30, 40, 50]
for idx in [2, 7, -1, 100]:
    try:
        print(f"  lst[{idx}] = {lst[idx]}")
    except IndexError:
        print(f"  lst[{idx}] — індекс виходить за межі")
