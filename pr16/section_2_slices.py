# Розділ 2 — Індексація та зрізи

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Список:", data)
print("Кортеж:", t)

# Індексація
print("\nПрямий індекс data[0]:", data[0])
print("Зворотній data[-1]:", data[-1])
print("data[3]:", data[3])

# Зрізи списку
print("\ndata[:4]:", data[:4])
print("data[6:]:", data[6:])
print("data[2:7]:", data[2:7])
print("data[::2]:", data[::2])
print("data[::-1]:", data[::-1])

# Зрізи кортежу
print("\nt[1:5]:", t[1:5])
print("t[::3]:", t[::3])
