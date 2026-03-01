# Завдання 32 — Логування виключень

import logging, io

log_stream = io.StringIO()
logging.basicConfig(stream=log_stream, level=logging.DEBUG,
                    format="%(levelname)s: %(message)s")

def divide(a, b):
    try:
        result = a / b
        logging.info(f"{a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error(f"Ділення на нуль: {a}/{b}")
        return None
    except TypeError as e:
        logging.warning(f"Неправильний тип: {e}")
        return None

divide(10, 2)
divide(5, 0)
divide("x", 2)

print(log_stream.getvalue())
