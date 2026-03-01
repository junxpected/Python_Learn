# Завдання 13 — Власне повідомлення при TypeError

def add(a, b):
    try:
        return a + b
    except TypeError:
        print(f"  TypeError: не можна додати {type(a).__name__} і {type(b).__name__}")
        return None

print(add(1, 2))
print(add("abc", 3))
print(add([1,2], [3,4]))
