# Завдання 11 — Кілька типів виключень в одному except

def parse(value):
    try:
        return int(value) * 2
    except (ValueError, TypeError) as e:
        print(f"  ValueError або TypeError: {e}")
        return None

for v in ["5", "abc", None, "10"]:
    r = parse(v)
    if r is not None: print(f"  '{v}' * 2 = {r}")
