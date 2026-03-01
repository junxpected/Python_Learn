# Завдання 10 — Обробка PermissionError

import stat, os, tempfile
fname = tempfile.mktemp(suffix=".txt")
with open(fname, "w") as f: f.write("secret")
os.chmod(fname, stat.S_IWRITE)  # прибираємо права читання

try:
    with open(fname, "r") as f: print(f.read())
except PermissionError as e:
    print(f"PermissionError: {e}")
finally:
    os.chmod(fname, stat.S_IREAD | stat.S_IWRITE)
    os.unlink(fname)
    print("[finally] Файл очищено")
