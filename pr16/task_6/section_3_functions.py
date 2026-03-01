# Розділ 3 — Вбудовані функції та методи

nums = [15, 3, 42, 8, 23, 4, 16, 7]
print("Список:", nums)

# Базові функції
print("\nlen():", len(nums))
print("sum():", sum(nums))
print("min():", min(nums))
print("max():", max(nums))
print("sorted():", sorted(nums))
print("sorted(reverse=True):", sorted(nums, reverse=True))

# Методи списку
nums.sort()
print("\nПісля sort():", nums)
nums.reverse()
print("Після reverse():", nums)
print("count(3):", nums.count(3))
nums.append(3)
print("Після append(3):", nums)
print("index(42):", nums.index(42))

# Методи кортежу
t = (5, 1, 5, 3, 5, 2)
print("\nКортеж:", t)
print("count(5):", t.count(5))
print("index(3):", t.index(3))
