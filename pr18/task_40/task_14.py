# Завдання 14 — Перевірка коректності даних для середнього

def average(values):
    try:
        nums = [float(v) for v in values]
        if not nums:
            raise ZeroDivisionError("Порожній список")
        return sum(nums) / len(nums)
    except ValueError as e:
        print(f"  ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"  ZeroDivisionError: {e}")
    return None

print(average([1, 2, 3, 4]))
print(average([1, "abc", 3]))
print(average([]))
