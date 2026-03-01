# Розділ 4 — Блок finally для очищення ресурсів

import tempfile, os

def read_file(filename):
    f = None
    try:
        f = open(filename, "r", encoding="utf-8")
        content = f.read()
        print(f"  Вміст: {content[:50]}")
        return content
    except FileNotFoundError:
        print(f"  Файл '{filename}' не знайдено")
    except PermissionError:
        print(f"  Немає прав для читання '{filename}'")
    finally:
        if f:
            f.close()
            print("  [finally] Файл закрито")
        else:
            print("  [finally] Файл не було відкрито")

print("=== Читання існуючого файлу ===")
with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as tmp:
    tmp.write("Привіт, це тестовий файл!")
    tmp_name = tmp.name
read_file(tmp_name)
os.unlink(tmp_name)

print("\n=== Читання неіснуючого файлу ===")
read_file("nonexistent.txt")

print("\n=== Симуляція з'єднання з БД ===")
def db_operation(should_fail=False):
    connection = None
    try:
        print("  Відкриваємо з'єднання...")
        if should_fail:
            raise ConnectionError("Не вдалося підключитися до БД")
        connection = {"status": "open"}
        print("  Виконуємо запит... дані отримано")
    except ConnectionError as e:
        print(f"  Помилка з'єднання: {e}")
    finally:
        if connection:
            connection["status"] = "closed"
        print("  [finally] Завжди виконується")

db_operation(should_fail=False)
print()
db_operation(should_fail=True)
