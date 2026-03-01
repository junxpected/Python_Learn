# Завдання 34 — Множинні операції над текстом

text1 = set("programming")
text2 = set("python")
print("Символи 'programming':", sorted(text1))
print("Символи 'python':", sorted(text2))
print("Спільні символи:", sorted(text1 & text2))
print("Унікальні для programming:", sorted(text1 - text2))
