import random


def calculate_demand(x):
    if 1 <= x <= 25:
        return 10
    elif 26 <= x <= 60:
        return 11
    elif 61 <= x <= 90:
        return 12
    else:
        return 13


demand = []
day = 10
total_demand = 0

for i in range(day):
    current_demand = calculate_demand(random.randint(0, 99))
    demand.append(current_demand)
    total_demand += current_demand

print(demand)
print(total_demand)
