# Розділ 1 — Цикли у Python: for та while

# --- for по списку ---
fruits = ["яблуко", "банан", "вишня", "манго"]
print("=== for по списку ===")
for fruit in fruits:
    print(f"  {fruit}")

# --- for по рядку ---
print("\n=== for по рядку ===")
for char in "Python":
    print(f"  '{char}'", end=" ")
print()

# --- for з range ---
print("\n=== for з range ===")
for i in range(1, 11):
    print(i, end=" ")
print()

# --- for з enumerate ---
print("\n=== enumerate ===")
for i, val in enumerate(fruits, start=1):
    print(f"  {i}. {val}")

# --- while ---
print("\n=== while ===")
n = 1
while n <= 5:
    print(f"  n = {n}")
    n += 1

# --- while з break ---
print("\n=== while з break ===")
count = 0
while True:
    count += 1
    if count == 4:
        print(f"  Зупинка на {count}")
        break

# --- continue ---
print("\n=== for з continue (парні) ===")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i, end=" ")
print()
