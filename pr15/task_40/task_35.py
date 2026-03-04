# Завдання 35 — Цикл по словнику

grades = {"Аня": 95, "Богдан": 72, "Віта": 88, "Гліб": 61}

def letter_grade(score):
    if score >= 90: return "A"
    if score >= 75: return "B"
    if score >= 60: return "C"
    return "F"

for name, score in sorted(grades.items(), key=lambda x: x[1], reverse=True):
    print(f"  {name:<10} {score}  ({letter_grade(score)})")
