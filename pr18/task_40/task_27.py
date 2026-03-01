# Завдання 27 — Обробка AttributeError

class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return f"{self.name} каже: Гав!"

animals = [Dog("Рекс"), "not a dog", Dog("Бобік"), 42]
for a in animals:
    try:
        print(" ", a.bark())
    except AttributeError:
        print(f"  AttributeError: '{type(a).__name__}' не має методу bark()")
