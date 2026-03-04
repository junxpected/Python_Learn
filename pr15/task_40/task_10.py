# Завдання 10 — while з введенням (симуляція)

inputs = ["abc", "42"]
result = None
while result is None:
    val = inputs.pop(0)
    print(f"Введіть число: {val}")
    try:
        result = int(val)
    except ValueError:
        print("  Не число, спробуйте ще")
print(f"Прийнято: {result}")
