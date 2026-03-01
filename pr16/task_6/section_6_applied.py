# Розділ 6 — Задача: Система обліку товарів магазину

# Товар: (назва, категорія, ціна, кількість)
inventory = [
    ("Молоко", "молочне", 35.50, 100),
    ("Хліб", "хлібобулочне", 22.00, 200),
    ("Сир", "молочне", 120.00, 50),
    ("Яблука", "фрукти", 45.00, 80),
    ("Банани", "фрукти", 38.00, 60),
    ("Кефір", "молочне", 28.00, 90),
    ("Печиво", "кондитерське", 55.00, 40),
]

print("=== КАТАЛОГ ТОВАРІВ ===")
for name, cat, price, qty in inventory:
    print(f"  {name:<12} | {cat:<16} | {price:>7.2f} грн | {qty} шт")

# Фільтрація: тільки молочні
dairy = [item for item in inventory if item[1] == "молочне"]
print(f"\n=== МОЛОЧНІ ТОВАРИ ({len(dairy)}) ===")
for name, _, price, qty in dairy:
    print(f"  {name}: {price} грн")

# Сортування за ціною
by_price = sorted(inventory, key=lambda x: x[2])
print("\n=== ЗА ЦІНОЮ (зростання) ===")
for name, _, price, _ in by_price:
    print(f"  {name}: {price:.2f} грн")

# Підрахунок вартості запасів
total_value = sum(price * qty for _, _, price, qty in inventory)
print(f"\n=== ЗАГАЛЬНА ВАРТІСТЬ ЗАПАСІВ: {total_value:,.2f} грн ===")

# Товари, яких менше 60 штук
low_stock = [item for item in inventory if item[3] < 60]
print(f"\n=== МАЛИЙ ЗАЛИШОК (<60 шт) ===")
for name, _, _, qty in low_stock:
    print(f"  {name}: {qty} шт")

# Унікальні категорії
categories = sorted(set(item[1] for item in inventory))
print("\n=== КАТЕГОРІЇ ===", categories)
