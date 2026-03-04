# Завдання 40 — Фінальна задача: статистика оцінок

def get_stats(scores):
    n = len(scores)
    mean = sum(scores) / n
    sorted_s = sorted(scores)
    median = sorted_s[n // 2] if n % 2 else (sorted_s[n//2-1] + sorted_s[n//2]) / 2
    spread = max(scores) - min(scores)
    passing = [s for s in scores if s >= 60]
    return {"mean": round(mean, 2), "median": median, "spread": spread,
            "pass_rate": round(len(passing)/n*100, 1)}

def grade(score):
    for limit, letter in [(90,"A"),(75,"B"),(60,"C"),(0,"F")]:
        if score >= limit:
            return letter

students = {
    "Аня":    [95, 88, 92, 97, 85],
    "Богдан": [72, 65, 70, 68, 75],
    "Віта":   [100, 98, 95, 99, 97],
    "Гліб":   [55, 60, 58, 50, 63],
}

print("Студент    Середня  Медіана  Оцінка")
print("-" * 38)
all_scores = []
for name, scores in students.items():
    st = get_stats(scores)
    all_scores.extend(scores)
    print(f"{name:<10} {st['mean']:>7}  {st['median']:>7}    {grade(st['mean'])}")

overall = get_stats(all_scores)
print(f"\nЗагальна: середня={overall['mean']}, pass rate={overall['pass_rate']}%")
