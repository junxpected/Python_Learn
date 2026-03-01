# Завдання 21 — Власний клас виключення

class AppError(Exception):
    pass

class NegativeValueError(AppError):
    def __init__(self, value):
        super().__init__(f"Від'ємне значення неприпустиме: {value}")
        self.value = value

def sqrt(x):
    if x < 0:
        raise NegativeValueError(x)
    return x ** 0.5

for val in [9, 16, -4, 25, -1]:
    try:
        print(f"  sqrt({val}) = {sqrt(val):.2f}")
    except NegativeValueError as e:
        print(f"  NegativeValueError: {e}")
