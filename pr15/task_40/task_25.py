# Завдання 25 — Двійковий пошук

def binary_search(lst, target):
    lo, hi = 0, len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:   return mid
        elif lst[mid] < target:  lo = mid + 1
        else:                    hi = mid - 1
    return -1

arr = list(range(0, 100, 5))
print(f"Індекс 35: {binary_search(arr, 35)}")
print(f"Індекс 99: {binary_search(arr, 99)}")
