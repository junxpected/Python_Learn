# Завдання 08 — Блок finally — виконується завжди

def risky(x):
    try:
        print(f"  Обчислення 10/{x}...")
        print(f"  Результат: {10/x}")
    except ZeroDivisionError:
        print("  Помилка: ділення на нуль")
    finally:
        print("  [finally] Завжди виконується\n")

risky(2)
risky(0)
