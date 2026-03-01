# Розділ 5 — Власні виключення

class ValidationError(Exception):
    """Помилка валідації даних."""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"[{field}] {message}")

class InsufficientFundsError(Exception):
    """Недостатньо коштів на рахунку."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Баланс {balance} грн, потрібно {amount} грн")

class AgeRestrictionError(Exception):
    """Вікове обмеження."""
    pass

# --- Валідація форми ---
def register_user(name, email, age):
    if not name or len(name) < 2:
        raise ValidationError("name", "Ім'я занадто коротке")
    if "@" not in email:
        raise ValidationError("email", "Некоректний email")
    if not (0 < age < 120):
        raise ValidationError("age", "Вік поза допустимим діапазоном")
    return f"Користувач {name} зареєстрований"

print("=== Валідація користувача ===")
test_cases = [
    ("Аня", "anya@mail.com", 21),
    ("A", "anya@mail.com", 21),
    ("Богдан", "bogdan_mail", 22),
    ("Віта", "vita@mail.com", -5),
]
for name, email, age in test_cases:
    try:
        print(" ", register_user(name, email, age))
    except ValidationError as e:
        print(f"  ValidationError — поле '{e.field}': {e.message}")

# --- Банківський рахунок ---
def withdraw(balance, amount):
    if amount <= 0:
        raise ValidationError("amount", "Сума має бути більше нуля")
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

print("\n=== Зняття коштів ===")
for bal, amt in [(1000, 500), (200, 800), (500, 0)]:
    try:
        new_bal = withdraw(bal, amt)
        print(f"  Знято {amt} грн. Залишок: {new_bal} грн")
    except InsufficientFundsError as e:
        print(f"  InsufficientFundsError: {e}")
    except ValidationError as e:
        print(f"  ValidationError: {e}")
