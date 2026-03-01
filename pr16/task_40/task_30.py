# Завдання 30 — Розбиття списку на підсписки (chunks)

def chunk_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

data = list(range(1, 13))
print("Оригінал:", data)
print("По 3:", chunk_list(data, 3))
print("По 4:", chunk_list(data, 4))
