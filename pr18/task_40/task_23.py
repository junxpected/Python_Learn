# Завдання 23 — Контекстний менеджер з обробкою виключень

class ManagedResource:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print(f"  [{self.name}] відкрито")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"  [{self.name}] закрито")
        if exc_type:
            print(f"  Виключення перехоплено: {exc_val}")
            return True  # пригнічуємо виключення
        return False
    def process(self, value):
        if value < 0:
            raise ValueError(f"Від'ємне значення: {value}")
        return value * 2

with ManagedResource("ресурс") as r:
    print("  Результат:", r.process(5))

with ManagedResource("ресурс") as r:
    print("  Результат:", r.process(-3))
