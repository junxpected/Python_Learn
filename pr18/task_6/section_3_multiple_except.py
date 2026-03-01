# Розділ 3 — Кілька блоків except та блок else

def process_input(data, index):
    """Конвертує елемент списку у число і ділить 100 на нього."""
    try:
        value = int(data[index])
        result = 100 / value
    except IndexError:
        print(f"  IndexError: індекс {index} виходить за межі списку")
    except ValueError:
        print(f"  ValueError: '{data[index]}' не є числом")
    except ZeroDivisionError:
        print(f"  ZeroDivisionError: елемент дорівнює нулю")
    except Exception as e:
        print(f"  Невідома помилка: {e}")
    else:
        # Виконується лише якщо виключень не було
        print(f"  Успіх: 100 / {data[index]} = {result:.2f}")

data = ["5", "0", "abc", "25"]

print("=== Тест різних виключень ===")
process_input(data, 0)   # успіх
process_input(data, 1)   # ZeroDivisionError
process_input(data, 2)   # ValueError
process_input(data, 10)  # IndexError
