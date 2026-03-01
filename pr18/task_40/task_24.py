# Завдання 24 — Обробка помилок при роботі з JSON

import json

strings = [
    '{"name": "Аня", "age": 21}',
    'не JSON',
    '{"prices": [10, 20, 30]}',
    '{broken',
]

for s in strings:
    try:
        data = json.loads(s)
        print(f"  OK: {data}")
    except json.JSONDecodeError as e:
        print(f"  JSONDecodeError: {e.msg}")
