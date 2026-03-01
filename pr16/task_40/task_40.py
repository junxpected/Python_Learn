# Завдання 40 — Аналіз оцінок студентів 

grades = {
    "Аня":    [95, 87, 92, 88, 76],
    "Богдан": [70, 65, 80, 72, 68],
    "Віта":   [100, 98, 95, 99, 97],
    "Гліб":   [55, 60, 58, 62, 50],
}

# Формуємо статистику як список кортежів
stats = [
    (name, round(sum(g) / len(g), 1), min(g), max(g))
    for name, g in grades.items()
]

# Сортуємо за середньою оцінкою (спадання)
stats.sort(key=lambda x: x[1], reverse=True)

print(f"{'Студент':<10} {'Середня':>8} {'Мін':>5} {'Макс':>5}")
print("-" * 32)
for name, avg, mn, mx in stats:
    print(f"{name:<10} {avg:>8} {mn:>5} {mx:>5}")

print("\nНайкращий студент:", stats[0][0])
print("Відмінники (avg >= 90):", [s[0] for s in stats if s[1] >= 90])
print("Загальна кількість оцінок:", sum(len(g) for g in grades.values()))
