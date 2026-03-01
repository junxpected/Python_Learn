# Завдання 31 — Повторні спроби (retry decorator)

import functools, random

def retry(times=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  Спроба {attempt}/{times} не вдалась: {e}")
                    if attempt == times:
                        raise
        return wrapper
    return decorator

random.seed(1)

@retry(times=4)
def unstable_request():
    if random.random() < 0.7:
        raise ConnectionError("Сервер недоступний")
    return "Відповідь отримано!"

try:
    print(unstable_request())
except ConnectionError:
    print("  Всі спроби вичерпано")
