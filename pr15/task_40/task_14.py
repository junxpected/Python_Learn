# Завдання 14 — *args — довільна кількість аргументів

def total(*nums):
    return sum(nums)

print(total(1, 2, 3))
print(total(10, 20, 30, 40, 50))
