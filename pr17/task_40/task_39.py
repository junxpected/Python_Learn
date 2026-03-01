# Завдання 39 — Операції над множинами в циклі

teams = {
    "команда_1": {"Аня", "Богдан", "Віта"},
    "команда_2": {"Богдан", "Гліб", "Діна"},
    "команда_3": {"Аня", "Євген", "Гліб"},
}
all_members = set().union(*teams.values())
print("Всі учасники:", all_members)

in_multiple = set()
members_list = list(teams.values())
for i in range(len(members_list)):
    for j in range(i+1, len(members_list)):
        in_multiple |= members_list[i] & members_list[j]
print("В кількох командах:", in_multiple)
