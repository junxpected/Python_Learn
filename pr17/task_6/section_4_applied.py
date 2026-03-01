# Розділ 4 — Задачі з використанням множин та словників

# --- Задача 1: підрахунок частоти слів ---
text = "python це мова python дуже популярна мова програмування python"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Частота слів:", freq)
print("Найчастіше:", max(freq, key=freq.get))

# --- Задача 2: унікальні відвідувачі сайту ---
day1 = {"user1", "user2", "user3", "user4"}
day2 = {"user3", "user4", "user5", "user6"}
day3 = {"user1", "user5", "user7"}

all_users = day1 | day2 | day3
returning = day1 & day2
new_day2 = day2 - day1

print("\nВсього унікальних:", len(all_users))
print("Повернулись на 2-й день:", returning)
print("Нові на 2-й день:", new_day2)

# --- Задача 3: групування студентів за оцінками ---
grades = [
    ("Аня", 95), ("Богдан", 72), ("Віта", 88),
    ("Гліб", 61), ("Діна", 91), ("Євген", 74),
]

grouped = {"відмінно": [], "добре": [], "задовільно": []}
for name, grade in grades:
    if grade >= 90:
        grouped["відмінно"].append(name)
    elif grade >= 75:
        grouped["добре"].append(name)
    else:
        grouped["задовільно"].append(name)

print("\nГрупи студентів:")
for group, names in grouped.items():
    print(f"  {group}: {names}")
