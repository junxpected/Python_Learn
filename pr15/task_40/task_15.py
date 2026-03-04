# Завдання 15 — **kwargs — іменовані аргументи

def profile(**data):
    for key, val in data.items():
        print(f"  {key}: {val}")

profile(name="Аня", age=21, city="Київ")
