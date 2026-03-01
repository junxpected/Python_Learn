# Завдання 29 — Захист від нескінченного циклу через StopIteration

def limited_range(start, stop):
    current = start
    while True:
        if current >= stop:
            raise StopIteration(f"Досягнуто межі {stop}")
        yield current
        current += 1

gen = limited_range(0, 5)
try:
    while True:
        print(" ", next(gen))
except StopIteration as e:
    print(f"StopIteration: {e}")
