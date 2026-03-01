# Завдання 36 — assert як легкий варіант перевірки

def calc_discount(price, discount_pct):
    try:
        assert 0 <= discount_pct <= 100, f"Знижка {discount_pct}% поза діапазоном [0,100]"
        assert price > 0, f"Ціна {price} має бути більше нуля"
        return price * (1 - discount_pct / 100)
    except AssertionError as e:
        print(f"  AssertionError: {e}")
        return None

for price, disc in [(1000, 20), (500, -10), (200, 110), (800, 0)]:
    r = calc_discount(price, disc)
    if r is not None:
        print(f"  Ціна {price} зі знижкою {disc}%: {r:.2f}")
