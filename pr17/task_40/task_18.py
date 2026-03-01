# Завдання 18 — Метод setdefault()

config = {"host": "localhost"}
config.setdefault("port", 8080)
config.setdefault("host", "example.com")  # не змінить
print("Config:", config)
