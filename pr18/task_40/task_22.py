# Завдання 22 — Ланцюжок виключень (raise from)

class DataProcessingError(Exception):
    pass

def load_config(data):
    try:
        return int(data["timeout"])
    except KeyError as e:
        raise DataProcessingError("Відсутній ключ конфігурації") from e
    except ValueError as e:
        raise DataProcessingError("Некоректне значення timeout") from e

for cfg in [{"timeout": "30"}, {"host": "localhost"}, {"timeout": "abc"}]:
    try:
        t = load_config(cfg)
        print(f"  timeout = {t}")
    except DataProcessingError as e:
        print(f"  DataProcessingError: {e}")
        print(f"  Причина: {e.__cause__}")
