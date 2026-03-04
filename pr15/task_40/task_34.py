# Завдання 34 — Замикання (closure)

def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

triple = make_multiplier(3)
times5 = make_multiplier(5)
print([triple(i) for i in range(1, 6)])
print([times5(i) for i in range(1, 6)])
