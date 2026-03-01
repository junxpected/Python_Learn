# Розділ 2 — Робота з ключами та значеннями у словниках

# Створення словників
person = {"ім'я": "Аня", "вік": 21, "місто": "Київ"}
empty = {}
from_keys = dict.fromkeys(["a", "b", "c"], 0)

print("Словник:", person)
print("З fromkeys:", from_keys)

# Доступ до значень
print("\nІм'я:", person["ім'я"])
print("Вік (get):", person.get("вік"))
print("Відсутній ключ (get з default):", person.get("email", "не вказано"))

# Додавання та зміна
person["email"] = "anya@example.com"
person["вік"] = 22
print("\nПісля додавання та зміни:", person)

# Видалення
removed = person.pop("місто")
print("Після pop('місто'):", person, "| видалено:", removed)

del person["email"]
print("Після del:", person)
