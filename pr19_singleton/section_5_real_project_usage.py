# Розділ 5 — Використання Singleton у реальному проєкті

class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {
                "db_host": "localhost",
                "db_port": 5432,
                "debug": True,
            }
        return cls._instance


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def info(self, message):
        self.logs.append(f"INFO: {message}")


if __name__ == "__main__":
    cfg1 = AppConfig()
    cfg2 = AppConfig()

    cfg1.settings["debug"] = False
    print("Один конфіг-об'єкт:", cfg1 is cfg2)
    print("debug у cfg2:", cfg2.settings["debug"])

    log1 = Logger()
    log2 = Logger()

    log1.info("Старт програми")
    log2.info("Ініціалізація сервісів")

    print("Один logger:", log1 is log2)
    print("Журнал:", log1.logs)
