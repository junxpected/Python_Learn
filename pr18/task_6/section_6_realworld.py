# Розділ 6 — Обробка виключень у реальних задачах

import json, tempfile, os

# --- Задача 1: безпечна робота з файлами ---
class FileProcessor:
    def read_json(self, filepath):
        try:
            with open(filepath, encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"  Файл не знайдено: {filepath}")
        except PermissionError:
            print(f"  Немає прав доступу: {filepath}")
        except json.JSONDecodeError as e:
            print(f"  Некоректний JSON: {e}")
        return None

    def write_json(self, filepath, data):
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  Збережено: {filepath}")
            return True
        except (OSError, TypeError) as e:
            print(f"  Помилка запису: {e}")
            return False

print("=== Робота з JSON файлами ===")
fp = FileProcessor()
fp.read_json("missing.json")

tmp = tempfile.mktemp(suffix=".json")
fp.write_json(tmp, {"users": ["Аня", "Богдан"], "count": 2})
data = fp.read_json(tmp)
print(f"  Зчитано: {data}")
os.unlink(tmp)

# --- Задача 2: симуляція підключення до БД з retry ---
import random

class DatabaseError(Exception): pass
class ConnectionTimeoutError(DatabaseError): pass

def connect_db(host, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            print(f"  Спроба {attempt}/{max_retries} підключення до {host}...")
            if random.random() < 0.6:   # 60% шанс помилки
                raise ConnectionTimeoutError(f"Timeout при підключенні до {host}")
            print(f"  Підключено до {host}!")
            return {"host": host, "status": "connected"}
        except ConnectionTimeoutError as e:
            print(f"  {e}")
            if attempt == max_retries:
                raise DatabaseError(f"Не вдалося підключитися після {max_retries} спроб") from e
    return None

print("\n=== Підключення до БД (retry) ===")
random.seed(42)
try:
    conn = connect_db("localhost:5432")
    print(f"  З'єднання: {conn}")
except DatabaseError as e:
    print(f"  DatabaseError: {e}")
