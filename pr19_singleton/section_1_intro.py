# Розділ 1 — Ознайомлення із шаблоном Singleton

class SingletonTheory:
    """Невелика довідка про призначення шаблону Singleton."""

    @staticmethod
    def explain():
        print("Singleton гарантує один екземпляр класу та єдину точку доступу до нього.")
        print("Типові кейси: конфігурація, логер, кеш, підключення до спільних ресурсів.")


if __name__ == "__main__":
    SingletonTheory.explain()
