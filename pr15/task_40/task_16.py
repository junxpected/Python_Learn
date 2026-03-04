# Завдання 16 — Lambda функція

square  = lambda x: x ** 2
add     = lambda a, b: a + b
is_even = lambda x: x % 2 == 0

print(square(7))
print(add(3, 4))
print([x for x in range(10) if is_even(x)])
