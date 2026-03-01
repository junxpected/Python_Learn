# Завдання 28 — Обробка UnicodeDecodeError при читанні файлу

import tempfile, os

# Записуємо байти які не є UTF-8
fname = tempfile.mktemp(suffix=".txt")
with open(fname, "wb") as f:
    f.write(b"normal text \xff\xfe broken")

try:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError: {e}")
    with open(fname, "r", encoding="latin-1") as f:
        content = f.read()
    print(f"Прочитано з latin-1: {repr(content)}")
finally:
    os.unlink(fname)
