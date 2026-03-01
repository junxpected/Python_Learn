# Завдання 38 — Вкладений словник: матриця суміжності графа

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}
print("Сусіди A:", list(graph["A"].keys()))
print("Відстань B→D:", graph["B"]["D"])
all_nodes = set(graph.keys())
print("Всі вузли:", all_nodes)
