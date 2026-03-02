# Розділ 2 — Простий Singleton

class SimpleSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == "__main__":
    a = SimpleSingleton()
    b = SimpleSingleton()

    print("a is b:", a is b)  # Очікується True
    print("id(a):", id(a))
    print("id(b):", id(b))
