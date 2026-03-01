# Завдання 30 — Підрахунок суми та середнього значень словника

prices = {"хліб": 22, "молоко": 35, "сир": 120, "яйця": 65}
total = sum(prices.values())
avg = total / len(prices)
print("Сума:", total)
print("Середня:", round(avg, 2))
print("Найдорожче:", max(prices, key=prices.get))
