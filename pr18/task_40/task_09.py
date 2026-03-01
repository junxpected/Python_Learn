# Завдання 09 — Відкриття файлу (FileNotFoundError)

import os, tempfile
fname = tempfile.mktemp(suffix=".txt")
# Файл ще не існує
try:
    with open(fname) as f: print(f.read())
except FileNotFoundError:
    print(f"Файл не знайдено: {fname}")

# Створюємо і читаємо
with open(fname, "w") as f: f.write("Привіт!")
with open(fname) as f: print("Вміст:", f.read())
os.unlink(fname)
