# Завдання 37 — ExceptionGroup (Python 3.11+) — симуляція через список

errors = []

def validate_form(data):
    if not data.get("name"):
        errors.append(ValueError("Поле 'name' обов'язкове"))
    if not data.get("email") or "@" not in data.get("email",""):
        errors.append(ValueError("Некоректний email"))
    age = data.get("age", 0)
    if not isinstance(age, int) or age < 18:
        errors.append(ValueError(f"Вік {age} — менше 18"))

form = {"name": "", "email": "bad_email", "age": 15}
validate_form(form)

if errors:
    print(f"Знайдено {len(errors)} помилок:")
    for e in errors:
        print(f"  - {e}")
else:
    print("Форма коректна")
