# Завдання 18 — Вкладені try/except: введення індексу та доступ до списку

lst = [100, 200, 300, 400, 500]
inputs = ["2", "abc", "10", "0", "4.5"]

for inp in inputs:
    try:
        idx = int(inp)        # може ValueError
        try:
            val = lst[idx]    # може IndexError
            print(f"  lst[{idx}] = {val}")
        except IndexError:
            print(f"  IndexError: індекс {idx} виходить за межі")
    except ValueError:
        print(f"  ValueError: '{inp}' не є цілим числом")
