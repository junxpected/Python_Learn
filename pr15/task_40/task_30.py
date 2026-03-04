# Завдання 30 — Декоратор функції

def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_result
def greet(name):
    return f"привіт, {name}!"

print(greet("аня"))
print(greet("богдан"))
