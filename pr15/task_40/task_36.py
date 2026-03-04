# Завдання 36 — Підрахунок символів у рядку

def char_count(text):
    result = {}
    for ch in text.lower():
        if ch.isalpha():
            result[ch] = result.get(ch, 0) + 1
    return result

freq = char_count("Hello World Python")
top5 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
print("Топ-5 символів:", top5)
