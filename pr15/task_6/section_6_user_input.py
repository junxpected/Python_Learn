# Розділ 6 — Взаємодія з користувачем (симуляція вводу)

def get_valid_int(prompt, inputs):
    """Симулює input() — бере значення зі списку."""
    val = inputs.pop(0)
    print(f"{prompt}{val}")
    try:
        return int(val)
    except ValueError:
        print(f"  Помилка: '{val}' — не ціле число. Спробуйте ще.")
        return None

def menu_app(inputs):
    """Проста менюшна програма з циклом."""
    numbers = []

    while inputs:
        print("\n--- МЕНЮ ---")
        print("1. Додати число")
        print("2. Показати всі числа")
        print("3. Порахувати суму")
        print("4. Знайти мінімум та максимум")
        print("0. Вийти")

        choice = inputs.pop(0)
        print(f"Ваш вибір: {choice}")

        if choice == "1":
            raw = inputs.pop(0) if inputs else "0"
            print(f"Введіть число: {raw}")
            try:
                numbers.append(float(raw))
                print(f"  Додано: {raw}")
            except ValueError:
                print(f"  Некоректне значення: '{raw}'")

        elif choice == "2":
            print(f"  Числа: {numbers}")

        elif choice == "3":
            print(f"  Сума: {sum(numbers)}")

        elif choice == "4":
            if numbers:
                print(f"  min={min(numbers)}, max={max(numbers)}")
            else:
                print("  Список порожній")

        elif choice == "0":
            print("  До побачення!")
            break
        else:
            print(f"  Невідома команда: '{choice}'")

# Симулюємо сесію користувача
simulated_inputs = ["1","42","1","17","1","abc","2","3","4","0"]
menu_app(simulated_inputs)
