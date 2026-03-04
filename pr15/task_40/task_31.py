# Завдання 31 — Цикл while — вгадай число (симуляція)

import random
random.seed(7)
secret = random.randint(1, 20)
guesses = [10, 15, 17, secret]

attempts = 0
for guess in guesses:
    attempts += 1
    print(f"Спроба {attempts}: {guess}", end=" → ")
    if guess < secret:   print("Більше")
    elif guess > secret: print("Менше")
    else:
        print(f"Вгадав за {attempts} спроб!")
        break
