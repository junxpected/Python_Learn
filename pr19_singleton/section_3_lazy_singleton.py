# Розділ 3 — Singleton з лінивою ініціалізацією

class LazySingleton:
    _instance = None

    def __init__(self):
        # Прапорець просто показує факт створення об'єкта
        self.loaded = True

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            print("Створення екземпляра LazySingleton...")
            cls._instance = cls()
        return cls._instance


if __name__ == "__main__":
    print("До першого виклику get_instance() екземпляра ще немає.")
    x = LazySingleton.get_instance()
    y = LazySingleton.get_instance()

    print("x is y:", x is y)  # Очікується True
    print("loaded:", x.loaded)
