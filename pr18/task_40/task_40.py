# Завдання 40 — Фінальна задача: надійний калькулятор

class CalculatorError(Exception): pass
class DivisionByZeroError(CalculatorError): pass
class InvalidInputError(CalculatorError): pass

class Calculator:
    def __init__(self):
        self.history = []

    def calculate(self, expr):
        try:
            parts = expr.strip().split()
            if len(parts) != 3:
                raise InvalidInputError(f"Формат: 'число оператор число', отримано: '{expr}'")
            a, op, b = parts
            a, b = float(a), float(b)
            if op == "+" : result = a + b
            elif op == "-": result = a - b
            elif op == "*": result = a * b
            elif op == "/":
                if b == 0: raise DivisionByZeroError(f"Ділення на нуль: {a}/{b}")
                result = a / b
            elif op == "**": result = a ** b
            else: raise InvalidInputError(f"Невідомий оператор: '{op}'")
            entry = f"{expr} = {result:.4g}"
            self.history.append(entry)
            return result
        except (ValueError, TypeError):
            raise InvalidInputError(f"Некоректні числа у виразі: '{expr}'")

    def show_history(self):
        print("  Історія:")
        for h in self.history: print(f"    {h}")

calc = Calculator()
expressions = ["10 + 5", "20 / 0", "abc * 2", "9 ** 0.5", "100 - 37", "50 / 8", "7 ? 2"]
print("=== Калькулятор ===")
for expr in expressions:
    try:
        r = calc.calculate(expr)
        print(f"  {expr} = {r:.4g}")
    except DivisionByZeroError as e:
        print(f"  DivisionByZeroError: {e}")
    except InvalidInputError as e:
        print(f"  InvalidInputError: {e}")
calc.show_history()
